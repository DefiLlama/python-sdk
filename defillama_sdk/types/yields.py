"""Yield type definitions."""

from typing import List, Literal, Optional, TypedDict, Union


class YieldPoolPredictions(TypedDict, total=False):
    predictedClass: Optional[str]
    predictedProbability: Optional[float]
    binnedConfidence: Optional[float]


class YieldPool(TypedDict, total=False):
    pool: str
    chain: str
    project: str
    symbol: str
    tvlUsd: float
    apy: Optional[float]
    apyBase: Optional[float]
    apyReward: Optional[float]
    rewardTokens: Optional[List[str]]
    underlyingTokens: Optional[List[str]]
    poolMeta: Optional[str]
    exposure: Optional[str]
    il7d: Optional[float]
    apyBase7d: Optional[float]
    apyPct1D: Optional[float]
    apyPct7D: Optional[float]
    apyPct30D: Optional[float]
    stablecoin: bool
    ilRisk: Optional[str]
    predictions: Optional[YieldPoolPredictions]
    mu: Optional[float]
    sigma: Optional[float]
    count: Optional[float]
    outlier: Optional[bool]
    volumeUsd1d: Optional[float]
    volumeUsd7d: Optional[float]
    apyMean30d: Optional[float]
    apyBaseInception: Optional[float]


class YieldPoolsResponse(TypedDict):
    status: str
    data: List[YieldPool]


YieldPoolOld = TypedDict(
    "YieldPoolOld",
    {
        **YieldPool.__annotations__,
        # Legacy pool identifier (v2 `pool_key`)
        "pool_old": str,
        # Pool receipt/LP token address
        "poolTokenAddress": Optional[str],
        "timestamp": str,
        "url": str,
        "return": Optional[float],
        "apyMeanExpanding": Optional[float],
        "apyStdExpanding": Optional[float],
        # Factorized project identifier (always null on the /yields/v1 compatibility route)
        "project_factorized": Optional[int],
        # Factorized chain identifier (always null on the /yields/v1 compatibility route)
        "chain_factorized": Optional[int],
    },
    total=False,
)


class YieldPoolsOldResponse(TypedDict):
    status: str
    data: List[YieldPoolOld]


class YieldChartDataPoint(TypedDict, total=False):
    timestamp: str
    tvlUsd: float
    apy: Optional[float]
    apyBase: Optional[float]
    apyReward: Optional[float]
    il7d: Optional[float]
    apyBase7d: Optional[float]
    # Price per share of the pool token
    pricePerShare: Optional[float]


class YieldChartResponse(TypedDict):
    status: str
    data: List[YieldChartDataPoint]


class BorrowPool(YieldPool, total=False):
    apyBaseBorrow: Optional[float]
    apyRewardBorrow: Optional[float]
    totalSupplyUsd: Optional[float]
    totalBorrowUsd: Optional[float]
    debtCeilingUsd: Optional[float]
    ltv: Optional[float]
    borrowable: Optional[bool]
    mintedCoin: Optional[str]
    borrowFactor: Optional[float]


class BorrowPoolsResponse(TypedDict):
    status: str
    data: List[BorrowPool]


class LendBorrowChartDataPoint(TypedDict, total=False):
    timestamp: str
    totalSupplyUsd: Optional[float]
    totalBorrowUsd: Optional[float]
    debtCeilingUsd: Optional[float]
    apyBase: Optional[float]
    apyBaseBorrow: Optional[float]
    apyReward: Optional[float]
    apyRewardBorrow: Optional[float]


class LendBorrowChartResponse(TypedDict):
    status: str
    data: List[LendBorrowChartDataPoint]


class PerpPool(TypedDict, total=False):
    perp_id: str
    timestamp: str
    marketplace: str
    market: str
    baseAsset: str
    fundingRate: Optional[float]
    fundingRatePrevious: Optional[float]
    fundingTimePrevious: Optional[int]
    openInterest: Optional[float]
    indexPrice: Optional[float]
    fundingRate7dAverage: Optional[float]
    fundingRate7dSum: Optional[float]
    fundingRate30dAverage: Optional[float]
    fundingRate30dSum: Optional[float]


class PerpsResponse(TypedDict):
    """Response from the /api/perpFundingRates endpoint (formerly /yields/perps)."""

    status: str
    data: List[PerpPool]


class LsdRate(TypedDict, total=False):
    name: str
    symbol: str
    address: str
    type: Optional[str]
    expectedRate: Optional[float]
    marketRate: Optional[float]
    ethPeg: Optional[float]
    fee: Optional[float]


LsdRatesResponse = List[LsdRate]


# ---------------------------------------------------------------------------
# Yields v2 (/yields/v2/*)
#
# Changes from v1:
# - No project slug: `protocol` is a display name (e.g. "Aave V3"); `chain` is a display name as in v1.
# - Lending `tvl_usd` is total supplied (v1 `tvlUsd` was supplied minus borrowed).
# - APY is nested: `apy.current|avg_7d|avg_30d.{base,reward,total}`;
#   `reward` is positive or null, never 0.
# - Tokens are objects (`{ address, symbol, decimals }`), not address strings.
# - `/earn` only lists pools with at least $10K supplied.
# ---------------------------------------------------------------------------

# History window for v2 history routes. The server defaults to `"max"`.
YieldHistoryRange = Literal["30d", "90d", "max"]


class YieldToken(TypedDict, total=False):
    """Token reference used across v2 responses."""

    address: str
    symbol: Optional[str]
    decimals: Optional[int]


class YieldPoolToken(TypedDict, total=False):
    """Receipt/LP token of a pool."""

    address: str
    symbol: Optional[str]
    name: Optional[str]


class YieldDisplay(TypedDict, total=False):
    """Human-readable pool label and detail (e.g. fee tier, market name)."""

    label: Optional[str]
    detail: Optional[str]


class YieldApy(TypedDict, total=False):
    """APY components in percent. `reward` is positive or null, never 0."""

    base: Optional[float]
    reward: Optional[float]
    total: Optional[float]


class YieldApyWindows(TypedDict, total=False):
    """APY over the current sample and trailing 7d/30d averages."""

    current: YieldApy
    avg_7d: YieldApy
    avg_30d: YieldApy


class YieldApyHistoryWindows(TypedDict, total=False):
    """APY over trailing 1d/7d/30d averages, as used by history points."""

    avg_1d: YieldApy
    avg_7d: YieldApy
    avg_30d: YieldApy


class YieldIntrinsicApy(TypedDict, total=False):
    """Intrinsic (underlying token) APY, e.g. stETH staking yield inside a lending pool."""

    base: Optional[float]


class YieldIntrinsicApyHistoryWindows(TypedDict, total=False):
    avg_1d: YieldIntrinsicApy
    avg_7d: YieldIntrinsicApy
    avg_30d: YieldIntrinsicApy


class YieldIntrinsicHistory(TypedDict, total=False):
    """Intrinsic APY on a history point."""

    apy: YieldIntrinsicApyHistoryWindows


class YieldIntrinsicApyWindows(TypedDict, total=False):
    current: YieldIntrinsicApy
    avg_7d: YieldIntrinsicApy
    avg_30d: YieldIntrinsicApy


class YieldIntrinsicSourcePool(TypedDict, total=False):
    id: str
    pool_token: Optional[str]
    symbol: Optional[str]


class YieldIntrinsic(TypedDict, total=False):
    """Intrinsic APY plus the pool it is sourced from."""

    apy: YieldIntrinsicApyWindows
    source_pool: YieldIntrinsicSourcePool


class YieldStability(TypedDict, total=False):
    """30-day APY stability score in 0..1 (1 / (1 + coefficient of variation)), per APY composition."""

    base: Optional[float]
    base_reward: Optional[float]
    base_intrinsic: Optional[float]
    base_reward_intrinsic: Optional[float]


class YieldAvailableHistory(TypedDict, total=False):
    """Which history series exist for a pool."""

    supply: bool
    borrow: bool


class EarnPoolAttributes(TypedDict, total=False):
    stablecoin_only: bool
    single_asset_exposure: bool
    impermanent_loss_risk: bool


class EarnPoolHolders(TypedDict, total=False):
    count: Optional[int]
    avg_position_usd: Optional[float]
    top_10_share_pct: Optional[float]


# EarnPool without `holders`, shared with EarnPoolDetail (TS `Omit<EarnPool, "holders">`):
# a TypedDict subclass can't narrow an inherited key's type.
class _EarnPoolFields(TypedDict, total=False):
    # Pool UUID (same id as v1 `pool`)
    id: str
    # Stable adapter key (v1 `pool_old`)
    pool_key: str
    pool_token: Optional[YieldPoolToken]
    display: YieldDisplay
    reference_asset_symbol: Optional[str]
    url: Optional[str]
    # Protocol display name, e.g. "Aave V3" (v1 `project` was the slug "aave-v3")
    protocol: str
    # Chain display name, e.g. "Ethereum"
    chain: str
    underlying_tokens: List[YieldToken]
    reward_tokens: List[YieldToken]
    # TVL in USD. For lending pools this is total supplied (v1 subtracted borrows).
    tvl_usd: Optional[float]
    apy: YieldApyWindows
    intrinsic: Optional[YieldIntrinsic]
    stability_30d: YieldStability
    price_per_share: Optional[float]
    volume_1d_usd: Optional[float]
    attributes: EarnPoolAttributes
    # Room left under the supply cap in USD; null = uncapped, 0 = at/over cap
    available_supply_usd: Optional[float]


class EarnPool(_EarnPoolFields, total=False):
    """An earn pool from `/yields/v2/earn`. Replaces `YieldPool`.

    Changes from v1: `protocol` is a display name (no project slug); lending
    `tvl_usd` is total supplied; APY is nested under `apy.current|avg_7d|avg_30d`;
    tokens are objects; only pools with at least $10K supplied are listed.
    """

    holders: EarnPoolHolders


YieldHolderMovementStatus = Literal["up", "down", "steady", "entered_top_10", "unknown"]


class YieldHolderShareChange(TypedDict, total=False):
    status: YieldHolderMovementStatus
    pct_point_delta: Optional[float]


class YieldHolderBalanceChange(TypedDict, total=False):
    status: YieldHolderMovementStatus
    pct_delta: Optional[float]


class YieldHolderChange(TypedDict, total=False):
    """A top-10 holder's share and balance movement over a window."""

    share: YieldHolderShareChange
    balance: YieldHolderBalanceChange


class YieldTopHolder(TypedDict, total=False):
    rank: int
    address: str
    # Raw token balance as a decimal string (scale by `decimals`)
    balance: Optional[str]
    share_pct: Optional[float]
    change_7d: YieldHolderChange
    change_30d: YieldHolderChange


class EarnPoolTopHolders(TypedDict, total=False):
    decimals: Optional[int]
    holders: List[YieldTopHolder]


class EarnPoolDetailHolders(EarnPoolHolders, total=False):
    """Holder data on the pool detail route."""

    count_change_7d: Optional[int]
    count_change_30d: Optional[int]
    top_10_holders: Optional[EarnPoolTopHolders]


class EarnPoolDetail(_EarnPoolFields, total=False):
    """A single earn pool from `/yields/v2/earn/{id}`: an `EarnPool` plus holder detail."""

    holders: EarnPoolDetailHolders
    available_history: YieldAvailableHistory


class EarnHistoryPoint(TypedDict, total=False):
    """Daily earn pool history point. Replaces `YieldChartDataPoint`."""

    # YYYY-MM-DD
    date: str
    tvl_usd: Optional[float]
    apy: YieldApyHistoryWindows
    intrinsic: Optional[YieldIntrinsicHistory]
    price_per_share: Optional[float]


class EarnQueryParams(TypedDict, total=False):
    """Filters for `/yields/v2/earn/query`. Keys match the server's query params.

    `chain` and `protocol` are slugs (e.g. "ethereum", "aave-v3"; case-insensitive),
    up to 20 values each. Responses carry display names, not slugs.
    """

    chain: Union[str, List[str]]
    protocol: Union[str, List[str]]
    stablecoin: bool
    single_asset_exposure: bool
    impermanent_loss_risk: bool
    # Minimum TVL in USD (>= 0)
    min_tvl: float
    # 1-based page number
    page: int
    # Page size, 1-300 (default 100)
    limit: int


class EarnResponse(TypedDict, total=False):
    """Response from `/yields/v2/earn`. Replaces `YieldPoolsResponse`."""

    # Newest sample time in the snapshot (ISO), when rows carry one
    as_of: str
    data: List[EarnPool]


class EarnQueryPagination(TypedDict, total=False):
    total: int
    page: int
    limit: int


class EarnQueryResponse(TypedDict):
    """Response from `/yields/v2/earn/query`. Rows sorted by TVL descending."""

    data: List[EarnPool]
    pagination: EarnQueryPagination


class EarnPoolResponse(TypedDict):
    """Response from `/yields/v2/earn/{id}`."""

    data: EarnPoolDetail


class EarnHistoryResponse(TypedDict):
    """Response from `/yields/v2/earn/{id}/history`. Replaces `YieldChartResponse`."""

    data: List[EarnHistoryPoint]


class BorrowMarketIntrinsic(TypedDict, total=False):
    supply: Optional[YieldIntrinsic]
    borrow: Optional[YieldIntrinsic]


class BorrowMarket(TypedDict, total=False):
    """A borrow market from `/yields/v2/borrow/markets`. Replaces `BorrowPool`.

    Changes from v1: `protocol` is a display name; supply and borrow APY are nested
    windows (`supply_apy`, `borrow_cost_apy`); tokens are objects.
    """

    # Pool UUID (same id as v1 `pool`)
    id: str
    pool_key: str
    pool_token: Optional[YieldPoolToken]
    display: YieldDisplay
    url: Optional[str]
    # Protocol display name
    protocol: str
    # Chain display name
    chain: str
    collateral_token: Optional[YieldToken]
    borrow_token: Optional[YieldToken]
    reward_tokens: List[YieldToken]
    loan_to_value: Optional[float]
    total_supply_usd: Optional[float]
    total_borrow_usd: Optional[float]
    available_borrow_usd: Optional[float]
    supply_apy: YieldApyWindows
    # Borrow cost; `reward` is the incentive that reduces it
    borrow_cost_apy: YieldApyWindows
    intrinsic: BorrowMarketIntrinsic


class BorrowMarketDetail(BorrowMarket, total=False):
    """A single borrow market from `/yields/v2/borrow/markets/{id}`."""

    available_history: YieldAvailableHistory


class BorrowMarketHistoryPoint(TypedDict, total=False):
    """Daily borrow market history point.

    Together with `EarnHistoryPoint` (supply side) this replaces `LendBorrowChartDataPoint`.
    """

    # YYYY-MM-DD
    date: str
    total_borrow_usd: Optional[float]
    available_borrow_usd: Optional[float]
    borrow_cost_apy: YieldApyHistoryWindows
    intrinsic: Optional[YieldIntrinsicHistory]


class BorrowMarketsResponse(TypedDict, total=False):
    """Response from `/yields/v2/borrow/markets`. Replaces `BorrowPoolsResponse`."""

    # Newest sample time in the snapshot (ISO), when rows carry one
    as_of: str
    data: List[BorrowMarket]


class BorrowMarketResponse(TypedDict):
    """Response from `/yields/v2/borrow/markets/{id}`."""

    data: BorrowMarketDetail


class BorrowMarketHistoryResponse(TypedDict):
    """Response from `/yields/v2/borrow/markets/{id}/history`."""

    data: List[BorrowMarketHistoryPoint]


__all__ = [
    "YieldPoolPredictions",
    "YieldPool",
    "YieldPoolsResponse",
    "YieldPoolOld",
    "YieldPoolsOldResponse",
    "YieldChartDataPoint",
    "YieldChartResponse",
    "BorrowPool",
    "BorrowPoolsResponse",
    "LendBorrowChartDataPoint",
    "LendBorrowChartResponse",
    "PerpPool",
    "PerpsResponse",
    "LsdRate",
    "LsdRatesResponse",
    "YieldHistoryRange",
    "YieldToken",
    "YieldPoolToken",
    "YieldDisplay",
    "YieldApy",
    "YieldApyWindows",
    "YieldApyHistoryWindows",
    "YieldIntrinsicApy",
    "YieldIntrinsicApyHistoryWindows",
    "YieldIntrinsicHistory",
    "YieldIntrinsicApyWindows",
    "YieldIntrinsicSourcePool",
    "YieldIntrinsic",
    "YieldStability",
    "YieldAvailableHistory",
    "EarnPoolAttributes",
    "EarnPoolHolders",
    "EarnPool",
    "YieldHolderMovementStatus",
    "YieldHolderShareChange",
    "YieldHolderBalanceChange",
    "YieldHolderChange",
    "YieldTopHolder",
    "EarnPoolTopHolders",
    "EarnPoolDetailHolders",
    "EarnPoolDetail",
    "EarnHistoryPoint",
    "EarnQueryParams",
    "EarnResponse",
    "EarnQueryPagination",
    "EarnQueryResponse",
    "EarnPoolResponse",
    "EarnHistoryResponse",
    "BorrowMarketIntrinsic",
    "BorrowMarket",
    "BorrowMarketDetail",
    "BorrowMarketHistoryPoint",
    "BorrowMarketsResponse",
    "BorrowMarketResponse",
    "BorrowMarketHistoryResponse",
]
