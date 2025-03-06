from typing import TypedDict
from web3.types import ChecksumAddress
from .utils.clients import PublicClient
from .configuration_lib import policy


async def get_enabled_policies(
    client: PublicClient,
    comptroller_proxy: ChecksumAddress,
    policy_manager: ChecksumAddress,
) -> list[ChecksumAddress]:
    contract = client.contract(policy_manager, "IPolicyManager")
    function = contract.functions.getEnabledPoliciesForFund(comptroller_proxy)
    return await function.call()
