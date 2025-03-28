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
            "releases": [SULU],
            "symbol": "MLN",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x122b5334A8b55861dBc6729c294451471FbF318D",
                "rate_asset": RateAsset.USD,
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
        {
            "decimals": 8,
            "id": "0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf",
            "name": "Coinbase Wrapped BTC",
            "releases": [SULU],
            "symbol": "cbBTC",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x07DA0E54543a844a80ABE69c8A12F22B3aA59f9D",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xc1CBa3fCea344f92D9239c08C0568f6F2F0ee452",
            "name": "Wrapped liquid staked Ether 2.0",
            "releases": [SULU],
            "symbol": "wstETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x43a5C292A453A3bF3606fa856197f09D7B74251a",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x99CBC45ea5bb7eF3a5BC08FB1B7E56bB2442Ef0D",
            "name": "Aave Base wstETH",
            "releases": [SULU],
            "symbol": "aBaswstETH",
            "type": "aave-v3",
            "underlying": "0xc1CBa3fCea344f92D9239c08C0568f6F2F0ee452",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x43a5C292A453A3bF3606fa856197f09D7B74251a",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x1Bc71130A0e39942a7658878169764Bbd8A45993",
            "name": "KelpDao Restaked ETH",
            "releases": [SULU],
            "symbol": "rsETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xd7221b10FBBC1e1ba95Fd0B4D031C15f7F365296",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0xDBFeFD2e8460a6Ee4955A68582F85708BAEA60A3",
            "name": "Super OETH",
            "symbol": "superOETHb",
            "releases": [SULU],
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x71041dddad3595F9CEd3DcCFBe3D1F4b0a16Bb70",
                "rate_asset": RateAsset.USD,
                "non_standard": True,
                "pegged_to": "ETH",
            },
        },
        {
            "id": "0x7FcD174E80f264448ebeE8c88a7C4476AAF58Ea6",
            "name": "Wrapped Super OETH",
            "symbol": "wsuperOETHb",
            "decimals": 18,
            "releases": [SULU],
            "type": "primitive",
            "price_feed": {
                "type": "DERIVATIVE_ERC4626",
                "address": "0x6889790Fb10A03bBf9dc86f1BEd3219b509F5367",
                "non_standard": True,
            },
        },
    ],
)
