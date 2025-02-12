from web3 import Web3
from web3.types import ChecksumAddress, HexStr, TxParams
from eth_abi import encode, decode
from typing import Callable, Any, Tuple
from .extensions import call_extension
from ..utils.clients import WalletClient


ACTION = {
    "call_on_integration": 0,
    "add_tracked_assets": 1,
    "remove_tracked_assets": 2,
}

SELECTOR = {
    "action": "0xa7a19e00",  # action(address,bytes,bytes)
    "claim_rewards": "0xb9dfbacc",  # claimRewards(address,bytes,bytes)
    "lend": "0x099f7515",  # lend(address,bytes,bytes)
    "lend_and_stake": "0x29fa046e",  # lendAndStake(address,bytes,bytes)
    "redeem": "0xc29fa9dd",  # redeem(address,bytes,bytes)
    "stake": "0xfa7dd04d",  # stake(address,bytes,bytes)
    "take_multiple_orders": "0x0e7f692d",  # takeMultipleOrders(address,bytes,bytes)
    "take_order": "0x03e38a2b",  # takeOrder(address,bytes,bytes)
    "transfer": "0x3461917c",  # transfer(address,bytes,bytes)
    "unstake": "0x68e30677",  # unstake(address,bytes,bytes)
    "unstake_and_redeem": "0x8334eb99",  # unstakeAndRedeem(address,bytes,bytes)
    "wrap": "0xa5ca2d71",  # wrap(address,bytes,bytes)
}


def make_use(selector: HexStr, encoder: Callable) -> Callable:
    async def use_integration(
        client: WalletClient,
        comptroller_proxy: ChecksumAddress,
        integration_manager: ChecksumAddress,
        integration_adapter: ChecksumAddress,
        call_args: Any,
    ) -> TxParams:
        return await call(
            client,
            comptroller_proxy,
            integration_manager,
            integration_adapter,
            selector,
            encoder(call_args),
        )

    return use_integration


# --------------------------------------------------------------------------------------------
# CALL ON INTEGRATION
# --------------------------------------------------------------------------------------------

CALL_ENCODING = [
    {
        "type": "address",
        "name": "adapter",
    },
    {
        "type": "bytes4",
        "name": "selector",
    },
    {
        "type": "bytes",
        "name": "integrationData",
    },
]


def call_encode(
    function_selector: HexStr,
    integration_adapter: ChecksumAddress,
    call_args: HexStr = "0x",
) -> HexStr:
    types = [e["type"] for e in CALL_ENCODING]
    values = [
        integration_adapter,
        function_selector,
        Web3.to_bytes(hexstr=call_args),
    ]
    return encode(types, values)


def call_decode(encoded: HexStr) -> Tuple[HexStr, ChecksumAddress, HexStr]:
    """
    Returns:
        (function_selector, integration_adapter, call_args)
    """
    types = [e["type"] for e in CALL_ENCODING]
    return decode(types, Web3.to_bytes(hexstr=encoded))


async def call(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    integration_manager: ChecksumAddress,
    integration_adapter: ChecksumAddress,
    function_selector: HexStr,
    call_args: HexStr = "0x",
) -> TxParams:
    return await call_extension(
        client,
        comptroller_proxy,
        integration_manager,
        ACTION["call_on_integration"],
        call_encode(function_selector, integration_adapter, call_args),
    )


# --------------------------------------------------------------------------------------------
# ADD TRACKED ASSET
# --------------------------------------------------------------------------------------------

ADD_TRACKED_ASSETS_ENCODING = [
    {
        "type": "address[]",
        "name": "assets",
    },
]


def add_tracked_assets_encode(add_assets: list[ChecksumAddress]) -> HexStr:
    types = [e["type"] for e in ADD_TRACKED_ASSETS_ENCODING]
    values = [add_assets]
    return encode(types, values)


def add_tracked_assets_decode(encoded: HexStr) -> list[ChecksumAddress]:
    types = [e["type"] for e in ADD_TRACKED_ASSETS_ENCODING]
    decoded = decode(types, Web3.to_bytes(hexstr=encoded))
    return decoded[0]


async def add_tracked_assets(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    integration_manager: ChecksumAddress,
    add_assets: list[ChecksumAddress],
) -> TxParams:
    return await call_extension(
        client,
        comptroller_proxy,
        integration_manager,
        ACTION["add_tracked_assets"],
        add_tracked_assets_encode(add_assets),
    )


# --------------------------------------------------------------------------------------------
# REMOVE TRACKED ASSET
# --------------------------------------------------------------------------------------------

REMOVE_TRACKED_ASSETS_ENCODING = [
    {
        "type": "address[]",
        "name": "assets",
    },
]


def remove_tracked_assets_encode(remove_assets: list[ChecksumAddress]) -> HexStr:
    types = [e["type"] for e in REMOVE_TRACKED_ASSETS_ENCODING]
    values = [remove_assets]
    return encode(types, values)


def remove_tracked_assets_decode(encoded: HexStr) -> list[ChecksumAddress]:
    types = [e["type"] for e in REMOVE_TRACKED_ASSETS_ENCODING]
    decoded = decode(types, Web3.to_bytes(hexstr=encoded))
    return decoded[0]


async def remove_tracked_assets(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    integration_manager: ChecksumAddress,
    remove_assets: list[ChecksumAddress],
) -> TxParams:
    return await call_extension(
        client,
        comptroller_proxy,
        integration_manager,
        ACTION["remove_tracked_assets"],
        remove_tracked_assets_encode(remove_assets),
    )
