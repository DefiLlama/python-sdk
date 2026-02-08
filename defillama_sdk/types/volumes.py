"""Volume type definitions."""

from typing import Dict, List, Optional, Tuple, TypedDict, Literal, Union


class VolumeOverviewOptions(TypedDict, total=False):
    excludeTotalDataChart: Optional[bool]
    excludeTotalDataChartBreakdown: Optional[bool]
    dataType: Optional[Literal["dailyVolume", "totalVolume"]]


class VolumeSummaryOptions(TypedDict, total=False):
    dataType: Optional[Literal["dailyVolume", "totalVolume"]]


class VolumeProtocol(TypedDict, total=False):
    defillamaId: str
    name: str
    displayName: str
    module: str
    category: str
    logo: str
    chains: List[str]
    protocolType: str
    methodologyURL: str
    methodology: Optional[object]
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
    change_1d: Optional[float]
    change_7d: Optional[float]
    change_1m: Optional[float]
    change_7dover7d: Optional[float]
    change_30dover30d: Optional[float]
    breakdown24h: Optional[Dict[str, Dict[str, float]]]
    breakdown30d: Optional[Dict[str, Dict[str, float]]]
    linkedProtocols: Optional[List[str]]
    doublecounted: Optional[bool]
    parentProtocol: Optional[str]
    slug: str


VolumeChartBreakdownDataPoint = Tuple[int, Dict[str, float]]
VolumeNestedChartBreakdownDataPoint = Tuple[int, Dict[str, Dict[str, float]]]


class VolumeOverviewResponse(TypedDict, total=False):
    totalDataChart: List[Tuple[int, float]]
    totalDataChartBreakdown: List[VolumeChartBreakdownDataPoint]
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
    protocols: List[VolumeProtocol]


class VolumeSummaryResponse(TypedDict, total=False):
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
    childProtocols: Optional[List[str]]
    defillamaId: str
    displayName: str
    module: str
    category: str
    methodologyURL: Optional[str]
    methodology: Optional[object]
    forkedFrom: Optional[List[str]]
    audits: Optional[str]
    audit_links: Optional[List[str]]
    parentProtocol: Optional[str]
    previousNames: Optional[List[str]]
    hallmarks: Optional[List[List[object]]]
    slug: str
    protocolType: str
    total24h: Optional[float]
    total48hto24h: Optional[float]
    total7d: Optional[float]
    total30d: Optional[float]
    totalAllTime: Optional[float]
    totalDataChart: List[Tuple[int, float]]
    totalDataChartBreakdown: List[VolumeNestedChartBreakdownDataPoint]
    hasLabelBreakdown: bool
    change_1d: Optional[float]


class VolumeMetricsOptions(TypedDict, total=False):
    dataType: Optional[Literal["dailyVolume", "totalVolume"]]


class VolumeMetricsProtocol(TypedDict, total=False):
    id: Optional[str]
    tokenRights: Optional[Dict[str, object]]
    symbol: Optional[str]
    address: Optional[str]
    linkedProtocols: Optional[List[str]]
    childProtocols: Optional[List["VolumeMetricsChildProtocol"]]
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
    hallmarks: Optional[List[Tuple[int, str]]]
    defaultChartView: Optional[str]
    breakdownMethodology: Optional[Union[str, Dict[str, Dict[str, str]]]]
    slug: str
    protocolType: str
    total24h: Optional[float]
    total48hto24h: Optional[float]
    total7d: Optional[float]
    total30d: Optional[float]
    totalAllTime: Optional[float]
    hasLabelBreakdown: bool
    change_1d: Optional[float]
    dimensions: Optional[Dict[str, object]]
    misrepresentedTokens: bool
    doublecounted: Optional[bool]
    referralUrl: Optional[str]


class VolumeMetricsChildProtocol(TypedDict, total=False):
    name: str
    defillamaId: str
    displayName: str
    methodologyURL: Optional[str]
    methodology: Optional[Dict[str, str]]
    defaultChartView: Optional[str]
    breakdownMethodology: Optional[Union[str, Dict[str, Dict[str, str]]]]


class VolumeMetricsResponse(TypedDict, total=False):
    protocols: List[VolumeMetricsProtocol]
    total24h: Optional[float]
    total48hto24h: Optional[float]
    total7d: Optional[float]
    total30d: Optional[float]
    totalAllTime: Optional[float]
    hasLabelBreakdown: bool
    change_1d: Optional[float]
    dimensions: Optional[Dict[str, object]]


class VolumeMetricsByProtocolResponse(TypedDict, total=False):
    id: Optional[str]
    tokenRights: Optional[Dict[str, object]]
    symbol: Optional[str]
    address: Optional[str]
    linkedProtocols: Optional[List[str]]
    childProtocols: Optional[List[VolumeMetricsChildProtocol]]
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
    hallmarks: Optional[List[Tuple[int, str]]]
    defaultChartView: Optional[str]
    breakdownMethodology: Optional[Union[str, Dict[str, Dict[str, str]]]]
    slug: str
    protocolType: str
    total24h: Optional[float]
    total48hto24h: Optional[float]
    total7d: Optional[float]
    total30d: Optional[float]
    totalAllTime: Optional[float]
    hasLabelBreakdown: bool
    change_1d: Optional[float]
    dimensions: Optional[Dict[str, object]]
    misrepresentedTokens: bool
    doublecounted: Optional[bool]
    referralUrl: Optional[str]


DexOverviewOptions = VolumeOverviewOptions
DexOverviewResponse = VolumeOverviewResponse
DexSummaryOptions = VolumeSummaryOptions
DexSummaryResponse = VolumeSummaryResponse
OptionsOverviewOptions = VolumeOverviewOptions
OptionsOverviewResponse = VolumeOverviewResponse
OptionsSummaryResponse = VolumeSummaryResponse
DerivativesOverviewResponse = VolumeOverviewResponse
DerivativesSummaryResponse = VolumeSummaryResponse

DexMetricsOptions = VolumeMetricsOptions
DexMetricsResponse = VolumeMetricsResponse
DexMetricsByProtocolResponse = VolumeMetricsByProtocolResponse
DerivativesMetricsOptions = VolumeMetricsOptions
DerivativesMetricsResponse = VolumeMetricsResponse
DerivativesMetricsByProtocolResponse = VolumeMetricsByProtocolResponse
OptionsMetricsOptions = VolumeMetricsOptions
OptionsMetricsResponse = VolumeMetricsResponse
OptionsMetricsByProtocolResponse = VolumeMetricsByProtocolResponse


__all__ = [
    "VolumeOverviewOptions",
    "VolumeSummaryOptions",
    "VolumeProtocol",
    "VolumeOverviewResponse",
    "VolumeSummaryResponse",
    "VolumeChartBreakdownDataPoint",
    "VolumeNestedChartBreakdownDataPoint",
    "VolumeMetricsOptions",
    "VolumeMetricsProtocol",
    "VolumeMetricsChildProtocol",
    "VolumeMetricsResponse",
    "VolumeMetricsByProtocolResponse",
    "DexOverviewOptions",
    "DexOverviewResponse",
    "DexSummaryOptions",
    "DexSummaryResponse",
    "OptionsOverviewOptions",
    "OptionsOverviewResponse",
    "OptionsSummaryResponse",
    "DerivativesOverviewResponse",
    "DerivativesSummaryResponse",
    "DexMetricsOptions",
    "DexMetricsResponse",
    "DexMetricsByProtocolResponse",
    "DerivativesMetricsOptions",
    "DerivativesMetricsResponse",
    "DerivativesMetricsByProtocolResponse",
    "OptionsMetricsOptions",
    "OptionsMetricsResponse",
    "OptionsMetricsByProtocolResponse",
]
