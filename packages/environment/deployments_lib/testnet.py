from ..assets_lib.polygon import ASSETS
from ..networks import NETWORK_BY_SLUG
from .polygon import DEPLOYMENT as POLYGON

DEPLOYMENT = {
    "address": "0xD77231f355c6790441C1fb95A2e2Ef916d5B3d84",
    "assets": ASSETS,
    "external_contracts": POLYGON["external_contracts"],
    "inception": 25731749,
    "kind": "test",
    "known_address_lists": {
        "no_slippage_adapters": 1,
        "adapters": 2,
        "fees": 3,
        "policies": 4,
        "non_standard_price_feed_assets": 128,
        "a_tokens": 115,
        "deposit_wrapper_allowed_exchanges": 125,
    },
    "known_uint_lists": {},
    "label": "Testnet",
    "named_tokens": POLYGON["named_tokens"],
    "network": NETWORK_BY_SLUG["polygon"],
    "releases": {
        "sulu": {
            "address": "0x4bc71568feB39E38734DB97113752a4e5657D319",
            "contracts": {
                "AaveDebtPositionLib": "0xb9eA765ED3443712f238520B0384C4Beb4aeB8C2",
                "AaveDebtPositionParser": "0x1191aD9888e895Bc543E97B40ad6748F86A11A89",
                "AavePriceFeed": "0xce08ed41e04BBD5906aCaa3773F9bA03fA34146F",
                "AaveV2Adapter": "0x0000000000000000000000000000000000000000",
                "AaveV2ATokenListOwner": "0x0000000000000000000000000000000000000000",
                "AaveV3Adapter": "0xD20F64252F984FA8560eCB5619CB86412178d336",
                "AaveV3ATokenListOwner": "0x0000000000000000000000000000000000000000",
                "AaveV3DebtPositionLib": "0x42ab51B812eF040bBf7c42EebE8108b89921Ae0F",
                "AaveV3DebtPositionParser": "0xfb80EAecc49EAE3afceF2F8687988D8f1904637e",
                "AaveV3FlashLoanAssetManagerFactory": "0x0000000000000000000000000000000000000000",
                "AaveV3FlashLoanAssetManagerLib": "0x0000000000000000000000000000000000000000",
                "AddressListRegistry": "0x477a4E56EABC94a871744d4F1d59e045fD53C1Ef",
                "AlicePositionLib": "0x0000000000000000000000000000000000000000",
                "AlicePositionParser": "0x0000000000000000000000000000000000000000",
                "AllowedAdapterIncomingAssetsPolicy": "0x390bE32D5864fDA0295D0E5F413d411EAbD7c4CE",
                "AllowedAdaptersPerManagerPolicy": "0xd63909B856ab759AFF30eb52651e366d2625d1DE",
                "AllowedAdaptersPolicy": "0x35CF5A1Fe0254F863c9f6C0cd5C2128EE61bAF58",
                "AllowedAssetsForRedemptionPolicy": "0x2be12155dfbe1bB92F314d0b9759bb127FEBDe65",
                "AllowedDepositRecipientsPolicy": "0x7656970e350E79CE550DD3051d4014373371Df53",
                "AllowedExternalPositionTypesPerManagerPolicy": "0x3291B7c08B2AC90d547e4CeF11103f770f14b390",
                "AllowedExternalPositionTypesPolicy": "0x2cb6b222E17167629F75DE39dD13C0ba6D58f0Cf",
                "AllowedRedeemersForSpecificAssetsPolicy": "0xB4343AC6c53cBa47aEF22470c351F92e89bF7170",
                "AllowedSharesTransferRecipientsPolicy": "0x0aCfeb85b8Dc2DB3AA34F93151B7A494B84a99Bc",
                "ArbitraryLoanPositionLib": "0x8f3f038581E7e03518C078D964674B23b590F521",
                "ArbitraryLoanPositionParser": "0xdD8C63313b9F0A8618A6cf557636C1E6c787a9FD",
                "ArbitraryLoanTotalNominalDeltaOracleModule": "0xb0c636423757684f3Ac92688274928B226A07eED",
                "ArrakisV2Adapter": "0x1F4658D8D09a73a74cAb97725A0144fcaC47ce57",
                "ArrakisV2PriceFeed": "0x86A7eCf8328dEdc954714042ae67E50Fb3Bb3822",
                "AssetValueCalculator": "0xbdFD3Bb2C61Aa0ea087d80F574166bec21fE3744",
                "BalancerV2GaugeTokenPriceFeed": "0x7915090595c4321EA6F8ACFfB1bC0EeDdDA15Ba3",
                "BalancerV2LiquidityAdapter": "0x8FFe411488c2d2C55AcbEa7D1FEAb7BeB5881605",
                "BalancerV2StablePoolPriceFeed": "0xbBD3Cc67C7F90f3FA546C62d13db59e3fD11eb36",
                "BalancerV2WeightedPoolPriceFeed": "0xfD63783414032e146842e191d2568329A91B3aAe",
                "ChainlinkLikeWstethPriceFeed": "0x0000000000000000000000000000000000000000",
                "ChainlinkLikeYnEthPriceFeed": "0x0000000000000000000000000000000000000000",
                "CompoundAdapter": "0x0000000000000000000000000000000000000000",
                "CompoundDebtPositionLib": "0x0000000000000000000000000000000000000000",
                "CompoundDebtPositionParser": "0x0000000000000000000000000000000000000000",
                "CompoundPriceFeed": "0x0000000000000000000000000000000000000000",
                "CompoundV3TokenListOwner": "0xCa64C1D5e337f18e9d270225aA5004Be5a8E570C",
                "CompoundV3Adapter": "0xaA1Cb33F9659FF7cb1876EBA57EE6Ae5Ea053e99",
                "ComptrollerLib": "0x1c3279E12F94943Bf3021029CBCd0287B4c89135",
                "ConvertedQuoteAggregatorFactory": "0x0000000000000000000000000000000000000000",
                "ConvexVotingPositionLib": "0x0000000000000000000000000000000000000000",
                "ConvexVotingPositionParser": "0x0000000000000000000000000000000000000000",
                "CumulativeSlippageTolerancePolicy": "0x561176cd43B958482d33DcD62A1EB437Bd7BFeF9",
                "CurveExchangeAdapter": "0x174CBC353607C2Ec9d8829d26e9E1ED7bf7dE2e9",
                "CurveLiquidityAaveAdapter": "0x0000000000000000000000000000000000000000",
                "CurveLiquidityAdapter": "0x278C870e693A06bF55eB518A5546D615AF0e0FF3",
                "CurveLiquiditySethAdapter": "0x0000000000000000000000000000000000000000",
                "CurveLiquidityStethAdapter": "0x0000000000000000000000000000000000000000",
                "CurvePriceFeed": "0x5876B6044D8Aea8a5e59E4feB00d50F9c8B0c8F2",
                "DepositWrapper": "0x0043bD9b82095724Ec613136083E093436dC0649",
                "DisallowedAdapterIncomingAssetsPolicy": "0xb496D3453A07801248D7B4339e09546ac13EB141",
                "Dispatcher": "0xD77231f355c6790441C1fb95A2e2Ef916d5B3d84",
                "EntranceRateBurnFee": "0x722E252E5140A46530CC3F4534EB1561851B8B57",
                "EntranceRateDirectFee": "0xc1755FB4b9157186AECf0775C4f6C3a0dD0Ea7af",
                "ERC4626Adapter": "0x0000000000000000000000000000000000000000",
                "ERC4626PriceFeed": "0x0000000000000000000000000000000000000000",
                "EtherFiEthPriceFeed": "0x0000000000000000000000000000000000000000",
                "ExitRateBurnFee": "0x00dED19F9F8E512Dc8041F5B52B20d53eBDb69F8",
                "ExitRateDirectFee": "0xAEd3e269898DE65715f71D88F7Dcb7986d3f31b0",
                "ExternalPositionFactory": "0x30ca263F9A3780c70530FFaF0ccC162AE3eba993",
                "ExternalPositionManager": "0x370826fa91762609964723962187efBA705c1F17",
                "FeeManager": "0x22D1c7AABd397B4715Afa64FF89bC225650787bA",
                "FiduPriceFeed": "0x0000000000000000000000000000000000000000",
                "FundDataProviderRouter": "0xAD2eE0Cd4820f62Cd78121a22C582C56804740D9",
                "FundDeployer": "0x4bc71568feB39E38734DB97113752a4e5657D319",
                "FundValueCalculator": "0x36D55C3c1C57a88EfdA07dF425d10fF267F3f9d1",
                "FundValueCalculatorRouter": "0xb9c46d50d25808014B9371a91f44e602EcDa7f0F",
                "GasRelayPaymasterFactory": "0xeDabD8516499B4C0141057B19acCa9d1df055323",
                "GasRelayPaymasterLib": "0x900851aEcffBB7440745724a8e37C7a7Ae67DDf2",
                "GatedRedemptionQueueSharesWrapperFactory": "0xd188Ab263828d0bECE1442dA7DEe7e0AE76F709C",
                "GatedRedemptionQueueSharesWrapperLib": "0x33D092CF2859989d6dc52EAb8ab7962b5486eaB5",
                "GenericAdapter": "0xD8d52AfEf3e073F6378b89885A1B15E36e1fB5e5",
                "GlobalConfigLib": "0xA2669671B9de8acb4032F5E40D0240E4599E7a2D",
                "GlobalConfigProxy": "0x864371e0Ea7543e0b76f847A29f48DC77416F09B",
                "GMXV2LeverageTradingPositionLib": "0x0000000000000000000000000000000000000000",
                "GMXV2LeverageTradingPositionParser": "0x0000000000000000000000000000000000000000",
                "IntegrationManager": "0xAD31aaeFFd50430b80386263aEb477B9e607b0D1",
                "KilnStakingPositionLib": "0x0000000000000000000000000000000000000000",
                "KilnStakingPositionParser": "0x0000000000000000000000000000000000000000",
                "LidoWithdrawalsPositionLib": "0x0000000000000000000000000000000000000000",
                "LidoWithdrawalsPositionParser": "0x0000000000000000000000000000000000000000",
                "LiquityDebtPositionLib": "0x0000000000000000000000000000000000000000",
                "LiquityDebtPositionParser": "0x0000000000000000000000000000000000000000",
                "ManagementFee": "0x4a95185896aDCe31a8cDfAaA2832DecC3d20Dc2C",
                "ManualValueOracleFactory": "0x0b7fA18e37e9bD2e156Cac8467D164261f5119Cc",
                "MapleLiquidityPositionLib": "0x0000000000000000000000000000000000000000",
                "MapleLiquidityPositionParser": "0x0000000000000000000000000000000000000000",
                "MinAssetBalancesPostRedemptionPolicy": "0x7800955AAE98C31e4EaC22C1b4e7eDd6aD0c3ba0",
                "MinMaxInvestmentPolicy": "0xd2dBB1d5222200b94f4aEa2618D88cC33146987B",
                "MinSharesSupplyFee": "0x8A2cfB231be7c229209DC41E62def7756a6088A2",
                "MorphoBluePositionLib": "0x0000000000000000000000000000000000000000",
                "MorphoBluePositionParser": "0x0000000000000000000000000000000000000000",
                "NoDepegOnRedeemSharesForSpecificAssetsPolicy": "0x91cf2e3A615428f1f14fa3240b8dD52A2bDae649",
                "NotionalV2PositionLib": "0x0000000000000000000000000000000000000000",
                "NotionalV2PositionParser": "0x0000000000000000000000000000000000000000",
                "OneInchV5Adapter": "0xb474bD1b1f2fA3A0C0a815D63839d065aF98Fb12",
                "OnlyRemoveDustExternalPositionPolicy": "0x713E7DaC3C237b71dd54a8718Ce21Ecd5D2Dc747",
                "OnlyUntrackDustOrPricelessAssetsPolicy": "0xC1F7b231874E2f9B2c9d4ec701dC6F046Eab253a",
                "ParaSwapV5Adapter": "0xb663C344ce8f66f906dd1BB7F1E269ed352DeEA9",
                "PeggedDerivativesPriceFeed": "0xAD80a1C732E3e3b979c64e1df6815F739D3317f7",
                "PerformanceFee": "0xF1FcBa510713355D7504B87A163420A2bD116a4B",
                "PendleV2Adapter": "0x0000000000000000000000000000000000000000",
                "PendleV2PositionLib": "0x0000000000000000000000000000000000000000",
                "PendleV2PositionParser": "0x0000000000000000000000000000000000000000",
                "PendleMarketsRegistry": "0x0000000000000000000000000000000000000000",
                "PolicyManager": "0xbEc6C9E0F2Aa62413144B37095fAf60656B26007",
                "PoolTogetherV4Adapter": "0x0Ed3e9C0A16cFafdC4E06a07576302B39249116d",
                "PoolTogetherV4PriceFeed": "0x64B466b2630249A926D72BBB2d64B33bbbEc155D",
                "ProtocolFeeReserveLib": "0xD7aDa00E0d9d05436C9C271fdC7C9e398eD678dC",
                "ProtocolFeeReserveProxy": "0x9B3011a1152139555FB8A560e6582c3367DD93F7",
                "ProtocolFeeTracker": "0xA77585469F71499B0F2784c5151aAA919fdffFcA",
                "SharePriceThrottledAssetManagerFactory": "0x0000000000000000000000000000000000000000",
                "SharePriceThrottledAssetManagerLib": "0x0000000000000000000000000000000000000000",
                "SharesSplitterFactory": "0x7D3a58e675362dE47A4f79DD5451074F2ebc8459",
                "SingleAssetRedemptionQueueFactory": "0xAd1980b3301557Eae118275E79C2554cB6EfbD5A",
                "SingleAssetRedemptionQueueLib": "0x78c357627c65c336A64Abefa062a0b19ba6FA6F4",
                "SolvV2BondBuyerPositionLib": "0x0000000000000000000000000000000000000000",
                "SolvV2BondBuyerPositionParser": "0x0000000000000000000000000000000000000000",
                "SolvV2BondIssuerPositionLib": "0x0000000000000000000000000000000000000000",
                "SolvV2BondIssuerPositionParser": "0x0000000000000000000000000000000000000000",
                "StaderSDPriceFeed": "0x0000000000000000000000000000000000000000",
                "StaderStakingAdapter": "0x0000000000000000000000000000000000000000",
                "StaderWithdrawalsPositionLib": "0x0000000000000000000000000000000000000000",
                "StaderWithdrawalsPositionParser": "0x0000000000000000000000000000000000000000",
                "StakeWiseV3StakingPositionLib": "0x0000000000000000000000000000000000000000",
                "StakeWiseV3StakingPositionParser": "0x0000000000000000000000000000000000000000",
                "SwellStakingAdapter": "0x0000000000000000000000000000000000000000",
                "SynthetixAdapter": "0x0000000000000000000000000000000000000000",
                "TermFinanceV1LendingPositionLib": "0x0000000000000000000000000000000000000000",
                "TermFinanceV1LendingPositionParser": "0x0000000000000000000000000000000000000000",
                "TheGraphDelegationPositionLib": "0x0000000000000000000000000000000000000000",
                "TheGraphDelegationPositionParser": "0x0000000000000000000000000000000000000000",
                "ThreeOneThirdAdapter": "0x0c4dc97e6c0D94327F3ca1873aE5868F5D0A6f05",
                "TransferAssetsAdapter": "0x0000000000000000000000000000000000000000",
                "UintListRegistry": "0xe296EA33a38108580dcae364239Fb0C50c53591B",
                "UniswapV2ExchangeAdapter": "0x0000000000000000000000000000000000000000",
                "UniswapV2LiquidityAdapter": "0x0000000000000000000000000000000000000000",
                "UniswapV2PoolPriceFeed": "0x0000000000000000000000000000000000000000",
                "UniswapV3Adapter": "0x502631CfCa0261F57243eF07a03aed6815Ddb88d",
                "UniswapV3LiquidityPositionLib": "0x64a498AeDA1fe6447082e58eb54cdb784e075c8b",
                "UniswapV3LiquidityPositionParser": "0x70cdbb90cc3Babd05D02Ce649D18d8902d9A28D5",
                "UnpermissionedActionsWrapper": "0xB9a1A15357Ba60CC1A0Ab4C6D4B46F4f40e9D4bc",
                "UsdEthSimulatedAggregator": "0x51e75b5E0eef2d40B4D70C5dAa2666E1eA30F0Bd",
                "ValueInterpreter": "0x0777062308749e88113BBfB1317f434f40dbb2d8",
                "VaultLib": "0xD785Cf317dad803eF4FBDA3A95b41F965770dBA6",
                "WstethPriceFeed": "0x0000000000000000000000000000000000000000",
                "YearnVaultV2Adapter": "0x0000000000000000000000000000000000000000",
                "YearnVaultV2PriceFeed": "0x0000000000000000000000000000000000000000",
                "ZeroExV2Adapter": "0x0000000000000000000000000000000000000000",
                "ZeroExV4Adapter": "0x72595b87975b57b518891b9090d97583678011A4",
                "ZeroExV4AdapterPmm2Kyc": "0x0000000000000000000000000000000000000000",
                "ZeroLendLRTBTCAaveV3Adapter": "0x0000000000000000000000000000000000000000",
                "ZeroLendLRTBTCAaveV3ATokenListOwner": "0x0000000000000000000000000000000000000000",
                "ZeroLendLRTBTCAaveV3DebtPositionLib": "0x0000000000000000000000000000000000000000",
                "ZeroLendLRTBTCAaveV3DebtPositionParser": "0x0000000000000000000000000000000000000000",
                "ZeroLendRWAStablecoinsAaveV3Adapter": "0x0000000000000000000000000000000000000000",
                "ZeroLendRWAStablecoinsAaveV3ATokenListOwner": "0x0000000000000000000000000000000000000000",
                "ZeroLendRWAStablecoinsAaveV3DebtPositionLib": "0x0000000000000000000000000000000000000000",
                "ZeroLendRWAStablecoinsAaveV3DebtPositionParser": "0x0000000000000000000000000000000000000000",
            },
            "inception": 25731946,
            "network": NETWORK_BY_SLUG["polygon"],
            "slug": "testnet.sulu",
            "status": "live",
            "version": "sulu",
        },
    },
    "slug": "testnet",
    "subgraphs": {
        "assets": {
            "slug": "asset-universe-testnet",
            "id": "H7KYtV4eVas2Py83UE1596DPkQNRRNGiPqSbN1AbKMaX",
        },
        "balances": {
            "slug": "vault-balances-testnet",
            "id": "86aJM6X5DB5vrCVapuFWufVKPBtVYmxygzxsLctRhc3r",
        },
        "core": {
            "slug": "enzyme-core-testnet",
            "id": "98iFcdDw1g5akWxbTFqcs2TsUaJhVDNxPTgH8P2WBUao",
            "dev_version": "version/latest",
        },
        "shares": {
            "slug": "vault-shares-testnet",
            "id": "EPZTMtyWpwckXczAry12HddRpssBjKjtrhWB1ZGK9bLt",
        },
        "vaults": {
            "slug": "vault-lineage-testnet",
            "id": "BPhRz8C6rUcb3PXWpWFYCH2zjudLg76HjAeDtcNEWCNV",
        },
    },
}
