"""Digital Asset Treasury type definitions."""

from typing import Dict, List, Optional, Tuple, TypedDict, Union


class InstitutionHolding(TypedDict, total=False):
    amount: float
    avgPrice: Optional[float]
    usdValue: float
    cost: Optional[float]
    transactionCount: Optional[int]
    firstAnnouncementDate: Optional[str]
    lastAnnouncementDate: Optional[str]
    supplyPercentage: Optional[float]


class InstitutionMetadata(TypedDict, total=False):
    institutionId: int
    ticker: str
    name: str
    type: Optional[str]
    price: Optional[float]
    priceChange24h: Optional[float]
    volume24h: Optional[float]
    fd_realized: Optional[Union[float, str]]
    fd_realistic: Optional[Union[float, str]]
    fd_maximum: Optional[Union[float, str]]
    mcapRealized: Optional[float]
    mcapRealistic: Optional[float]
    mcapMax: Optional[float]
    realized_mNAV: Optional[float]
    realistic_mNAV: Optional[float]
    max_mNAV: Optional[float]
    totalCost: Optional[float]
    totalUsdValue: Optional[float]
    holdings: Optional[Dict[str, InstitutionHolding]]
    description: Optional[str]
    logo: Optional[str]
    url: Optional[str]
    country: Optional[str]
    exchange: Optional[str]
    marketCap: Optional[float]
    totalBitcoin: Optional[float]
    totalEthereum: Optional[float]


class DatAssetMetadata(TypedDict, total=False):
    name: str
    ticker: str
    geckoId: Optional[str]
    companies: Optional[int]
    totalAmount: Optional[float]
    totalUsdValue: Optional[float]
    circSupplyPerc: Optional[float]


class DatInstitutionSummary(TypedDict):
    institutionId: int
    totalUsdValue: float
    totalCost: Optional[float]


class DatAssetInstitutionSummary(TypedDict):
    institutionId: int
    usdValue: float
    amount: float


DatFlowPoint = Tuple[float, float, float, float, float, float]
DatMnavPoint = Tuple[float, float, float, float]
DatStatsPoint = Tuple[
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
]
DatOhlcvPoint = Tuple[float, float, float, float, float, float]


class DatInstitutionsResponse(TypedDict, total=False):
    institutionMetadata: Dict[str, InstitutionMetadata]
    assetMetadata: Dict[str, DatAssetMetadata]
    institutions: List[DatInstitutionSummary]
    assets: Dict[str, List[DatAssetInstitutionSummary]]
    flows: Optional[Dict[str, List[DatFlowPoint]]]
    mNAV: Optional[Dict[str, Dict[str, List[DatMnavPoint]]]]
    totalCompanies: int
    lastUpdated: str


class DatInstitutionAssetMeta(TypedDict):
    name: str
    ticker: str


class DatInstitutionResponse(TypedDict, total=False):
    institutionId: int
    ticker: str
    name: str
    type: Optional[str]
    rank: Optional[int]
    price: Optional[float]
    priceChange24h: Optional[float]
    volume24h: Optional[float]
    fd_realized: Optional[Union[float, str]]
    fd_realistic: Optional[Union[float, str]]
    fd_max: Optional[Union[float, str]]
    mcap_realized: Optional[float]
    mcap_realistic: Optional[float]
    mcap_max: Optional[float]
    realized_mNAV: Optional[float]
    realistic_mNAV: Optional[float]
    max_mNAV: Optional[float]
    totalCost: Optional[float]
    totalUsdValue: Optional[float]
    assets: Optional[Dict[str, InstitutionHolding]]
    assetsMeta: Optional[Dict[str, DatInstitutionAssetMeta]]
    assetValue: Optional[List[Tuple[float, float]]]
    stats: Optional[List[DatStatsPoint]]
    ohlcv: Optional[List[DatOhlcvPoint]]
    transactions: Optional[List[object]]
    lastUpdated: Optional[str]


__all__ = [
    "InstitutionHolding",
    "InstitutionMetadata",
    "DatAssetMetadata",
    "DatInstitutionSummary",
    "DatAssetInstitutionSummary",
    "DatFlowPoint",
    "DatMnavPoint",
    "DatStatsPoint",
    "DatOhlcvPoint",
    "DatInstitutionsResponse",
    "DatInstitutionAssetMeta",
    "DatInstitutionResponse",
]
