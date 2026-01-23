"""Yield type definitions."""

from typing import List, Optional, TypedDict


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
        "pool_old": str,
        "timestamp": str,
        "url": str,
        "return": Optional[float],
        "apyMeanExpanding": Optional[float],
        "apyStdExpanding": Optional[float],
        "project_factorized": int,
        "chain_factorized": int,
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
]
