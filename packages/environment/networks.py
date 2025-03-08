from typing import Any, Literal, TypedDict, get_args
from web3.types import ChecksumAddress

from .assets import PrimitiveAsset


Network = Literal[42161, 8453, 1, 137]


NetworkSlug = Literal["arbitrum", "base", "ethereum", "polygon"]


class NetworkDefinitionCurrency(TypedDict):
    wrapper: ChecksumAddress
    native_token: PrimitiveAsset


class NetworkDefinitionExplorer(TypedDict):
    label: str
    url: str


class NetworkDefinition(TypedDict):
    currency: NetworkDefinitionCurrency
    explorer: NetworkDefinitionExplorer
    id: Network
    slug: NetworkSlug
    label: str
    rpc: str


def get_network(network_or_slug: Network | NetworkSlug) -> NetworkDefinition:
    if is_supported_network(network_or_slug):
        return NETWORKS[network_or_slug]
    if is_supported_network_slug(network_or_slug):
        return NETWORKS[NETWORK_BY_SLUG[network_or_slug]]
    raise ValueError(f"Invalid network {network_or_slug}")


def is_network_identifier(value: Any) -> bool:
    return is_supported_network(value) or is_supported_network_slug(value)


def is_supported_network_slug(value: Any) -> bool:
    return isinstance(value, str) and value in get_args(NetworkSlug)


def is_supported_network(value: Any) -> bool:
    return isinstance(value, int) and value in get_args(Network)


SLUG_BY_NETWORK = dict(zip(get_args(Network), get_args(NetworkSlug)))


NETWORK_BY_SLUG = dict(zip(get_args(NetworkSlug), get_args(Network)))


ARBITRUM: NetworkDefinition = {
    "currency": {
        "wrapper": "0x82af49447d8a07e3bd95bd0d56f35241523fbab1",
        "native_token": {
            "id": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "name": "Ether",
            "symbol": "ETH",
            "decimals": 18,
            "type": "primitive",  # AssetType from .assets
            "releases": [],
            "network": NETWORK_BY_SLUG["arbitrum"],
            "registered": False,
            "price_feed": {
                "type": "NONE",  # PriceFeedType from .price_feeds
            },
        },
    },
    "explorer": {
        "label": "Arbiscan",
        "url": "https://arbiscan.io/",
    },
    "id": NETWORK_BY_SLUG["arbitrum"],
    "label": "Arbitrum",
    "rpc": "https://arb1.arbitrum.io/rpc",
    "slug": "arbitrum",  # NetworkSlug
}


BASE: NetworkDefinition = {
    "currency": {
        "wrapper": "0x4200000000000000000000000000000000000006",
        "native_token": {
            "id": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "name": "Ether",
            "symbol": "ETH",
            "decimals": 18,
            "type": "primitive",  # AssetType from .assets
            "releases": [],
            "network": NETWORK_BY_SLUG["base"],
            "registered": False,
            "price_feed": {
                "type": "NONE",  # PriceFeedType from .price_feeds
            },
        },
    },
    "explorer": {
        "label": "BaseScan",
        "url": "https://basescan.org/",
    },
    "id": NETWORK_BY_SLUG["base"],
    "label": "Base",
    "rpc": "https://mainnet.base.org",
    "slug": "base",  # NetworkSlug
}


MAINNET: NetworkDefinition = {
    "currency": {
        "wrapper": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
        "native_token": {
            "id": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "name": "Ether",
            "symbol": "ETH",
            "decimals": 18,
            "type": "primitive",  # AssetType from .assets
            "releases": [],
            "network": NETWORK_BY_SLUG["ethereum"],
            "registered": False,
            "price_feed": {
                "type": "NONE",  # PriceFeedType from .price_feeds
            },
        },
    },
    "explorer": {
        "label": "Etherscan",
        "url": "https://etherscan.io",
    },
    "id": NETWORK_BY_SLUG["ethereum"],
    "label": "Ethereum",
    "rpc": "https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
    "slug": "ethereum",  # NetworkSlug
}


POLYGON: NetworkDefinition = {
    "currency": {
        "wrapper": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
        "native_token": {
            "id": "0x0000000000000000000000000000000000001010",
            "name": "Polygon Ecosystem Token",
            "symbol": "POL",
            "decimals": 18,
            "type": "primitive",  # AssetType from .assets
            "releases": [],
            "network": NETWORK_BY_SLUG["polygon"],
            "registered": False,
            "price_feed": {
                "type": "NONE",  # PriceFeedType from .price_feeds
            },
        },
    },
    "explorer": {
        "label": "Polygonscan",
        "url": "https://polygonscan.com",
    },
    "id": NETWORK_BY_SLUG["polygon"],
    "label": "Polygon",
    "rpc": "https://polygon-rpc.com",
    "slug": "polygon",  # NetworkSlug
}


NETWORKS = dict(zip(get_args(Network), [ARBITRUM, BASE, MAINNET, POLYGON]))
