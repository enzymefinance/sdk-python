from web3.types import ChecksumAddress, TxParams
from .utils.clients import PublicClient, WalletClient


# --------------------------------------------------------------------------------------------
# TRANSACTIONS
# --------------------------------------------------------------------------------------------


async def set_freely_transferable_shares(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.setFreelyTransferableShares()
    return await client.populated_transaction(function)


async def set_nominated_owner(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
    nextNominatedOwner: ChecksumAddress,
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.setNominatedOwner(nextNominatedOwner)
    return await client.populated_transaction(function)


async def remove_nominated_owner(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.removeNominatedOwner()
    return await client.populated_transaction(function)


async def claim_ownership(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.claimOwnership()
    return await client.populated_transaction(function)


async def set_name(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
    name: str,
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.setName(name)
    return await client.populated_transaction(function)


async def set_symbol(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
    symbol: str,
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.setSymbol(symbol)
    return await client.populated_transaction(function)


async def add_asset_managers(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
    managers: list[ChecksumAddress],
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.addAssetManagers(managers)
    return await client.populated_transaction(function)


async def remove_asset_managers(
    client: WalletClient,
    vaultProxy: ChecksumAddress,
    managers: list[ChecksumAddress],
) -> TxParams:
    contract = client.contract(vaultProxy, "IVaultLib")
    function = contract.functions.removeAssetManagers(managers)
    return await client.populated_transaction(function)


# --------------------------------------------------------------------------------------------
# READ FUNCTIONS
# --------------------------------------------------------------------------------------------


async def get_name(
    client: PublicClient,
    vaultProxy: ChecksumAddress,
) -> str:
    contract = client.contract(vaultProxy, "IVaultLib")
    return await contract.functions.name().call()


async def get_symbol(
    client: PublicClient,
    vaultProxy: ChecksumAddress,
) -> str:
    contract = client.contract(vaultProxy, "IVaultLib")
    return await contract.functions.symbol().call()


async def get_owner(
    client: PublicClient,
    vaultProxy: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(vaultProxy, "IVaultLib")
    return await contract.functions.getOwner().call()


async def get_nominated_owner(
    client: PublicClient,
    vault: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(vault, "IVaultLib")
    return await contract.functions.getNominatedOwner().call()


async def get_denomination_asset(
    client: PublicClient,
    comptrollerProxy: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(comptrollerProxy, "IComptrollerLib")
    return await contract.functions.getDenominationAsset().call()


async def get_comptroller_proxy(
    client: PublicClient,
    vaultProxy: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(vaultProxy, "IVaultLib")
    return await contract.functions.getAccessor().call()


async def get_policy_manager(
    client: PublicClient,
    comptrollerProxy: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(comptrollerProxy, "IComptrollerLib")
    return await contract.functions.getPolicyManager().call()


async def get_fee_manager(
    client: PublicClient,
    comptrollerProxy: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(comptrollerProxy, "IComptrollerLib")
    return await contract.functions.getFeeManager().call()


async def shares_are_freely_transferable(
    client: PublicClient,
    vaultProxy: ChecksumAddress,
) -> bool:
    contract = client.contract(vaultProxy, "IVaultLib")
    return await contract.functions.sharesAreFreelyTransferable().call()


async def get_fund_deployer(
    client: PublicClient,
    vaultProxy: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(vaultProxy, "IVaultLib")
    return await contract.functions.getFundDeployer().call()
