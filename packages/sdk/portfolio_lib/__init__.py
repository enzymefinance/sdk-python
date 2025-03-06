import asyncio
from typing import TypedDict, Any
from web3.types import ChecksumAddress, HexStr, TxParams
from ..utils.clients import PublicClient, WalletClient
from .. import asset as assets
from . import asset_managers
from . import integrations

from .._internal.external_position_manager import (
    ACTION as EXTERNAL_POSITION_ACTION,
    call as call_external_position,
    call_encode as call_external_position_encode,
    call_decode as call_external_position_decode,
    CallArgs as ExternalPositionCallArgs,
    create as create_external_position,
    create_encode as create_external_position_encode,
    create_decode as create_external_position_decode,
    CreateArgs as CreateExternalPositionArgs,
    remove as remove_external_position,
    remove_encode as remove_external_position_encode,
    remove_decode as remove_external_position_decode,
    RemoveArgs as RemoveExternalPositionArgs,
    reactivate as reactivate_external_position,
    reactivate_encode as reactivate_external_position_encode,
    reactivate_decode as reactivate_external_position_decode,
    ReactivateArgs as ReactivateExternalPositionArgs,
)


from .._internal.integration_manager import (
    ACTION as INTEGRATION_ADAPTER_ACTION,
    SELECTOR as INTEGRATION_ADAPTER_SELECTOR,
    call as call_integration_adapter,
    call_encode as call_integration_adapter_encode,
    call_decode as call_integration_adapter_decode,
    CallArgs as CallIntegrationAdapterArgs,
    add_tracked_assets,
    add_tracked_assets_encode,
    add_tracked_assets_decode,
    AddTrackedAssetsArgs,
    remove_tracked_assets,
    remove_tracked_assets_encode,
    remove_tracked_assets_decode,
    RemoveTrackedAssetsArgs,
)


class VaultCallOnContractParams(TypedDict):
    client: WalletClient
    comptroller_proxy: ChecksumAddress
    contract: ChecksumAddress
    selector: HexStr
    encoded_args: HexStr


async def vault_call_on_contract(
    client: WalletClient,
    comptroller_proxy: ChecksumAddress,
    contract: ChecksumAddress,
    selector: HexStr,
    encoded_args: HexStr,
) -> TxParams:
    contract = client.contract(comptroller_proxy, "IComptrollerLib")
    function = contract.functions.vaultCallOnContract(contract, selector, encoded_args)
    return await client.populated_transaction(function)


async def get_portfolio(
    client: PublicClient,
    vault_proxy: ChecksumAddress,
) -> dict[str, Any]:
    external_position_addresses, tracked_asset_addresses = await asyncio.gather(
        get_active_external_positions(client, vault_proxy),
        get_tracked_assets(client, vault_proxy),
    )

    # Prepare all coroutines for external positions
    external_position_coroutines = []
    for external_position in external_position_addresses:
        external_position_coroutines.extend(
            [
                get_external_position_type(client, external_position),
                get_external_position_debt_assets(client, external_position),
                get_external_position_managed_assets(client, external_position),
            ]
        )

    # Prepare all coroutines for tracked assets
    tracked_asset_coroutines = [
        assets.get_balance_of(client, asset, owner=vault_proxy)
        for asset in tracked_asset_addresses
    ]

    # Gather all data in parallel
    all_results = await asyncio.gather(
        *external_position_coroutines, *tracked_asset_coroutines
    )

    external_positions_data = []
    for i in range(0, len(external_position_addresses) * 3, 3):
        external_position_type = all_results[i]
        debt_assets = all_results[i + 1]
        managed_assets = all_results[i + 2]

        external_positions_data.append(
            {
                "external_position": external_position_addresses[i // 3],
                "external_position_type": external_position_type,
                "debt_assets": debt_assets,
                "managed_assets": managed_assets,
            }
        )

    tracked_assets_data = []
    for i, asset in enumerate(tracked_asset_addresses):
        amount = all_results[len(external_position_coroutines) + i]
        tracked_assets_data.append(
            {
                "asset": asset,
                "amount": amount,
            }
        )

    return {
        "external_positions": external_positions_data,
        "tracked_assets": tracked_assets_data,
    }


async def get_tracked_assets(
    client: PublicClient,
    vault_proxy: ChecksumAddress,
) -> list[ChecksumAddress]:
    contract = client.contract(vault_proxy, "IVaultLib")
    function = contract.functions.getTrackedAssets()
    return await function.call()


# --------------------------------------------------------------------------------------------
# EXTERNAL POSITIONS
# --------------------------------------------------------------------------------------------


async def is_active_external_position(
    client: PublicClient,
    vault_proxy: ChecksumAddress,
    external_position: ChecksumAddress,
) -> bool:
    contract = client.contract(vault_proxy, "IVaultLib")
    function = contract.functions.isActiveExternalPosition(external_position)
    return await function.call()


async def get_total_value_for_all_external_positions(
    client: PublicClient,
    vault_proxy: ChecksumAddress,
) -> int:
    pass


async def get_active_external_positions(
    client: PublicClient,
    vault_proxy: ChecksumAddress,
) -> list[ChecksumAddress]:
    contract = client.contract(vault_proxy, "IVaultLib")
    function = contract.functions.getActiveExternalPositions()
    return await function.call()


async def get_external_position_managed_assets(
    client: PublicClient,
    external_position: ChecksumAddress,
) -> list[dict[ChecksumAddress, int]]:
    contract = client.contract(external_position, "IExternalPosition")
    function = contract.functions.getManagedAssets()
    assets, amounts = await function.call()
    assert all(amount is not None for amount in amounts), "Missing managed asset amount"
    return [
        {
            "asset": asset,
            "amount": amount,
        }
        for asset, amount in zip(assets, amounts)
    ]


async def get_external_position_debt_assets(
    client: PublicClient,
    external_position: ChecksumAddress,
) -> list[dict[ChecksumAddress, int]]:
    contract = client.contract(external_position, "IExternalPosition")
    function = contract.functions.getDebtAssets()
    assets, amounts = await function.call()
    assert all(amount is not None for amount in amounts), "Missing debt asset amount"
    return [
        {
            "asset": asset,
            "amount": amount,
        }
        for asset, amount in zip(assets, amounts)
    ]


async def get_external_position_assets(
    client: PublicClient,
    external_position: ChecksumAddress,
) -> dict[str, list[dict[ChecksumAddress, int]]]:
    debt_assets, managed_assets = await asyncio.gather(
        get_external_position_debt_assets(client, external_position),
        get_external_position_managed_assets(client, external_position),
    )
    return {
        "debt_assets": debt_assets,
        "managed_assets": managed_assets,
    }


async def get_external_position_type(
    client: PublicClient,
    external_position: ChecksumAddress,
) -> int:
    contract = client.contract(external_position, "IExternalPositionProxy")
    function = contract.functions.getExternalPositionType()
    return await function.call()


async def get_type_label(
    client: PublicClient,
    external_position_factory: ChecksumAddress,
    type_id: int,
) -> str:
    contract = client.contract(external_position_factory, "IExternalPositionFactory")
    function = contract.functions.getTypeLabel(type_id)
    return await function.call()
