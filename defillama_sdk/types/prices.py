"""Price type definitions."""

from typing import Dict, List, Optional, TypedDict


class CoinPrice(TypedDict, total=False):
    decimals: Optional[int]
    symbol: str
    price: float
    timestamp: int
    confidence: Optional[float]


class CoinPricesResponse(TypedDict):
    coins: Dict[str, CoinPrice]


class BatchHistoricalPricePoint(TypedDict, total=False):
    timestamp: int
    price: float
    confidence: Optional[float]


class BatchHistoricalCoinData(TypedDict, total=False):
    prices: List[BatchHistoricalPricePoint]
    symbol: Optional[str]
    decimals: Optional[int]
    confidence: Optional[float]


class BatchHistoricalResponse(TypedDict):
    coins: Dict[str, BatchHistoricalCoinData]


class ChartPricePoint(TypedDict):
    timestamp: int
    price: float


class CoinChartData(TypedDict, total=False):
    prices: List[ChartPricePoint]
    symbol: str
    confidence: Optional[float]
    decimals: Optional[int]


class ChartResponse(TypedDict):
    coins: Dict[str, CoinChartData]


class PercentageResponse(TypedDict):
    coins: Dict[str, float]


class FirstPriceData(TypedDict):
    price: float
    timestamp: int
    symbol: str


class FirstPriceResponse(TypedDict):
    coins: Dict[str, FirstPriceData]


class BlockInfo(TypedDict):
    height: int
    timestamp: int


class ChartOptions(TypedDict, total=False):
    start: Optional[int]
    end: Optional[int]
    span: Optional[int]
    period: Optional[str]
    searchWidth: Optional[str]


class PercentageOptions(TypedDict, total=False):
    timestamp: Optional[int]
    lookForward: Optional[bool]
    period: Optional[str]


__all__ = [
    "CoinPrice",
    "CoinPricesResponse",
    "BatchHistoricalPricePoint",
    "BatchHistoricalCoinData",
    "BatchHistoricalResponse",
    "ChartPricePoint",
    "CoinChartData",
    "ChartResponse",
    "PercentageResponse",
    "FirstPriceData",
    "FirstPriceResponse",
    "BlockInfo",
    "ChartOptions",
    "PercentageOptions",
]
