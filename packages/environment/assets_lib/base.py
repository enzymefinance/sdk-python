from web3 import Web3
from ..releases import RELEASES
from ..assets import define_asset_list
from ..networks import NETWORK_BY_SLUG
from ..price_feeds import RateAsset


SULU = RELEASES["base"]["sulu"]


ASSETS = define_asset_list(
    NETWORK_BY_SLUG["base"],
    [
        {
            "decimals": 18,
            "id": "0x4200000000000000000000000000000000000006",
            "name": "Wrapped Ether",
            "releases": [SULU],
            "symbol": "WETH",
            "type": "primitive",
            "price_feed": {
                "type": "WETH",
            },
        },
        {
            "decimals": 18,
            "id": "0x7C298664BD6582f6f264c2Cb5a4B9cC09b6E3889",
            "name": "Melon Token",
            "releases": [],
            "symbol": "MLN",
            "type": "primitive",
            "price_feed": {
                "type": "NONE",
            },
        },
        {
            "decimals": 18,
            "id": "0x50c5725949A6F0c72E6C4a641F24049A917DB0Cb",
            "name": "Dai Stablecoin",
            "releases": [SULU],
            "symbol": "DAI",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x591e79239a7d679378eC8c847e5038150364C78F",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x9e1028F5F1D5eDE59748FFceE5532509976840E0",
            "name": "Compound",
            "releases": [SULU],
            "symbol": "COMP",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x9DDa783DE64A9d1A60c49ca761EbE528C35BA428",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
            "name": "USD Coin",
            "releases": [SULU],
            "symbol": "USDC",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x7e860098F58bBFC8648a4311b374B1D669a2bc6B",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2",
            "name": "Tether USD",
            "releases": [SULU],
            "symbol": "USDT",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xf19d560eB8d2ADf07BD6D13ed03e1D11215721F9",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 8,
            "id": "0x0555E30da8f98308EdB960aa94C0Db47230d2B9c",
            "name": "Wrapped BTC",
            "releases": [SULU],
            "symbol": "WBTC",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xCCADC697c55bbB68dc5bCdf8d3CBe83CdD4E071E",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xD4a0e0b9149BCee3C920d2E00b5dE09138fd8bb7",
            "name": "Aave Base WETH",
            "releases": [SULU],
            "symbol": "aBasWETH",
            "type": "aave-v3",
            "underlying": "0x4200000000000000000000000000000000000006",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x71041dddad3595F9CEd3DcCFBe3D1F4b0a16Bb70",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0x4e65fE4DbA92790696d040ac24Aa414708F5c0AB",
            "name": "Aave Base USDC",
            "releases": [SULU],
            "symbol": "aBasUSDC",
            "type": "aave-v3",
            "underlying": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x7e860098F58bBFC8648a4311b374B1D669a2bc6B",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "id": "0xbeeF010f9cb27031ad51e3333f9aF9C6B1228183",
            "decimals": 18,
            "name": "Steakhouse USDC",
            "symbol": "steakUSDC",
            "releases": [SULU],
            "type": "erc-4626",
            "underlying": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
            "protocol": "morpho",
            "price_feed": {
                "type": "DERIVATIVE_ERC4626",
                "address": "0x6889790Fb10A03bBf9dc86f1BEd3219b509F5367",
            },
        },
        {
            "id": "0xbEEf050a7485865A7a8d8Ca0CC5f7536b7a3443e",
            "decimals": 18,
            "name": "Steakhouse ETH",
            "symbol": "steakETH",
            "releases": [SULU],
            "type": "erc-4626",
            "underlying": "0x4200000000000000000000000000000000000006",
            "protocol": "morpho",
            "price_feed": {
                "type": "DERIVATIVE_ERC4626",
                "address": "0x6889790Fb10A03bBf9dc86f1BEd3219b509F5367",
            },
        },
    ],
)
