"""ETF type definitions."""

from typing import Dict, TypedDict, Literal


class EtfOverviewItem(TypedDict):
    ticker: str
    timestamp: int
    asset: str
    issuer: str
    etf_name: str
    custodian: str
    pct_fee: float
    url: str
    flows: float
    aum: float
    volume: float


class EtfHistoryItem(TypedDict):
    gecko_id: str
    day: str
    total_flow_usd: float


FdvPeriod = Literal["7", "30", "ytd", "365"]


FdvPerformanceItem = Dict[str, float]


__all__ = [
    "EtfOverviewItem",
    "EtfHistoryItem",
    "FdvPeriod",
    "FdvPerformanceItem",
]
