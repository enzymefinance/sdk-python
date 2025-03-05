from typing import TypedDict
from web3.types import ChecksumAddress, HexStr, TxParams
from ..utils.clients import WalletClient

class CallExtensionParams(TypedDict):
    client: WalletClient
    comptroller_proxy: ChecksumAddress
    extension_manager: ChecksumAddress
    action_id: int
    call_args: HexStr


async def call_extension(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    extension_manager: ChecksumAddress,
    action_id: int,
    call_args: HexStr
) -> TxParams:
    contract = client.contract(comptroller_proxy, "IComptrollerLib")
    function = contract.functions.callOnExtension(
        extension_manager, action_id, call_args
    )
    return await client.populated_transaction(function)
