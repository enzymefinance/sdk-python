import asyncio
from typing import List, Tuple
from web3.types import ChecksumAddress, TxParams
from utils.clients import WalletClient, PublicClient


# --------------------------------------------------------------------------------------------
# TRANSACTIONS
# --------------------------------------------------------------------------------------------


async def approve(
    client: WalletClient,
    asset: ChecksumAddress,
    spender: ChecksumAddress,
    amount: int,
) -> TxParams:
    contract = client.contract(asset, "IERC20")
    return await contract.functions.approve(spender, amount).call()


# --------------------------------------------------------------------------------------------
# READ FUNCTIONS
# --------------------------------------------------------------------------------------------


async def get_info(
    client: PublicClient,
    asset: ChecksumAddress,
) -> Tuple[str, str, int]:
    """
    returns: (name, symbol, decimals)
    """
    return await asyncio.gather(
        get_name(client, asset),
        get_symbol(client, asset),
        get_decimals(client, asset),
    )


async def get_name(
    client: PublicClient,
    asset: ChecksumAddress,
) -> str:
    # TODO: Handle case where name is a bytes32
    contract = client.contract(asset, "IERC20")
    return await contract.functions.name().call()


async def get_symbol(
    client: PublicClient,
    asset: ChecksumAddress,
) -> str:
    # TODO: Handle case where symbol is a bytes32
    contract = client.contract(asset, "IERC20")
    return await contract.functions.symbol().call()


async def get_balance_of(
    client: PublicClient,
    owner: ChecksumAddress,
    asset: ChecksumAddress,
) -> int:
    contract = client.contract(asset, "IERC20")
    return await contract.functions.balanceOf(owner).call()


async def get_balances_of(
    client: PublicClient,
    owner: ChecksumAddress,
    assets: List[ChecksumAddress],
) -> List[int]:
    return await asyncio.gather(
        *[get_balance_of(client, owner, asset) for asset in assets],
    )


async def get_allowance(
    client: PublicClient,
    asset: ChecksumAddress,
    owner: ChecksumAddress,
    spender: ChecksumAddress,
) -> int:
    contract = client.contract(asset, "IERC20")
    return await contract.functions.allowance(owner, spender).call()


async def get_decimals(
    client: PublicClient,
    asset: ChecksumAddress,
) -> int:
    contract = client.contract(asset, "IERC20")
    return await contract.functions.decimals().call()


async def get_total_supply(
    client: PublicClient,
    asset: ChecksumAddress,
) -> int:
    contract = client.contract(asset, "IERC20")
    return await contract.functions.totalSupply().call()


async def get_canonical_value(
    client: PublicClient,
    value_interpreter: ChecksumAddress,
    base_asset: ChecksumAddress,
    quote_asset: ChecksumAddress,
    amount: int,
) -> int:
    # TODO: simulate contract?
    contract = client.contract(value_interpreter, "IValueInterpreter")
    return await contract.functions.calcCanonicalAssetValue(base_asset, amount, quote_asset).call()
