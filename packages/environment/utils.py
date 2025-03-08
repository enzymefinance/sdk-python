from web3 import Web3
from web3.constants import ADDRESS_ZERO
from .networks import Network, NetworkSlug, is_network_identifier, get_network
from .releases import Deployment, is_deployment
from .deployments_lib.all import DEPLOYMENTS


def is_non_zero_address(address: str) -> bool:
    return Web3.is_checksum_address(address) and address != ADDRESS_ZERO


def get_deployment(
    deployment_or_network: Deployment | Network | NetworkSlug,
) -> Deployment:
    if is_deployment(deployment_or_network):
        return deployment_or_network
    if is_network_identifier(deployment_or_network):
        network = get_network(deployment_or_network)
        for deployment in DEPLOYMENTS:
            if deployment["network"] == network["id"] and deployment["kind"] == "live":
                return deployment
        raise ValueError(f"Missing deployment for network {network['slug']}")
    raise ValueError(f"Invalid deployment or network {deployment_or_network}")
