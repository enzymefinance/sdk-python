import asyncio
from decimal import Decimal
from eth_abi import encode, decode
from web3.types import ChecksumAddress, HexStr
from typing import Tuple
from ..._internal import integration_manager
from ..._internal import external_position_manager
from ...utils.clients import PublicClient
from ...utils.conversion import from_wei
from ... import Asset

# --------------------------------------------------------------------------------------------
# LEND
# --------------------------------------------------------------------------------------------

LEND_ENCODING = [
    {
        "type": "address",
        "name": "aToken",
    },
    {
        "type": "uint256",
        "name": "depositAmount",
    },
]


def lend_encode(a_token: ChecksumAddress, deposit_amount: int) -> HexStr:
    types = [e["type"] for e in LEND_ENCODING]
    values = [a_token, deposit_amount]
    return encode(types, values)


def lend_decode(encoded: HexStr) -> Tuple[ChecksumAddress, int]:
    """
    Returns:
        (a_token, deposit_amount)
    """
    types = [e["type"] for e in LEND_ENCODING]
    return decode(types, encoded)


lend = integration_manager.make_use(integration_manager.SELECTOR["lend"], lend_encode)


# --------------------------------------------------------------------------------------------
# REDEEM
# --------------------------------------------------------------------------------------------

REDEEM_ENCODING = [
    {
        "type": "address",
        "name": "aToken",
    },
    {
        "type": "uint256",
        "name": "redeemAmount",
    },
]


def redeem_encode(a_token: ChecksumAddress, redeem_amount: int) -> HexStr:
    types = [e["type"] for e in REDEEM_ENCODING]
    values = [a_token, redeem_amount]
    return encode(types, values)


def redeem_decode(encoded: HexStr) -> Tuple[ChecksumAddress, int]:
    """
    Returns:
        (a_token, redeem_amount)
    """
    types = [e["type"] for e in REDEEM_ENCODING]
    return decode(types, encoded)


redeem = integration_manager.make_use(
    integration_manager.SELECTOR["redeem"], redeem_encode
)


# --------------------------------------------------------------------------------------------
# EXTERNAL POSITION
# --------------------------------------------------------------------------------------------

ACTION = {
    "add_collateral": 0,
    "remove_collateral": 1,
    "borrow": 2,
    "repay_borrow": 3,
    "set_e_mode": 4,
    "set_use_reserve_as_collateral": 5,
    "claim_rewards": 6,
    "sweep": 7,
}

create = external_position_manager.create_only


# --------------------------------------------------------------------------------------------
# ADD COLLATERAL
# --------------------------------------------------------------------------------------------

ADD_COLLATERAL_ENCODING = [
    {
        "type": "address[]",
        "name": "aTokens",
    },
    {
        "type": "uint256[]",
        "name": "amounts",
    },
    {
        "type": "bool",
        "name": "fromUnderlying",
    },
]


def add_collateral_encode(
    a_tokens: list[ChecksumAddress], amounts: list[int], from_underlying: bool
) -> HexStr:
    types = [e["type"] for e in ADD_COLLATERAL_ENCODING]
    values = [a_tokens, amounts, from_underlying]
    return encode(types, values)


def add_collateral_decode(
    encoded: HexStr,
) -> Tuple[list[ChecksumAddress], list[int], bool]:
    """
    Returns:
        (a_tokens, amounts, from_underlying)
    """
    types = [e["type"] for e in ADD_COLLATERAL_ENCODING]
    return decode(types, encoded)


add_collateral = external_position_manager.make_use(
    ACTION["add_collateral"], add_collateral_encode
)
create_and_add_collateral = external_position_manager.make_create_and_use(
    ACTION["add_collateral"], add_collateral_encode
)


# --------------------------------------------------------------------------------------------
# REMOVE COLLATERAL
# --------------------------------------------------------------------------------------------

REMOVE_COLLATERAL_ENCODING = [
    {
        "type": "address[]",
        "name": "aTokens",
    },
    {
        "type": "uint256[]",
        "name": "amounts",
    },
    {
        "type": "bool",
        "name": "toUnderlying",
    },
]


def remove_collateral_encode(
    a_tokens: list[ChecksumAddress], amounts: list[int], to_underlying: bool
) -> HexStr:
    types = [e["type"] for e in REMOVE_COLLATERAL_ENCODING]
    values = [a_tokens, amounts, to_underlying]
    return encode(types, values)


def remove_collateral_decode(
    encoded: HexStr,
) -> Tuple[list[ChecksumAddress], list[int], bool]:
    """
    Returns:
        (a_tokens, amounts, to_underlying)
    """
    types = [e["type"] for e in REMOVE_COLLATERAL_ENCODING]
    return decode(types, encoded)


remove_collateral = external_position_manager.make_use(
    ACTION["remove_collateral"], remove_collateral_encode
)


# --------------------------------------------------------------------------------------------
# BORROW
# --------------------------------------------------------------------------------------------

BORROW_ENCODING = [
    {
        "type": "address[]",
        "name": "underlyingTokens",
    },
    {
        "type": "uint256[]",
        "name": "amounts",
    },
]


def borrow_encode(
    underlying_tokens: list[ChecksumAddress], amounts: list[int]
) -> HexStr:
    types = [e["type"] for e in BORROW_ENCODING]
    values = [underlying_tokens, amounts]
    return encode(types, values)


def borrow_decode(encoded: HexStr) -> Tuple[list[ChecksumAddress], list[int]]:
    """
    Returns:
        (underlying_tokens, amounts)
    """
    types = [e["type"] for e in BORROW_ENCODING]
    return decode(types, encoded)


borrow = external_position_manager.make_use(ACTION["borrow"], borrow_encode)
create_and_borrow = external_position_manager.make_create_and_use(
    ACTION["borrow"], borrow_encode
)


# --------------------------------------------------------------------------------------------
# REPAY BORROW
# --------------------------------------------------------------------------------------------

REPAY_BORROW_ENCODING = [
    {
        "type": "address[]",
        "name": "underlyingTokens",
    },
    {
        "type": "uint256[]",
        "name": "amounts",
    },
]


def repay_borrow_encode(
    underlying_tokens: list[ChecksumAddress], amounts: list[int]
) -> HexStr:
    types = [e["type"] for e in REPAY_BORROW_ENCODING]
    values = [underlying_tokens, amounts]
    return encode(types, values)


def repay_borrow_decode(encoded: HexStr) -> Tuple[list[ChecksumAddress], list[int]]:
    """
    Returns:
        (underlying_tokens, amounts)
    """
    types = [e["type"] for e in REPAY_BORROW_ENCODING]
    return decode(types, encoded)


repay_borrow = external_position_manager.make_use(
    ACTION["repay_borrow"], repay_borrow_encode
)


# --------------------------------------------------------------------------------------------
# SET E-MODE
# --------------------------------------------------------------------------------------------

SET_EMODE_ENCODING = [
    {
        "type": "uint8",
        "name": "categoryId",
    },
]


def set_e_mode_encode(category_id: int) -> HexStr:
    types = [e["type"] for e in SET_EMODE_ENCODING]
    values = [category_id]
    return encode(types, values)


def set_e_mode_decode(encoded: HexStr) -> int:
    """
    Returns:
        category_id
    """
    types = [e["type"] for e in SET_EMODE_ENCODING]
    decoded = decode(types, encoded)
    return decoded[0]


set_e_mode = external_position_manager.make_use(ACTION["set_e_mode"], set_e_mode_encode)

# --------------------------------------------------------------------------------------------
# SET USE RESERVE AS COLLATERAL
# --------------------------------------------------------------------------------------------

SET_USE_RESERVE_AS_COLLATERAL_ENCODING = [
    {
        "type": "address",
        "name": "underlying",
    },
    {
        "type": "bool",
        "name": "useAsCollateral",
    },
]


def set_use_reserve_as_collateral_encode(
    underlying: ChecksumAddress, use_as_collateral: bool
) -> HexStr:
    types = [e["type"] for e in SET_USE_RESERVE_AS_COLLATERAL_ENCODING]
    values = [underlying, use_as_collateral]
    return encode(types, values)


def set_use_reserve_as_collateral_decode(
    encoded: HexStr,
) -> Tuple[ChecksumAddress, bool]:
    """
    Returns:
        (underlying, use_as_collateral)
    """
    types = [e["type"] for e in SET_USE_RESERVE_AS_COLLATERAL_ENCODING]
    return decode(types, encoded)


set_use_reserve_as_collateral = external_position_manager.make_use(
    ACTION["set_use_reserve_as_collateral"], set_use_reserve_as_collateral_encode
)


# --------------------------------------------------------------------------------------------
# CLAIM REWARDS
# --------------------------------------------------------------------------------------------

CLAIM_REWARDS_ENCODING = [
    {
        "type": "address[]",
        "name": "assets",
    },
    {
        "type": "uint256",
        "name": "amount",
    },
    {
        "type": "address",
        "name": "rewardToken",
    },
]


def claim_rewards_encode(
    assets: list[ChecksumAddress], amount: int, reward_token: ChecksumAddress
) -> HexStr:
    types = [e["type"] for e in CLAIM_REWARDS_ENCODING]
    values = [assets, amount, reward_token]
    return encode(types, values)


def claim_rewards_decode(
    encoded: HexStr,
) -> Tuple[list[ChecksumAddress], int, ChecksumAddress]:
    """
    Returns:
        (assets, amount, reward_token)
    """
    types = [e["type"] for e in CLAIM_REWARDS_ENCODING]
    return decode(types, encoded)


claim_rewards = external_position_manager.make_use(
    ACTION["claim_rewards"], claim_rewards_encode
)


# --------------------------------------------------------------------------------------------
# SWEEP
# --------------------------------------------------------------------------------------------

SWEEP_ENCODING = [
    {
        "type": "address[]",
        "name": "assets",
    },
]


def sweep_encode(assets: list[ChecksumAddress]) -> HexStr:
    types = [e["type"] for e in SWEEP_ENCODING]
    values = [assets]
    return encode(types, values)


def sweep_decode(encoded: HexStr) -> list[ChecksumAddress]:
    """
    Returns:
        assets
    """
    types = [e["type"] for e in SWEEP_ENCODING]
    return decode(types, encoded)


sweep = external_position_manager.make_use(ACTION["sweep"], sweep_encode)

# --------------------------------------------------------------------------------------------
# THIRD PARTY READ FUNCTIONS
# --------------------------------------------------------------------------------------------


POOL_ADDRESS_PROVIDER_ABI = [
    {
        "inputs": [],
        "name": "getPool",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]


async def get_pool(
    client: PublicClient,
    pool_address_provider: ChecksumAddress,
) -> ChecksumAddress:
    contract = client.contract(pool_address_provider, POOL_ADDRESS_PROVIDER_ABI)
    return await contract.functions.getPool().call()


POOL_ABI = [
    {
        "inputs": [{"internalType": "uint8", "name": "id", "type": "uint8"}],
        "name": "getEModeCategoryData",
        "outputs": [
            {
                "components": [
                    {"internalType": "uint16", "name": "ltv", "type": "uint16"},
                    {
                        "internalType": "uint16",
                        "name": "liquidationThreshold",
                        "type": "uint16",
                    },
                    {
                        "internalType": "uint16",
                        "name": "liquidationBonus",
                        "type": "uint16",
                    },
                    {
                        "internalType": "address",
                        "name": "priceSource",
                        "type": "address",
                    },
                    {"internalType": "string", "name": "label", "type": "string"},
                ],
                "internalType": "struct DataTypes.EModeCategory",
                "name": "",
                "type": "tuple",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
        "name": "getUserAccountData",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "totalCollateralBase",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "totalDebtBase", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "availableBorrowsBase",
                "type": "uint256",
            },
            {
                "internalType": "uint256",
                "name": "currentLiquidationThreshold",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "ltv", "type": "uint256"},
            {"internalType": "uint256", "name": "healthFactor", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]


async def get_e_mode_category_data(
    client: PublicClient,
    pool: ChecksumAddress,
    category_id: int,
) -> Tuple[int, int, int, ChecksumAddress, str]:
    contract = client.contract(pool, POOL_ABI)
    return await contract.functions.getEModeCategoryData(category_id).call()


async def get_user_account_data(
    client: PublicClient,
    pool: ChecksumAddress,
    user: ChecksumAddress,
) -> Tuple[int, int, int, int, int, int]:
    contract = client.contract(pool, POOL_ABI)
    return await contract.functions.getUserAccountData(user).call()


REWARDS_CONTROLLER_ABI = [
    {
        "inputs": [
            {"internalType": "address[]", "name": "assets", "type": "address[]"},
            {"internalType": "address", "name": "user", "type": "address"},
        ],
        "name": "getAllUserRewards",
        "outputs": [
            {"internalType": "address[]", "name": "rewardsList", "type": "address[]"},
            {
                "internalType": "uint256[]",
                "name": "unclaimedAmounts",
                "type": "uint256[]",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
        "name": "getRewardsByAsset",
        "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "asset", "type": "address"},
            {"internalType": "address", "name": "reward", "type": "address"},
        ],
        "name": "getRewardsData",
        "outputs": [
            {"internalType": "uint256", "name": "index", "type": "uint256"},
            {"internalType": "uint256", "name": "emissionPerSecond", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "lastUpdateTimestamp",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "distributionEnd", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]


async def get_all_user_rewards(
    client: PublicClient,
    rewards_controller: ChecksumAddress,
    assets: list[ChecksumAddress],
    user: ChecksumAddress,
) -> Tuple[list[ChecksumAddress], list[int]]:
    contract = client.contract(rewards_controller, REWARDS_CONTROLLER_ABI)
    return await contract.functions.getAllUserRewards(assets, user).call()


async def get_rewards_by_asset(
    client: PublicClient,
    rewards_controller: ChecksumAddress,
    asset: ChecksumAddress,
) -> list[ChecksumAddress]:
    contract = client.contract(rewards_controller, REWARDS_CONTROLLER_ABI)
    return await contract.functions.getRewardsByAsset(asset).call()


async def get_rewards_data(
    client: PublicClient,
    rewards_controller: ChecksumAddress,
    asset: ChecksumAddress,
    reward: ChecksumAddress,
) -> Tuple[int, int, int, int]:
    contract = client.contract(rewards_controller, REWARDS_CONTROLLER_ABI)
    return await contract.functions.getRewardsData(asset, reward).call()


PROTOCOL_DATA_PROVIDER_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
        "name": "getReserveCaps",
        "outputs": [
            {"internalType": "uint256", "name": "borrowCap", "type": "uint256"},
            {"internalType": "uint256", "name": "supplyCap", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "asset", "type": "address"}],
        "name": "getReserveData",
        "outputs": [
            {"internalType": "uint256", "name": "unbacked", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "accruedToTreasuryScaled",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "totalAToken", "type": "uint256"},
            {"internalType": "uint256", "name": "totalStableDebt", "type": "uint256"},
            {"internalType": "uint256", "name": "totalVariableDebt", "type": "uint256"},
            {"internalType": "uint256", "name": "liquidityRate", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "variableBorrowRate",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "stableBorrowRate", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "averageStableBorrowRate",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "liquidityIndex", "type": "uint256"},
            {
                "internalType": "uint256",
                "name": "variableBorrowIndex",
                "type": "uint256",
            },
            {"internalType": "uint40", "name": "lastUpdateTimestamp", "type": "uint40"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]


async def get_reserve_caps(
    client: PublicClient,
    protocol_data_provider: ChecksumAddress,
    asset: ChecksumAddress,
) -> Tuple[Decimal, Decimal]:
    contract = client.contract(protocol_data_provider, PROTOCOL_DATA_PROVIDER_ABI)
    reserve_caps, decimals = await asyncio.gather(
        contract.functions.getReserveCaps(asset).call(),
        Asset.get_decimals(client, asset),
    )
    return (
        from_wei(reserve_caps[0], decimals),
        from_wei(reserve_caps[1], decimals),
    )


async def get_reserve_data(
    client: PublicClient,
    protocol_data_provider: ChecksumAddress,
    asset: ChecksumAddress,
) -> Tuple[int, int, int, int, int, int, int, int, int, int, int]:
    contract = client.contract(protocol_data_provider, PROTOCOL_DATA_PROVIDER_ABI)
    return await contract.functions.getReserveData(asset).call()


async def get_available_supply_amount(
    client: PublicClient,
    protocol_data_provider: ChecksumAddress,
    asset: ChecksumAddress,
    decimals: int,
) -> Decimal:
    reserve_caps, reserve_data = await asyncio.gather(
        get_reserve_caps(client, protocol_data_provider, asset),
        get_reserve_data(client, protocol_data_provider, asset),
    )
    return reserve_caps[1] - from_wei(reserve_data[2], decimals)


async def get_available_variable_debt_amount(
    client: PublicClient,
    protocol_data_provider: ChecksumAddress,
    asset: ChecksumAddress,
    decimals: int,
) -> Decimal:
    reserve_caps, reserve_data = await asyncio.gather(
        get_reserve_caps(client, protocol_data_provider, asset),
        get_reserve_data(client, protocol_data_provider, asset),
    )
    return reserve_caps[0] - from_wei(reserve_data[4], decimals)


UI_INCENTIVE_DATA_PROVIDER_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "provider", "type": "address"}],
        "name": "getReservesIncentivesData",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "underlyingAsset",
                        "type": "address",
                    },
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "tokenAddress",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "incentiveControllerAddress",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "string",
                                        "name": "rewardTokenSymbol",
                                        "type": "string",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "rewardTokenAddress",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "rewardOracleAddress",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "emissionPerSecond",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "incentivesLastUpdateTimestamp",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "tokenIncentivesIndex",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "emissionEndTimestamp",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "int256",
                                        "name": "rewardPriceFeed",
                                        "type": "int256",
                                    },
                                    {
                                        "internalType": "uint8",
                                        "name": "rewardTokenDecimals",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "uint8",
                                        "name": "precision",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "uint8",
                                        "name": "priceFeedDecimals",
                                        "type": "uint8",
                                    },
                                ],
                                "internalType": "struct IUiIncentiveDataProviderV3.RewardInfo[]",
                                "name": "rewardsTokenInformation",
                                "type": "tuple[]",
                            },
                        ],
                        "internalType": "struct IUiIncentiveDataProviderV3.IncentiveData",
                        "name": "aIncentiveData",
                        "type": "tuple",
                    },
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "tokenAddress",
                                "type": "address",
                            },
                            {
                                "internalType": "address",
                                "name": "incentiveControllerAddress",
                                "type": "address",
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "string",
                                        "name": "rewardTokenSymbol",
                                        "type": "string",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "rewardTokenAddress",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "address",
                                        "name": "rewardOracleAddress",
                                        "type": "address",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "emissionPerSecond",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "incentivesLastUpdateTimestamp",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "tokenIncentivesIndex",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "emissionEndTimestamp",
                                        "type": "uint256",
                                    },
                                    {
                                        "internalType": "int256",
                                        "name": "rewardPriceFeed",
                                        "type": "int256",
                                    },
                                    {
                                        "internalType": "uint8",
                                        "name": "rewardTokenDecimals",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "uint8",
                                        "name": "precision",
                                        "type": "uint8",
                                    },
                                    {
                                        "internalType": "uint8",
                                        "name": "priceFeedDecimals",
                                        "type": "uint8",
                                    },
                                ],
                                "internalType": "struct IUiIncentiveDataProviderV3.RewardInfo[]",
                                "name": "rewardsTokenInformation",
                                "type": "tuple[]",
                            },
                        ],
                        "internalType": "struct IUiIncentiveDataProviderV3.IncentiveData",
                        "name": "vIncentiveData",
                        "type": "tuple",
                    },
                ],
                "internalType": "struct IUiIncentiveDataProviderV3.AggregatedReserveIncentiveData[]",
                "name": "",
                "type": "tuple[]",
            },
        ],
        "stateMutability": "view",
        "type": "function",
    },
]


async def get_reserves_incentives_data(
    client: PublicClient,
    ui_incentive_data_provider: ChecksumAddress,
    pool_address_provider: ChecksumAddress,
):
    # TODO: unknown return type
    contract = client.contract(
        ui_incentive_data_provider, UI_INCENTIVE_DATA_PROVIDER_ABI
    )
    return await contract.functions.getReservesIncentivesData(
        pool_address_provider
    ).call()
