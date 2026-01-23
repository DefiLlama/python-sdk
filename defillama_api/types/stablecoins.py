"""Stablecoin type definitions."""

from typing import Dict, List, Optional, TypedDict


class PeggedAsset(TypedDict, total=False):
    peggedUSD: Optional[float]
    peggedVAR: Optional[float]
    peggedEUR: Optional[float]
    peggedJPY: Optional[float]
    peggedCNY: Optional[float]
    peggedUAH: Optional[float]
    peggedARS: Optional[float]
    peggedGBP: Optional[float]
    peggedCAD: Optional[float]
    peggedAUD: Optional[float]
    peggedSGD: Optional[float]
    peggedCHF: Optional[float]
    peggedREAL: Optional[float]
    peggedRUB: Optional[float]
    peggedMXN: Optional[float]
    peggedPHP: Optional[float]
    peggedTRY: Optional[float]


class StablecoinChainCirculating(TypedDict):
    current: PeggedAsset
    circulatingPrevDay: PeggedAsset
    circulatingPrevWeek: PeggedAsset
    circulatingPrevMonth: PeggedAsset


class Stablecoin(TypedDict, total=False):
    id: str
    name: str
    symbol: str
    gecko_id: Optional[str]
    pegType: str
    pegMechanism: str
    circulating: PeggedAsset
    circulatingPrevDay: PeggedAsset
    circulatingPrevWeek: PeggedAsset
    circulatingPrevMonth: PeggedAsset
    chainCirculating: Dict[str, StablecoinChainCirculating]
    chains: List[str]
    price: Optional[float]
    priceSource: Optional[str]


class StablecoinsResponse(TypedDict):
    peggedAssets: List[Stablecoin]


class StablecoinChartDataPoint(TypedDict, total=False):
    date: str
    totalCirculating: PeggedAsset
    totalUnreleased: Optional[PeggedAsset]
    totalCirculatingUSD: PeggedAsset
    totalMintedToL2: Optional[PeggedAsset]


class StablecoinChainDataPoint(TypedDict):
    date: str
    totalCirculating: PeggedAsset
    totalCirculatingUSD: PeggedAsset


class StablecoinTokenInfo(TypedDict):
    name: str
    address: str


class StablecoinChainBreakdown(TypedDict, total=False):
    tokens: Optional[List[StablecoinTokenInfo]]
    circulating: PeggedAsset
    circulatingPrevDay: PeggedAsset
    circulatingPrevWeek: PeggedAsset
    circulatingPrevMonth: PeggedAsset
    bridgedTo: Optional[str]
    minted: Optional[str]
    bridgeInfo: Optional[Dict[str, Dict[str, str]]]


class StablecoinDetails(TypedDict, total=False):
    id: str
    name: str
    address: str
    symbol: str
    url: str
    description: str
    mintRedeemDescription: Optional[str]
    onCoinGecko: str
    gecko_id: Optional[str]
    cmcId: Optional[str]
    pegType: str
    pegMechanism: str
    priceSource: Optional[str]
    auditLinks: Optional[List[str]]
    twitter: Optional[str]
    wiki: Optional[str]
    price: Optional[float]
    tokens: List["StablecoinSupplyPoint"]
    chainBalances: Dict[str, "StablecoinChainBalanceHistory"]
    currentChainBalances: Dict[str, PeggedAsset]


class StablecoinChainMcap(TypedDict, total=False):
    gecko_id: Optional[str]
    totalCirculatingUSD: PeggedAsset
    tokenSymbol: Optional[str]
    name: str


class StablecoinPricePoint(TypedDict):
    date: int
    prices: Dict[str, Optional[float]]


class StablecoinSupplyPoint(TypedDict):
    date: int
    circulating: PeggedAsset


class StablecoinChainBalanceTokenPoint(StablecoinSupplyPoint, total=False):
    bridgedTo: Optional[PeggedAsset]


class StablecoinChainBalanceHistory(TypedDict):
    tokens: List[StablecoinChainBalanceTokenPoint]


class StablecoinDominanceGreatestMcap(TypedDict):
    gecko_id: str
    symbol: str
    mcap: float


class StablecoinDominanceDataPoint(TypedDict):
    date: str
    totalCirculatingUSD: PeggedAsset
    greatestMcap: StablecoinDominanceGreatestMcap


__all__ = [
    "PeggedAsset",
    "Stablecoin",
    "StablecoinsResponse",
    "StablecoinChartDataPoint",
    "StablecoinChainDataPoint",
    "StablecoinTokenInfo",
    "StablecoinChainBreakdown",
    "StablecoinDetails",
    "StablecoinChainMcap",
    "StablecoinPricePoint",
    "StablecoinSupplyPoint",
    "StablecoinChainBalanceTokenPoint",
    "StablecoinChainBalanceHistory",
    "StablecoinDominanceDataPoint",
]
