from ..assets_lib.arbitrum import ASSETS
from ..networks import NETWORK_BY_SLUG


DEPLOYMENT = {
    "address": "0x8da28441a4c594fD2fac72726C1412d8Cf9E4A19",
    "assets": ASSETS,
    "external_contracts": {
        "aaveUIIncentiveDataProvider": "0xE92cd6164CE7DC68e740765BC1f2a091B6CBc3e4",
        "aaveV2IncentivesController": "0x0000000000000000000000000000000000000000",
        "aaveV2LendingPoolProvider": "0x0000000000000000000000000000000000000000",
        "aaveV3LendingPoolProvider": "0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb",
        "aaveV3ProtocolDataProvider": "0x7F23D86Ee20D869112572136221e173428DD740B",
        "aaveV3RewardsController": "0x929EC64c34a17401F460460D4B9390518E5B473e",
        "aliceOrderManager": "0x0000000000000000000000000000000000000000",
        "arrakisV2Helper": "0x0000000000000000000000000000000000000000",
        "arrakisV2Resolver": "0x0000000000000000000000000000000000000000",
        "balancerGaugeController": "0x0000000000000000000000000000000000000000",
        "balancerHelpers": "0x0000000000000000000000000000000000000000",
        "balancerMinter": "0x0000000000000000000000000000000000000000",
        "balancerProtocolFeesCollector": "0x0000000000000000000000000000000000000000",
        "balancerVault": "0xBA12222222228d8Ba445958a75a0704d566BF2C8",
        "chainlinkFeedsRegistry": "0x0000000000000000000000000000000000000000",
        "compoundComptroller": "0x0000000000000000000000000000000000000000",
        "compoundV3Rewards": "0x0000000000000000000000000000000000000000",
        "curveChildLiquidityGaugeFactory": "0x0000000000000000000000000000000000000000",
        "curveMinter": "0x0000000000000000000000000000000000000000",
        "curveRegistry": "0x0000000000000000000000000000000000000000",
        "cvxCrvStaking": "0x0000000000000000000000000000000000000000",
        "gmxV2ExchangeRouter": "0x900173A66dbD345006C51fA35fA3aB760FcD843b",
        "gmxV2ChainlinkPriceFeed": "0x527FB0bCfF63C47761039bB386cFE181A92a4701",
        "gmxV2DataStore": "0xFD70de6b91282D8017aA4E741e9Ae325CAb992d8",
        "gmxV2Reader": "0x0537C767cDAC0726c76Bb89e92904fe28fd02fE1",
        "gmxV2ReferralStorage": "0xe6fab3F0c7199b0d34d7FbE83394fc0e0D06e99d",
        "kilnStaking": "0x0000000000000000000000000000000000000000",
        "lidoWithdrawalsQueue": "0x0000000000000000000000000000000000000000",
        "liquityCollSurplusPool": "0x0000000000000000000000000000000000000000",
        "liquityHintHelpers": "0x0000000000000000000000000000000000000000",
        "liquitySortedTroves": "0x0000000000000000000000000000000000000000",
        "liquityTroveManager": "0x0000000000000000000000000000000000000000",
        "makerMCDPotAddress": "0x0000000000000000000000000000000000000000",
        "morphoBlue": "0x0000000000000000000000000000000000000000",
        "multicall": "0xcA11bde05977b3631167028862bE2a173976CA11",
        "paraswapV5AugustusSwapper": "0xDEF171Fe48CF0115B1d80b88dc8eAB59176FEe57",
        "paraswapV5TokenTransferProxy": "0x216B4B4Ba9F3e719726886d34a177484278Bfcae",
        "pendlePtLpOracle": "0x0000000000000000000000000000000000000000",
        "staderStakingPoolManager": "0x0000000000000000000000000000000000000000",
        "staderUserWithdrawManager": "0x0000000000000000000000000000000000000000",
        "stakeWiseV3KeeperRewards": "0x0000000000000000000000000000000000000000",
        "theGraphDelegationStakingProxy": "0x00669A4CF01450B64E8A2A20E9b1FCB71E61eF03",
        "theGraphEpochManagerProxy": "0x5A843145c43d328B9bB7a4401d94918f131bB281",
        "uniswapV3NonFungiblePositionManager": "0xC36442b4a4522E871399CD717aBDD847Ab11FE88",
        "voteLockedConvexToken": "0x0000000000000000000000000000000000000000",
        "votiumVoteProxy": "0x0000000000000000000000000000000000000000",
        "zeroExExchangeProxy": "0x0000000000000000000000000000000000000000",
        "zeroExV4Exchange": "0x0000000000000000000000000000000000000000",
    },
    "inception": 230330283,
    "kind": "live",
    "known_address_lists": {
        "no_slippage_adapters": 1,
        "adapters": 2,
        "fees": 3,
        "policies": 4,
        "non_standard_price_feed_assets": 16,
        "a_tokens": 8,
    },
    "known_uint_lists": {},
    "label": "Arbitrum",
    "named_tokens": {
        "bal": "0x040d1EdC9569d4Bab2D15287Dc5A4F10F56a56B8",
        "comp": "0x354A6dA3fcde098F8389cad84b0182725c6C91dE",
        "crv": "0x11cDb42B0EB46D95f990BeDD4695A6e3fA034978",
        "cvx": "0xaAFcFD42c9954C6689ef1901e03db742520829c5",
        "dai": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
        "grt": "0x9623063377AD1B27544C965cCd7342f7EA7e88C7",
        "mln": "0x8f5c1A99b1df736Ad685006Cb6ADCA7B7Ae4b514",
        "usdt": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "weth": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    },
    "network": NETWORK_BY_SLUG["arbitrum"],
    "releases": {
        "sulu": {
            "address": "0xa2B4c827dE13D4e9801eA1Ca837524a1A148Dec3",
            "contracts": {
                "AaveDebtPositionLib": "0x0000000000000000000000000000000000000000",
                "AaveDebtPositionParser": "0x0000000000000000000000000000000000000000",
                "AavePriceFeed": "0x0000000000000000000000000000000000000000",
                "AaveV2Adapter": "0x0000000000000000000000000000000000000000",
                "AaveV2ATokenListOwner": "0x0000000000000000000000000000000000000000",
                "AaveV3Adapter": "0xD0c6B9801FC1E70945f11b3F93340dCc7507FD7C",
                "AaveV3ATokenListOwner": "0x575af64231a91B3A954D5E45A57187aCE6549C81",
                "AaveV3DebtPositionLib": "0x6ef082e4041030dCA3AE728a6D60d137404bDA35",
                "AaveV3DebtPositionParser": "0xA4Fc3FA736B812eE086C75c442D568A2Cd48cd59",
                "AaveV3FlashLoanAssetManagerFactory": "0xB49f8c0ce9DF900E024dAB48952bB8a8992C1795",
                "AaveV3FlashLoanAssetManagerLib": "0xd38C8c77B250d80e743013c4019d02f6Cc85B80E",
                "AddressListRegistry": "0x2C6bef68DAbf0494bB5F727E63c8FB54f7D2c287",
                "AlicePositionLib": "0x0000000000000000000000000000000000000000",
                "AlicePositionParser": "0x0000000000000000000000000000000000000000",
                "AllowedAdapterIncomingAssetsPolicy": "0x54325c3DC5ad60305a70Bc565bE7a9Ce71224A76",
                "AllowedAdaptersPerManagerPolicy": "0xeb036c294E54CC5047AB526C204752d056cc1952",
                "AllowedAdaptersPolicy": "0x1768B813d17F82A8d70Bd8b80a8c8C1562878337",
                "AllowedAssetsForRedemptionPolicy": "0x166aDA85f6A398BA01d2B97022770Cc6bD9D2Ea2",
                "AllowedDepositRecipientsPolicy": "0xdE0c43B8cB1CacDEc773EF55FCbFBcbe009891F1",
                "AllowedExternalPositionTypesPerManagerPolicy": "0x38673BACe2ae5e90d4936D0d90b58a3577795205",
                "AllowedExternalPositionTypesPolicy": "0x3c441B696bD451D0bA95eBb73Cf1B23c20873e14",
                "AllowedRedeemersForSpecificAssetsPolicy": "0x19AbBa4aB3134c64abdd17a9073d1Ec83663f036",
                "AllowedSharesTransferRecipientsPolicy": "0xB5ef1f5e549Ad46603bec9011b99A96a6CFD993E",
                "ArbitraryLoanPositionLib": "0x0000000000000000000000000000000000000000",
                "ArbitraryLoanPositionParser": "0x0000000000000000000000000000000000000000",
                "ArbitraryLoanTotalNominalDeltaOracleModule": "0x0000000000000000000000000000000000000000",
                "ArrakisV2Adapter": "0x0000000000000000000000000000000000000000",
                "ArrakisV2PriceFeed": "0x0000000000000000000000000000000000000000",
                "AssetValueCalculator": "0x12CcCb314e67d3Ed7178f0601B2F4c72fB9FEE6E",
                "BalancerV2GaugeTokenPriceFeed": "0x80F0fc50d672158d118e5EE1E64a6905a5E72540",
                "BalancerV2LiquidityAdapter": "0xB3ea1f2f3d2cdbD81A3DE91fdf9A2f3E3ACd66C1",
                "BalancerV2StablePoolPriceFeed": "0x8f30c0483C1cd32c100462F1Af6D4Ae6283086A9",
                "BalancerV2WeightedPoolPriceFeed": "0xA95878965F3af1d88002e06AE25182A45943B9e2",
                "ChainlinkLikeWstethPriceFeed": "0x0000000000000000000000000000000000000000",
                "ChainlinkLikeYnEthPriceFeed": "0x0000000000000000000000000000000000000000",
                "CompoundAdapter": "0x0000000000000000000000000000000000000000",
                "CompoundDebtPositionLib": "0x0000000000000000000000000000000000000000",
                "CompoundDebtPositionParser": "0x0000000000000000000000000000000000000000",
                "CompoundPriceFeed": "0x0000000000000000000000000000000000000000",
                "CompoundV3TokenListOwner": "0x0000000000000000000000000000000000000000",
                "CompoundV3Adapter": "0x0000000000000000000000000000000000000000",
                "ComptrollerLib": "0x3868C0FC34B6ecE124c6ab122f6f29E978Be6661",
                "ConvexVotingPositionLib": "0x0000000000000000000000000000000000000000",
                "ConvexVotingPositionParser": "0x0000000000000000000000000000000000000000",
                "CumulativeSlippageTolerancePolicy": "0x487f6a8a93C2be5A296eAD2C3fBC3fCeEd4AC599",
                "CurveExchangeAdapter": "0x0000000000000000000000000000000000000000",
                "CurveLiquidityAaveAdapter": "0x0000000000000000000000000000000000000000",
                "CurveLiquidityAdapter": "0x0000000000000000000000000000000000000000",
                "CurveLiquiditySethAdapter": "0x0000000000000000000000000000000000000000",
                "CurveLiquidityStethAdapter": "0x0000000000000000000000000000000000000000",
                "CurvePriceFeed": "0x0000000000000000000000000000000000000000",
                "DepositWrapper": "0x41d82E0512D77508AD486d6800059f3d936910db",
                "DisallowedAdapterIncomingAssetsPolicy": "0x5c9348fBEdb75c39f0E84396618ACCAb6c01F847",
                "Dispatcher": "0x8da28441a4c594fD2fac72726C1412d8Cf9E4A19",
                "EntranceRateBurnFee": "0x6180B98d85AfBd904016C7eA08eb41cba77A1c08",
                "EntranceRateDirectFee": "0xbd35b273453eB3a977f2757F92b20e8C0b33c0B2",
                "ERC4626Adapter": "0x0000000000000000000000000000000000000000",
                "ERC4626PriceFeed": "0x0000000000000000000000000000000000000000",
                "EtherFiEthPriceFeed": "0x0000000000000000000000000000000000000000",
                "ExitRateBurnFee": "0x8bDB929F16C2Ce833C3c3176ba5C607E20949010",
                "ExitRateDirectFee": "0x769C732a17f6e72D7BA0Fe79Ad01a31B27bbCB3d",
                "ExternalPositionFactory": "0xD44256aCea2193D4A50a9Ad879a531666729962c",
                "ExternalPositionManager": "0x90B53aefdbD2Ba3573d965d2D98951F2aA00507d",
                "FeeManager": "0x2C46503D4a0313c7161a5593B6865BaA194b466f",
                "FiduPriceFeed": "0x0000000000000000000000000000000000000000",
                "FundDataProviderRouter": "0xbD154eed58A880FE4c0129491539751FC2BbBFE1",
                "FundDeployer": "0xa2B4c827dE13D4e9801eA1Ca837524a1A148Dec3",
                "FundValueCalculator": "0xEA609eeB38D1EE8E8719597d47Cc9276df9f8707",
                "FundValueCalculatorRouter": "0x2e58f80cea88F0787CAdf1bB30acC23d8Ac81982",
                "GasRelayPaymasterFactory": "0xe922362AA3426bd683B63a8e5d13903A9cFC4Cbb",
                "GasRelayPaymasterLib": "0x9ab4E80bfB2D6Ad0B52Fa22e8Fe3d9FD3846bBB4",
                "GatedRedemptionQueueSharesWrapperFactory": "0x0000000000000000000000000000000000000000",
                "GatedRedemptionQueueSharesWrapperLib": "0x0000000000000000000000000000000000000000",
                "GenericAdapter": "0x0000000000000000000000000000000000000000",
                "GlobalConfigLib": "0x211E54a2f1E83cABc9D1211A1Df0759B7193201A",
                "GlobalConfigProxy": "0xf9315B421904eADF2f8FCe776958c147Ee9bC880",
                "GMXV2LeverageTradingPositionLib": "0x64e4a778f82A49738714E390Ae97f17434fd2156",
                "GMXV2LeverageTradingPositionParser": "0x0645B362A0D43E005F46713D1857e193F665810E",
                "IntegrationManager": "0x55dF97AcA98c2a708721f28eA1Ca42A2bE7FF934",
                "KilnStakingPositionLib": "0x0000000000000000000000000000000000000000",
                "KilnStakingPositionParser": "0x0000000000000000000000000000000000000000",
                "LidoWithdrawalsPositionLib": "0x0000000000000000000000000000000000000000",
                "LidoWithdrawalsPositionParser": "0x0000000000000000000000000000000000000000",
                "LiquityDebtPositionLib": "0x0000000000000000000000000000000000000000",
                "LiquityDebtPositionParser": "0x0000000000000000000000000000000000000000",
                "ManagementFee": "0xD2Fa8f6706241Dfdf8069D05E1D6f6C4A439aa86",
                "ManualValueOracleFactory": "0x671ed11497E8fE5c98eD45e699639Cf081EE0A5F",
                "MapleLiquidityPositionLib": "0x0000000000000000000000000000000000000000",
                "MapleLiquidityPositionParser": "0x0000000000000000000000000000000000000000",
                "MinAssetBalancesPostRedemptionPolicy": "0x53a124c9201F0d00470Cd4245946d2bBB98210BA",
                "MinMaxInvestmentPolicy": "0x542812a43334634213877fbfdE33eCbEF5234c9d",
                "MinSharesSupplyFee": "0xa8c3B04A800c08AE010b56AC1C1Ad7033D980B0F",
                "MorphoBluePositionLib": "0x0000000000000000000000000000000000000000",
                "MorphoBluePositionParser": "0x0000000000000000000000000000000000000000",
                "NoDepegOnRedeemSharesForSpecificAssetsPolicy": "0xaD404CEAbAD39D4b22BF2e1265A161aC44620825",
                "NotionalV2PositionLib": "0x0000000000000000000000000000000000000000",
                "NotionalV2PositionParser": "0x0000000000000000000000000000000000000000",
                "OneInchV5Adapter": "0xC2f737AeECE89D8db98a7D82BFEd40D09e381Ed5",
                "OnlyRemoveDustExternalPositionPolicy": "0xE4453105Be9E579896A3ed73df9A1e285c8C95c2",
                "OnlyUntrackDustOrPricelessAssetsPolicy": "0xA482f4Ab637Cd5Ca00084d511B3cA9aa8d8f475E",
                "ParaSwapV5Adapter": "0x08dF49F617eCdCcbC90d9A0f87B8C1a84B2e7cb9",
                "PeggedDerivativesPriceFeed": "0x0000000000000000000000000000000000000000",
                "PerformanceFee": "0x9E0F80bc5a688e93D6c57efcFdD4564f70975e8b",
                "PendleV2Adapter": "0x0000000000000000000000000000000000000000",
                "PendleV2PositionLib": "0x0000000000000000000000000000000000000000",
                "PendleV2PositionParser": "0x0000000000000000000000000000000000000000",
                "PendleMarketsRegistry": "0x0000000000000000000000000000000000000000",
                "PolicyManager": "0xbDe1E8C4A061cd28F4871860dDf22200B85ee9Ec",
                "PoolTogetherV4Adapter": "0x0000000000000000000000000000000000000000",
                "PoolTogetherV4PriceFeed": "0x0000000000000000000000000000000000000000",
                "ProtocolFeeReserveLib": "0x642986a6BC5EC518Cfb97d8AFa5A7Fa8477d3Cf5",
                "ProtocolFeeReserveProxy": "0x9Eb802e7696C9951fdCbA90699e5000D7A39205c",
                "ProtocolFeeTracker": "0xE71227D6D846e0fb3367D020683327031c4c4A3D",
                "SharePriceThrottledAssetManagerFactory": "0x0000000000000000000000000000000000000000",
                "SharePriceThrottledAssetManagerLib": "0x0000000000000000000000000000000000000000",
                "SharesSplitterFactory": "0x0000000000000000000000000000000000000000",
                "SingleAssetRedemptionQueueFactory": "0x0000000000000000000000000000000000000000",
                "SingleAssetRedemptionQueueLib": "0x0000000000000000000000000000000000000000",
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
                "TheGraphDelegationPositionLib": "0x92dA9DF390D3e9199D105289B297ECA357Ecc9b7",
                "TheGraphDelegationPositionParser": "0xc2822Eca13A7760141041a173C1b9B13e22515f6",
                "ThreeOneThirdAdapter": "0x5a1c0E89133C4Cd844A8B345370565f1368A79A8",
                "TransferAssetsAdapter": "0xE8Db4924569A3C61aaDfb721bBb009e3127196bD",
                "UintListRegistry": "0xC438E48F5D2F99eb4a2b9865F8cccfC9915f227A",
                "UniswapV2ExchangeAdapter": "0x0000000000000000000000000000000000000000",
                "UniswapV2LiquidityAdapter": "0x0000000000000000000000000000000000000000",
                "UniswapV2PoolPriceFeed": "0x0000000000000000000000000000000000000000",
                "UniswapV3Adapter": "0xeA0F3Cc847c8e388bD2f7AdAC130B64b6754f5e2",
                "UniswapV3LiquidityPositionLib": "0x250530dB7ee6a10e0126288ACE48a7bB54bd4ADc",
                "UniswapV3LiquidityPositionParser": "0xc6ecE1bff7a7B16DEF7E2a6956b7C75189240671",
                "UnpermissionedActionsWrapper": "0x6aaB72Ede0255f3dD0e1cE568248A63AA3df2320",
                "UsdEthSimulatedAggregator": "0x0000000000000000000000000000000000000000",
                "ValueInterpreter": "0xDd5F18a52A63eCECF502A165A459D33BE5C0a06C",
                "VaultLib": "0xE1A147b3FB8a7bE78bf3A061F176bC718D897695",
                "WstethPriceFeed": "0x0000000000000000000000000000000000000000",
                "YearnVaultV2Adapter": "0x0000000000000000000000000000000000000000",
                "YearnVaultV2PriceFeed": "0x0000000000000000000000000000000000000000",
                "ZeroExV2Adapter": "0x0000000000000000000000000000000000000000",
                "ZeroExV4Adapter": "0x0000000000000000000000000000000000000000",
                "ZeroExV4AdapterPmm2Kyc": "0x0000000000000000000000000000000000000000",
            },
            "inception": 230330283,
            "network": NETWORK_BY_SLUG["arbitrum"],
            "slug": "arbitrum.sulu",
            "status": "live",
            "version": "sulu",
        },
    },
    "slug": "arbitrum",
    "subgraphs": {
        "assets": {
            "slug": "asset-universe-arbitrum",
            "id": "J2DQQxBCL5qxzwickTR2YKxVH5Bnr3aUwYdVEYbaYbrJ",
        },
        "balances": {
            "slug": "vault-balances-arbitrum",
            "id": "F6uEWkrjChyqzfA3wdwRTKCBdzQYm9LPCFbaVj3tvudN",
        },
        "core": {
            "slug": "enzyme-core-arbitrum",
            "id": "8UJ5Bkf2eazZhXsAshhzQ2Keibcb8NFHBvXis9pb2C2Y",
            "dev_version": "version/latest",
        },
        "shares": {
            "slug": "vault-shares-arbitrum",
            "id": "8pUZ51EFRYiMMdL5JLdjzYRjG5yqA2zv1KiMRHdrz9EH",
        },
        "vaults": {
            "slug": "vault-lineage-arbitrum",
            "id": "ErvkSrie41cprdwYAnLz7PAN44ZjJoqrLm14SyPvhbHa",
        },
    },
}
