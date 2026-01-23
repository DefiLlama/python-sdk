"""Fees type definitions."""

from typing import Dict, List, Optional, Tuple, TypedDict

from ..constants.dimensions import FeeDataType


class FeesOverviewOptions(TypedDict, total=False):
    excludeTotalDataChart: Optional[bool]
    excludeTotalDataChartBreakdown: Optional[bool]
    dataType: Optional[FeeDataType]


class FeesSummaryOptions(TypedDict, total=False):
    dataType: Optional[FeeDataType]


class FeesChartOptions(TypedDict, total=False):
    dataType: Optional[FeeDataType]


class FeesProtocol(TypedDict, total=False):
    id: str
    defillamaId: str
    name: str
    displayName: str
    module: str
    category: str
    logo: str
    chains: List[str]
    protocolType: str
    methodologyURL: str
    methodology: Dict[str, str]
    total24h: Optional[float]
    total48hto24h: Optional[float]
    total7d: Optional[float]
    total14dto7d: Optional[float]
    total30d: Optional[float]
    total60dto30d: Optional[float]
    total1y: Optional[float]
    totalAllTime: Optional[float]
    total7DaysAgo: Optional[float]
    total30DaysAgo: Optional[float]
    average1y: Optional[float]
    monthlyAverage1y: Optional[float]
    change_30dover30d: Optional[float]
    breakdown24h: Optional[Dict[str, Dict[str, float]]]
    breakdown30d: Optional[Dict[str, Dict[str, float]]]
    parentProtocol: Optional[str]
    slug: str


class FeesOverviewResponse(TypedDict, total=False):
    totalDataChart: List[Tuple[int, float]]
    totalDataChartBreakdown: List["ChartBreakdownDataPoint"]
    breakdown24h: Optional[Dict[str, Dict[str, float]]]
    breakdown30d: Optional[Dict[str, Dict[str, float]]]
    chain: Optional[str]
    allChains: List[str]
    total24h: float
    total48hto24h: float
    total7d: float
    total14dto7d: float
    total30d: float
    total60dto30d: float
    total1y: float
    change_1d: float
    change_7d: float
    change_1m: float
    change_7dover7d: float
    change_30dover30d: float
    total7DaysAgo: float
    total30DaysAgo: float
    totalAllTime: float
    protocols: List[FeesProtocol]


class FeesSummaryChildProtocol(TypedDict, total=False):
    name: str
    defillamaId: str
    displayName: str
    methodologyURL: Optional[str]
    methodology: Optional[Dict[str, str]]
    defaultChartView: Optional[str]
    breakdownMethodology: Optional[str]


class FeesSummaryResponse(TypedDict, total=False):
    id: str
    name: str
    url: str
    description: str
    logo: str
    gecko_id: Optional[str]
    cmcId: Optional[str]
    chains: List[str]
    twitter: Optional[str]
    treasury: Optional[str]
    governanceID: Optional[List[str]]
    github: Optional[List[str]]
    symbol: Optional[str]
    address: Optional[str]
    linkedProtocols: Optional[List[str]]
    childProtocols: Optional[List[FeesSummaryChildProtocol]]
    defillamaId: str
    displayName: str
    module: Optional[str]
    category: Optional[str]
    methodologyURL: Optional[str]
    methodology: Optional[Dict[str, str]]
    forkedFrom: Optional[List[str]]
    audits: Optional[str]
    audit_links: Optional[List[str]]
    parentProtocol: Optional[str]
    previousNames: Optional[List[str]]
    hallmarks: Optional[List[List[object]]]
    defaultChartView: Optional[str]
    doublecounted: Optional[bool]
    breakdownMethodology: Optional[str]
    slug: str
    protocolType: str
    total24h: Optional[float]
    total48hto24h: Optional[float]
    total7d: Optional[float]
    total30d: Optional[float]
    totalAllTime: Optional[float]
    totalDataChart: List[Tuple[int, float]]
    totalDataChartBreakdown: List["NestedChartBreakdownDataPoint"]
    hasLabelBreakdown: bool
    change_1d: Optional[float]


ChartDataPoint = Tuple[int, float]
ChartBreakdownDataPoint = Tuple[int, Dict[str, float]]
NestedChartBreakdownDataPoint = Tuple[int, Dict[str, Dict[str, float]]]


class FeesChartResponse(TypedDict):
    data: List[ChartDataPoint]


class FeesChartBreakdownResponse(TypedDict):
    data: List[ChartBreakdownDataPoint]


class FeesMetricsResponse(TypedDict, total=False):
    total24h: float
    total7d: float
    total30d: float
    total1y: Optional[float]
    change_1d: float
    change_7d: float
    change_1m: float
    protocols: List[FeesProtocol]
    allChains: List[str]


class FeesMetricsByProtocolResponse(TypedDict, total=False):
    id: str
    name: str
    address: Optional[str]
    symbol: Optional[str]
    url: str
    description: str
    chain: str
    logo: str
    audits: str
    audit_note: Optional[str]
    gecko_id: Optional[str]
    cmcId: Optional[str]
    category: Optional[str]
    chains: List[str]
    module: Optional[str]
    twitter: Optional[str]
    audit_links: Optional[List[str]]
    github: Optional[List[str]]
    dimensions: Optional[Dict[str, object]]
    methodology: Optional[Dict[str, str]]
    misrepresentedTokens: Optional[bool]
    doublecounted: Optional[bool]
    defillamaId: str
    displayName: str
    methodologyURL: Optional[str]
    forkedFrom: Optional[List[str]]
    governanceID: Optional[List[str]]
    treasury: Optional[str]
    parentProtocol: Optional[str]
    previousNames: Optional[List[str]]
    hallmarks: Optional[List[List[object]]]
    defaultChartView: Optional[str]
    breakdownMethodology: Optional[str]
    slug: str
    protocolType: str
    total24h: Optional[float]
    total48hto24h: Optional[float]
    total7d: Optional[float]
    total30d: Optional[float]
    totalAllTime: Optional[float]
    hasLabelBreakdown: bool


__all__ = [
    "FeesOverviewOptions",
    "FeesSummaryOptions",
    "FeesChartOptions",
    "FeesProtocol",
    "FeesOverviewResponse",
    "FeesSummaryChildProtocol",
    "FeesSummaryResponse",
    "ChartDataPoint",
    "ChartBreakdownDataPoint",
    "NestedChartBreakdownDataPoint",
    "FeesChartResponse",
    "FeesChartBreakdownResponse",
    "FeesMetricsResponse",
    "FeesMetricsByProtocolResponse",
]
