"""TVL type definitions."""

from typing import Dict, List, Optional, TypedDict, Union


class Protocol(TypedDict, total=False):
    id: str
    name: str
    address: Optional[str]
    symbol: str
    url: str
    description: Optional[str]
    chain: str
    logo: Optional[str]
    audits: Optional[str]
    audit_note: Optional[str]
    gecko_id: Optional[str]
    cmcId: Optional[str]
    category: str
    chains: List[str]
    module: Optional[str]
    twitter: Optional[str]
    forkedFrom: Optional[List[str]]
    oracles: Optional[List[str]]
    listedAt: Optional[int]
    methodology: Optional[Union[str, Dict[str, str]]]
    slug: str
    tvl: float
    chainTvls: Dict[str, float]
    change_1h: Optional[float]
    change_1d: Optional[float]
    change_7d: Optional[float]
    tokenBreakdowns: Optional[Dict[str, object]]
    mcap: Optional[float]
    referralUrl: Optional[str]
    parentProtocol: Optional[str]
    misrepresentedTokens: Optional[bool]


class TvlDataPoint(TypedDict):
    date: int
    totalLiquidityUSD: float


class TokenBalance(TypedDict):
    date: int
    tokens: Dict[str, float]


class ChainTvlData(TypedDict, total=False):
    tvl: List[TvlDataPoint]
    tokensInUsd: Optional[List[TokenBalance]]
    tokens: Optional[List[TokenBalance]]


class CurrentChainTvl(TypedDict):
    date: int
    totalLiquidityUSD: float


class ProtocolRaise(TypedDict, total=False):
    date: int
    amount: float
    round: str
    name: Optional[str]
    chains: Optional[List[str]]
    sector: Optional[str]
    category: Optional[str]
    categoryGroup: Optional[str]
    leadInvestors: Optional[List[str]]
    otherInvestors: Optional[List[str]]
    source: Optional[str]
    valuation: Optional[float]
    defillamaId: Optional[Union[str, int]]


class ProtocolMetrics(TypedDict, total=False):
    activeUsers: Optional[int]
    transactions: Optional[int]
    gasUsed: Optional[int]


class ProtocolDetails(TypedDict, total=False):
    id: str
    name: str
    address: Optional[str]
    symbol: str
    url: str
    description: Optional[str]
    chain: Optional[str]
    logo: Optional[str]
    audits: Optional[str]
    audit_note: Optional[str]
    gecko_id: Optional[str]
    cmcId: Optional[str]
    category: Optional[str]
    chains: List[str]
    module: Optional[str]
    twitter: Optional[str]
    forkedFrom: Optional[List[str]]
    oracles: Optional[List[str]]
    listedAt: Optional[int]
    methodology: Optional[Union[str, Dict[str, str]]]
    slug: Optional[str]
    tvl: List[TvlDataPoint]
    tokensInUsd: Optional[List[TokenBalance]]
    tokens: Optional[List[TokenBalance]]
    chainTvls: Dict[str, ChainTvlData]
    currentChainTvls: Dict[str, float]
    raises: Optional[List[ProtocolRaise]]
    metrics: Optional[ProtocolMetrics]
    mcap: Optional[float]
    isParentProtocol: Optional[bool]
    otherProtocols: Optional[List[str]]
    treasury: Optional[str]
    governanceID: Optional[List[str]]
    wrongLiquidity: Optional[bool]
    github: Optional[List[str]]
    stablecoins: Optional[List[str]]
    hallmarks: Optional[List[List[Union[int, str]]]]


class Chain(TypedDict, total=False):
    gecko_id: Optional[str]
    tvl: float
    tokenSymbol: Optional[str]
    cmcId: Optional[str]
    name: str
    chainId: Optional[int]


class HistoricalChainTvl(TypedDict):
    date: int
    tvl: float


class HistoricalChainsTvl(TypedDict, total=False):
    date: int


class TokenProtocolHolding(TypedDict, total=False):
    name: str
    category: str
    amountUsd: Dict[str, float]
    misrepresentedTokens: Optional[bool]


class TokenTvlSnapshot(TypedDict):
    tvl: Dict[str, float]


class ProtocolInflowsResponse(TypedDict):
    outflows: float
    oldTokens: TokenTvlSnapshot
    currentTokens: TokenTvlSnapshot


class ChainAssetBreakdown(TypedDict):
    total: str
    breakdown: Dict[str, str]


class ChainAsset(TypedDict, total=False):
    canonical: Optional[ChainAssetBreakdown]
    ownTokens: Optional[ChainAssetBreakdown]
    native: Optional[ChainAssetBreakdown]
    thirdParty: Optional[ChainAssetBreakdown]
    total: Optional[ChainAssetBreakdown]


ChainAssetsResponse = Dict[str, Union[ChainAsset, float, int]]


__all__ = [
    "Protocol",
    "ProtocolDetails",
    "Chain",
    "TvlDataPoint",
    "TokenBalance",
    "ChainTvlData",
    "CurrentChainTvl",
    "HistoricalChainTvl",
    "HistoricalChainsTvl",
    "TokenProtocolHolding",
    "ProtocolInflowsResponse",
    "ChainAsset",
    "ChainAssetBreakdown",
    "ChainAssetsResponse",
]
