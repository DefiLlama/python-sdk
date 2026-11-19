"""ETF type definitions."""

from typing import Dict, TypedDict, Literal


class EtfSnapshotItem(TypedDict):
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


class EtfFlowItem(TypedDict):
    gecko_id: str
    day: str
    total_flow_usd: float


FdvPeriod = Literal["7", "30", "ytd", "365"]


FdvPerformanceItem = Dict[str, float]


__all__ = [
    "EtfSnapshotItem",
    "EtfFlowItem",
    "FdvPeriod",
    "FdvPerformanceItem",
]
