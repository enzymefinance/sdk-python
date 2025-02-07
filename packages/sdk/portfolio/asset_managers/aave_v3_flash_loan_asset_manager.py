from web3 import Web3
from web3.types import ChecksumAddress, HexStr, TxParams
from eth_abi import encode
from ...utils.clients import PublicClient, WalletClient
from ....abis import abis


# --------------------------------------------------------------------------------------------
# FACTORY
# --------------------------------------------------------------------------------------------


def encode_deploy_proxy_construct_data(
    owner: ChecksumAddress,
    borrowed_assets_recipient: ChecksumAddress,
) -> HexStr:
    abi = abis.fetch("IAaveV3FlashLoanAssetManager")
    contract = Web3().eth.contract(abi=abi)
    return contract.encode_abi(
        "init",
        [owner, borrowed_assets_recipient],
    )


async def deploy_proxy(
    client: WalletClient,
    dispatcher_owned_beacon_factory: ChecksumAddress,
    construct_data: HexStr,
) -> TxParams:
    construct_data = Web3.to_bytes(hexstr=construct_data)
    contract = client.contract(
        dispatcher_owned_beacon_factory, "IDispatcherOwnedBeaconFactory"
    )
    function = contract.functions.deployProxy(construct_data)
    return await client.populated_transaction(function)


# --------------------------------------------------------------------------------------------
# LIB
# --------------------------------------------------------------------------------------------


FLASH_LOAN_CALLS_ENCODING = [
    {
        "type": "tuple[]",
        "name": "calls",
        "components": [
            {
                "name": "target",
                "type": "address",
            },
            {
                "name": "data",
                "type": "bytes",
            },
        ],
    },
]


def encode_flash_loan_calls(
    calls: list[ChecksumAddress, HexStr],
) -> HexStr:
    types = ["(address,bytes)[]"]
    args = [[[target, Web3.to_bytes(hexstr=data)] for target, data in calls]]
    return "0x" + encode(types, args).hex()


async def flash_loan(
    client: WalletClient,
    aave_v3_flash_loan_asset_manager: ChecksumAddress,
    assets: list[ChecksumAddress],
    amounts: list[int],
    encoded_calls: HexStr,
) -> TxParams:
    contract = client.contract(
        aave_v3_flash_loan_asset_manager, "IAaveV3FlashLoanAssetManager"
    )
    function = contract.functions.flashLoan(assets, amounts, encoded_calls)
    return await client.populated_transaction(function)


async def get_borrowed_assets_recipient(
    client: PublicClient,
    aave_v3_flash_loan_asset_manager: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(
        aave_v3_flash_loan_asset_manager, "IAaveV3FlashLoanAssetManager"
    )
    function = contract.functions.getBorrowedAssetsRecipient()
    return await function.call()


async def get_owner(
    client: PublicClient,
    aave_v3_flash_loan_asset_manager: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(
        aave_v3_flash_loan_asset_manager, "IAaveV3FlashLoanAssetManager"
    )
    function = contract.functions.getOwner()
    return await function.call()
