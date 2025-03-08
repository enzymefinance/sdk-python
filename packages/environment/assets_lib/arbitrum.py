from web3 import Web3
from ..releases import RELEASES
from ..assets import define_asset_list
from ..networks import NETWORK_BY_SLUG
from ..price_feeds import RateAsset


SULU = RELEASES["arbitrum"]["sulu"]


ASSETS = define_asset_list(
    NETWORK_BY_SLUG["arbitrum"],
    [
        {
            "decimals": 18,
            "id": "0x040d1EdC9569d4Bab2D15287Dc5A4F10F56a56B8",
            "name": "Balancer",
            "releases": [SULU],
            "symbol": "BAL",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xBE5eA816870D11239c543F84b71439511D70B94f",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x354A6dA3fcde098F8389cad84b0182725c6C91dE",
            "name": "Compound",
            "releases": [SULU],
            "symbol": "COMP",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xe7C53FFd03Eb6ceF7d208bC4C13446c76d1E5884",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x11cDb42B0EB46D95f990BeDD4695A6e3fA034978",
            "name": "Curve DAO Token",
            "releases": [SULU],
            "symbol": "CRV",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xaebDA2c976cfd1eE1977Eac079B4382acb849325",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xaAFcFD42c9954C6689ef1901e03db742520829c5",
            "name": "Convex Token",
            "releases": [SULU],
            "symbol": "CVX",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x851175a919f36c8e30197c09a9A49dA932c2CC00",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x9623063377AD1B27544C965cCd7342f7EA7e88C7",
            "name": "Graph Token",
            "releases": [SULU],
            "symbol": "GRT",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x0F38D86FceF4955B705F35c9e41d1A16e0637c73",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x1DEBd73E752bEaF79865Fd6446b0c970EaE7732f",
            "name": "Coinbase Wrapped Staked ETH",
            "releases": [SULU],
            "symbol": "cbETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xa668682974E3f121185a3cD94f00322beC674275",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x2416092f143378750bb29b79eD961ab195CcEea5",
            "name": "Renzo Restaked ETH",
            "releases": [SULU],
            "symbol": "ezETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x11E1836bFF2ce9d6A5bec9cA79dc998210f3886d",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 9,
            "id": "0x2bcC6D6CdBbDC0a4071e48bb3B969b06B3330c07",
            "name": "Wrapped SOL",
            "releases": [SULU],
            "symbol": "SOL",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x24ceA4b8ce57cdA5058b924B9B9987992450590c",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 8,
            "id": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
            "name": "Wrapped BTC",
            "releases": [SULU],
            "symbol": "WBTC",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xd0C7101eACbB49F3deCcCc166d238410D6D46d57",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x3082CC23568eA640225c2467653dB90e9250AaA0",
            "name": "Radiant",
            "releases": [SULU],
            "symbol": "RDNT",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x20d0Fcab0ECFD078B036b6CAf1FaC69A6453b352",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x35751007a407ca6FEFfE80b3cB397736D2cf4dbe",
            "name": "Wrapped eETH",
            "releases": [SULU],
            "symbol": "weETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xE141425bc1594b8039De6390db1cDaf4397EA22b",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x4186BFC76E2E237523CBC30FD220FE055156b41F",
            "name": "KelpDao Restaked ETH",
            "releases": [SULU],
            "symbol": "rsETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xb0EA543f9F8d4B818550365d13F66Da747e1476A",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x565609fAF65B92F7be02468acF86f8979423e514",
            "name": "Wrapped AVAX",
            "releases": [SULU],
            "symbol": "WAVAX",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x8bf61728eeDCE2F32c456454d87B5d6eD6150208",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x5979D7b546E38E414F7E9822514be443A4800529",
            "name": "Wrapped liquid staked Ether 2.0",
            "releases": [SULU],
            "symbol": "wstETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xb523AE262D20A936BC152e6023996e46FDC2A95D",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
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
            "id": "0x8f5c1A99b1df736Ad685006Cb6ADCA7B7Ae4b514",
            "name": "Melon Token",
            "releases": [SULU],
            "symbol": "MLN",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xD07de6e37A011CCAfD375d7eb130205E0fa24d69",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x912CE59144191C1204E64559FE8253a0e49E6548",
            "name": "Arbitrum",
            "releases": [SULU],
            "symbol": "ARB",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xb2A824043730FE05F3DA2efaFa1CBbe83fa548D6",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xa9004A5421372E1D83fB1f85b0fc986c912f91f3",
            "name": "Wrapped BNB",
            "releases": [SULU],
            "symbol": "WBNB",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x6970460aabF80C5BE983C6b74e5D06dEDCA95D4A",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xaC800FD6159c2a2CB8fC31EF74621eB430287a5A",
            "name": "Optimism",
            "releases": [SULU],
            "symbol": "OP",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x205aaD468a11fd5D34fA7211bC6Bad5b3deB9b98",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
            "name": "USD Coin",
            "releases": [SULU],
            "symbol": "USDC",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x50834F3163758fcC1Df9973b6e91f0F0F0434aD3",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xba5DdD1f9d7F570dc94a51479a000E3BCE967196",
            "name": "Aave Token",
            "releases": [SULU],
            "symbol": "AAVE",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xaD1d5344AaDE45F43E596773Bcc4c423EAbdD034",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xbc011A12Da28e8F0f528d9eE5E7039E22F91cf18",
            "name": "swETH",
            "releases": [SULU],
            "symbol": "swETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x05Bc6e5Fb110589bb366A3Cd7CdBe143EeBA2168",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
            "name": "Dai Stablecoin",
            "releases": [SULU],
            "symbol": "DAI",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xc5C8E77B397E531B8EC06BFb0048328B30E9eCfB",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xEC70Dcb4A1EFa46b8F2D97C310C9c4790ba5ffA8",
            "name": "Rocket Pool ETH",
            "releases": [SULU],
            "symbol": "rETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xD6aB2298946840262FcC278fF31516D39fF611eF",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0xf97f4df75117a78c1A5a0DBb814Af92458539FB4",
            "name": "ChainLink Token",
            "releases": [SULU],
            "symbol": "LINK",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xb7c8Fb1dB45007F98A68Da0588e1AA524C317f27",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0xFa7F8980b0f1E64A2062791cc3b0871572f1F7f0",
            "name": "Uniswap",
            "releases": [SULU],
            "symbol": "UNI",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x9C917083fDb403ab5ADbEC26Ee294f6EcAda2720",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a",
            "name": "GMX",
            "releases": [SULU],
            "symbol": "GMX",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xDB98056FecFff59D032aB628337A4887110df3dB",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
            "name": "USD₮0",
            "releases": [SULU],
            "symbol": "USD₮0",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x3f3f5dF88dC9F13eac63DF89EC16ef6e7E25DdE7",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xe50fA9b3c56FfB159cB0FCA61F5c9D750e8128c8",
            "name": "Aave Arbitrum WETH",
            "releases": [SULU],
            "symbol": "aArbWETH",
            "type": "aave-v3",
            "underlying": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0x724dc807b04555b71ed48a6896b6F41593b8C637",
            "name": "Aave Arbitrum USDCn",
            "releases": [SULU],
            "symbol": "aArbUSDCn",
            "type": "aave-v3",
            "underlying": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x50834F3163758fcC1Df9973b6e91f0F0F0434aD3",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 8,
            "id": "0x078f358208685046a11C85e8ad32895DED33A249",
            "name": "Aave Arbitrum WBTC",
            "releases": [SULU],
            "symbol": "aArbWBTC",
            "type": "aave-v3",
            "underlying": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xd0C7101eACbB49F3deCcCc166d238410D6D46d57",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x8437d7C167dFB82ED4Cb79CD44B7a32A1dd95c77",
            "name": "Aave Arbitrum weETH",
            "releases": [SULU],
            "symbol": "aArbweETH",
            "type": "aave-v3",
            "underlying": "0x35751007a407ca6FEFfE80b3cB397736D2cf4dbe",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xE141425bc1594b8039De6390db1cDaf4397EA22b",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x513c7E3a9c69cA3e22550eF58AC1C0088e918FFf",
            "name": "Aave Arbitrum wstETH",
            "releases": [SULU],
            "symbol": "aArbwstETH",
            "type": "aave-v3",
            "underlying": "0x5979D7b546E38E414F7E9822514be443A4800529",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xb523AE262D20A936BC152e6023996e46FDC2A95D",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 6,
            "id": "0x6ab707Aca953eDAeFBc4fD23bA73294241490620",
            "name": "Aave Arbitrum USDT",
            "releases": [SULU],
            "symbol": "aArbUSDT",
            "type": "aave-v3",
            "underlying": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x3f3f5dF88dC9F13eac63DF89EC16ef6e7E25DdE7",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x191c10Aa4AF7C30e871E70C95dB0E4eb77237530",
            "name": "Aave Arbitrum LINK",
            "releases": [SULU],
            "symbol": "aArbLINK",
            "type": "aave-v3",
            "underlying": "0xf97f4df75117a78c1A5a0DBb814Af92458539FB4",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xb7c8Fb1dB45007F98A68Da0588e1AA524C317f27",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x6533afac2E7BCCB20dca161449A13A32D391fb00",
            "name": "Aave Arbitrum ARB",
            "releases": [SULU],
            "symbol": "aArbARB",
            "type": "aave-v3",
            "underlying": "0x912CE59144191C1204E64559FE8253a0e49E6548",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xb2A824043730FE05F3DA2efaFa1CBbe83fa548D6",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0x625E7708f30cA75bfd92586e17077590C60eb4cD",
            "name": "Aave Arbitrum USDC",
            "releases": [SULU],
            "symbol": "aArbUSDC",
            "type": "aave-v3",
            "underlying": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x50834F3163758fcC1Df9973b6e91f0F0F0434aD3",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x82E64f49Ed5EC1bC6e43DAD4FC8Af9bb3A2312EE",
            "name": "Aave Arbitrum DAI",
            "releases": [SULU],
            "symbol": "aArbDAI",
            "type": "aave-v3",
            "underlying": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xc5C8E77B397E531B8EC06BFb0048328B30E9eCfB",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x8Eb270e296023E9D92081fdF967dDd7878724424",
            "name": "Aave Arbitrum rETH",
            "releases": [SULU],
            "symbol": "aArbrETH",
            "type": "aave-v3",
            "underlying": "0xEC70Dcb4A1EFa46b8F2D97C310C9c4790ba5ffA8",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xD6aB2298946840262FcC278fF31516D39fF611eF",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x8ffDf2DE812095b1D19CB146E4c004587C0A0692",
            "name": "Aave Arbitrum LUSD",
            "releases": [SULU],
            "symbol": "aArbLUSD",
            "type": "aave-v3",
            "underlying": "0x93b346b6BC2548dA6A1E7d98E9a421B42541425b",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x0411D28c94d85A36bC72Cb0f875dfA8371D8fFfF",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xf329e36C7bF6E5E86ce2150875a84Ce77f477375",
            "name": "Aave Arbitrum AAVE",
            "releases": [SULU],
            "symbol": "aArbAAVE",
            "type": "aave-v3",
            "underlying": "0xba5DdD1f9d7F570dc94a51479a000E3BCE967196",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xaD1d5344AaDE45F43E596773Bcc4c423EAbdD034",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xeBe517846d0F36eCEd99C735cbF6131e1fEB775D",
            "name": "Aave Arbitrum GHO",
            "releases": [SULU],
            "symbol": "aArbGHO",
            "type": "aave-v3",
            "underlying": "0x7dfF72693f6A4149b17e7C6314655f6A9F7c8B33",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x3c786e934F23375Ca345C9b8D5aD54838796E8e7",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x38d693cE1dF5AaDF7bC62595A37D667aD57922e5",
            "name": "Aave Arbitrum FRAX",
            "releases": [SULU],
            "symbol": "aArbFRAX",
            "type": "aave-v3",
            "underlying": "0x17FC002b466eEc40DaE837Fc4bE5c67993ddBd6F",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x0809E3d38d1B4214958faf06D8b1B1a2b73f2ab8",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0xe80772Eaf6e2E18B651F160Bc9158b2A5caFCA65",
            "name": "xUSD",
            "releases": [SULU],
            "symbol": "xUSD",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x6548a81E640C000150e06AB413fB3F772682e9c5",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 6,
            "id": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
            "name": "USD Coin (Arb1)",
            "releases": [SULU],
            "symbol": "USDC",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x50834F3163758fcC1Df9973b6e91f0F0F0434aD3",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x17FC002b466eEc40DaE837Fc4bE5c67993ddBd6F",
            "name": "Frax",
            "releases": [SULU],
            "symbol": "FRAX",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x0809E3d38d1B4214958faf06D8b1B1a2b73f2ab8",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34",
            "name": "USDe",
            "releases": [SULU],
            "symbol": "USDe",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x88AC7Bca36567525A866138F03a6F6844868E0Bc",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x211Cc4DD073734dA055fbF44a2b4667d5E5fE5d2",
            "name": "Staked USDe",
            "releases": [SULU],
            "symbol": "sUSDe",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xf2215b9c35b1697B5f47e407c917a40D055E68d7",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0xf7d4e7273E5015C96728A6b02f31C505eE184603",
            "name": "Staked ETH",
            "releases": [SULU],
            "symbol": "osETH",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xB4102D5E72c402D537C9f024F4bd9c3709FE200d",
                "rate_asset": RateAsset.ETH,
            },
        },
        {
            "decimals": 18,
            "id": "0x93b346b6BC2548dA6A1E7d98E9a421B42541425b",
            "name": "LUSD Stablecoin",
            "releases": [SULU],
            "symbol": "LUSD",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x0411D28c94d85A36bC72Cb0f875dfA8371D8fFfF",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 18,
            "id": "0x7dfF72693f6A4149b17e7C6314655f6A9F7c8B33",
            "name": "Gho Token",
            "releases": [SULU],
            "symbol": "GHO",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0x3c786e934F23375Ca345C9b8D5aD54838796E8e7",
                "rate_asset": RateAsset.USD,
            },
        },
        {
            "decimals": 8,
            "id": "0x050C24dBf1eEc17babE5fc585F06116A259CC77A",
            "name": "iBTC",
            "releases": [SULU],
            "symbol": "IBTC",
            "type": "primitive",
            "price_feed": {
                "type": "PRIMITIVE_CHAINLINK",
                "aggregator": "0xd0C7101eACbB49F3deCcCc166d238410D6D46d57",
                "rate_asset": RateAsset.USD,
                "pegged_to": "WBTC",
                "non_standard": True,
            },
        },
        {
            "decimals": 6,
            "id": "0xA1b91fe9FD52141Ff8cac388Ce3F10BFDc1dE79d",
            "name": "dogwifhat",
            "releases": [],
            "symbol": "$WIF",
            "type": "primitive",
            "price_feed": {
                "type": "NONE",
            },
        },
        {
            "decimals": 18,
            "id": "0x25d887Ce7a35172C62FeBFD67a1856F20FaEbB00",
            "name": "Pepe",
            "releases": [],
            "symbol": "PEPE",
            "type": "primitive",
            "price_feed": {
                "type": "NONE",
            },
        },
    ],
)
