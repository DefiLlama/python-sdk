"""Ecosystem type definitions."""

from typing import Dict, List, Optional, TypedDict


class CategoryTvlDataPoint(TypedDict, total=False):
    tvl: Optional[float]


class CategoriesResponse(TypedDict):
    chart: Dict[str, Dict[str, CategoryTvlDataPoint]]
    categories: Dict[str, List[str]]
    categoryPercentages: Optional[Dict[str, float]]


class ForkTvlDataPoint(TypedDict):
    tvl: float
    forks: Optional[float]


class ForksResponse(TypedDict, total=False):
    chart: Dict[str, Dict[str, ForkTvlDataPoint]]
    forks: Dict[str, List[str]]
    parentProtocols: Optional[Dict[str, str]]


class OracleTvlDataPoint(TypedDict, total=False):
    tvl: float
    protocolsSecured: Optional[float]


class OraclesResponse(TypedDict, total=False):
    chart: Dict[str, Dict[str, OracleTvlDataPoint]]
    chainChart: Optional[Dict[str, Dict[str, object]]]
    oraclesTVS: Optional[Dict[str, object]]
    oracles: Dict[str, List[str]]
    chainsByOracle: Optional[Dict[str, List[str]]]
    totalValueSecured: Optional[float]
    dominance: Optional[Dict[str, float]]


class TokenBreakdowns(TypedDict):
    ownTokens: float
    stablecoins: float
    majors: float
    others: float


class Entity(TypedDict, total=False):
    id: str
    name: str
    url: Optional[str]
    description: Optional[str]
    logo: Optional[str]
    category: Optional[str]
    module: Optional[str]
    twitter: Optional[str]
    symbol: Optional[str]
    chain: Optional[str]
    gecko_id: Optional[str]
    cmcId: Optional[str]
    chains: Optional[List[str]]
    misrepresentedTokens: Optional[bool]
    slug: Optional[str]
    tvl: float
    chainTvls: Optional[Dict[str, float]]
    change_1h: Optional[float]
    change_1d: Optional[float]
    change_7d: Optional[float]
    tokenBreakdowns: Optional[TokenBreakdowns]
    mcap: Optional[float]


class Treasury(TypedDict, total=False):
    id: str
    name: str
    address: Optional[str]
    symbol: Optional[str]
    url: Optional[str]
    description: Optional[str]
    chain: Optional[str]
    logo: Optional[str]
    audits: Optional[str]
    audit_note: Optional[str]
    audit_links: Optional[List[str]]
    gecko_id: Optional[str]
    cmcId: Optional[str]
    category: Optional[str]
    chains: Optional[List[str]]
    module: Optional[str]
    treasury: Optional[str]
    forkedFrom: Optional[List[str]]
    forkedFromIds: Optional[List[str]]
    twitter: Optional[str]
    misrepresentedTokens: Optional[bool]
    slug: Optional[str]
    tvl: float
    chainTvls: Optional[Dict[str, float]]
    change_1h: Optional[float]
    change_1d: Optional[float]
    change_7d: Optional[float]
    tokenBreakdowns: Optional[TokenBreakdowns]
    mcap: Optional[float]
    oracles: Optional[List[str]]
    oraclesBreakdown: Optional[object]
    listedAt: Optional[int]
    methodology: Optional[str]
    governanceID: Optional[List[str]]
    stablecoins: Optional[List[str]]
    referralUrl: Optional[str]
    openSource: Optional[bool]
    deadUrl: Optional[bool]
    deadFrom: Optional[int]
    github: Optional[List[str]]
    language: Optional[str]
    assetToken: Optional[str]
    dimensions: Optional[Dict[str, object]]
    hallmarks: Optional[List[List[object]]]
    previousNames: Optional[List[str]]
    rugged: Optional[bool]
    tags: Optional[List[str]]
    warningBanners: Optional[List[str]]
    wrongLiquidity: Optional[bool]


class Hack(TypedDict, total=False):
    date: int
    name: str
    classification: str
    technique: str
    amount: Optional[float]
    chain: List[str]
    bridgeHack: Optional[bool]
    targetType: Optional[str]
    source: Optional[str]
    returnedFunds: Optional[float]
    defillamaId: Optional[object]
    language: Optional[str]
    parentProtocolId: Optional[str]


class Raise(TypedDict, total=False):
    date: int
    name: str
    round: Optional[str]
    amount: float
    chains: Optional[List[str]]
    sector: Optional[str]
    category: Optional[str]
    categoryGroup: Optional[str]
    source: Optional[str]
    leadInvestors: List[str]
    otherInvestors: Optional[List[str]]
    valuation: Optional[float]
    defillamaId: Optional[str]


class RaisesResponse(TypedDict):
    raises: List[Raise]


__all__ = [
    "CategoryTvlDataPoint",
    "CategoriesResponse",
    "ForkTvlDataPoint",
    "ForksResponse",
    "OracleTvlDataPoint",
    "OraclesResponse",
    "TokenBreakdowns",
    "Entity",
    "Treasury",
    "Hack",
    "Raise",
    "RaisesResponse",
]
