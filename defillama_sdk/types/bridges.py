"""Bridge type definitions."""

from typing import Dict, List, Optional, TypedDict


class TransactionCounts(TypedDict):
    deposits: int
    withdrawals: int


class BridgeSummary(TypedDict, total=False):
    id: int
    defillamaId: Optional[str]
    name: str
    displayName: str
    icon: Optional[str]
    volumePrevDay: float
    volumePrev2Day: Optional[float]
    lastHourlyVolume: float
    last24hVolume: float
    lastDailyVolume: float
    dayBeforeLastVolume: Optional[float]
    weeklyVolume: Optional[float]
    monthlyVolume: Optional[float]
    chains: Optional[List[str]]
    destinationChain: Optional[str]
    url: Optional[str]
    slug: Optional[str]


class BridgeChainInfo(TypedDict, total=False):
    gecko_id: Optional[str]
    volumePrevDay: float
    tokenSymbol: Optional[str]
    name: str


class BridgesResponse(TypedDict, total=False):
    bridges: List[BridgeSummary]
    chains: Optional[List[BridgeChainInfo]]


class ChainVolumeBreakdown(TypedDict):
    lastHourlyVolume: float
    currentDayVolume: float
    lastDailyVolume: float
    dayBeforeLastVolume: float
    weeklyVolume: float
    monthlyVolume: float
    last24hVolume: float
    lastHourlyTxs: TransactionCounts
    currentDayTxs: TransactionCounts
    prevDayTxs: TransactionCounts
    dayBeforeLastTxs: TransactionCounts
    weeklyTxs: TransactionCounts
    monthlyTxs: TransactionCounts


class BridgeDetail(TypedDict, total=False):
    id: int
    name: str
    displayName: str
    lastHourlyVolume: float
    currentDayVolume: float
    lastDailyVolume: float
    dayBeforeLastVolume: float
    weeklyVolume: float
    monthlyVolume: float
    lastHourlyTxs: TransactionCounts
    currentDayTxs: TransactionCounts
    prevDayTxs: TransactionCounts
    dayBeforeLastTxs: TransactionCounts
    weeklyTxs: TransactionCounts
    monthlyTxs: TransactionCounts
    chainBreakdown: Optional[Dict[str, ChainVolumeBreakdown]]
    destinationChain: Optional[str]


class BridgeVolumeDataPoint(TypedDict):
    date: str
    depositUSD: float
    withdrawUSD: float
    depositTxs: int
    withdrawTxs: int


class TokenDayStats(TypedDict):
    usdValue: float
    amount: str
    symbol: str
    decimals: int


class AddressDayStats(TypedDict):
    usdValue: float
    txs: int


class BridgeDayStatsResponse(TypedDict):
    date: int
    totalTokensDeposited: Dict[str, TokenDayStats]
    totalTokensWithdrawn: Dict[str, TokenDayStats]
    totalAddressDeposited: Dict[str, AddressDayStats]
    totalAddressWithdrawn: Dict[str, AddressDayStats]


class BridgesOptions(TypedDict, total=False):
    includeChains: Optional[bool]


class BridgeTransactionsOptions(TypedDict, total=False):
    limit: Optional[int]
    startTimestamp: Optional[int]
    endTimestamp: Optional[int]
    sourceChain: Optional[str]
    address: Optional[str]


class BridgeTransaction(TypedDict, total=False):
    tx_hash: str
    ts: str
    tx_block: int
    tx_from: str
    tx_to: str
    token: str
    amount: str
    is_deposit: bool
    chain: str
    bridge_name: str
    usd_value: Optional[float]


__all__ = [
    "TransactionCounts",
    "BridgeSummary",
    "BridgeChainInfo",
    "BridgesResponse",
    "ChainVolumeBreakdown",
    "BridgeDetail",
    "BridgeVolumeDataPoint",
    "TokenDayStats",
    "AddressDayStats",
    "BridgeDayStatsResponse",
    "BridgesOptions",
    "BridgeTransactionsOptions",
    "BridgeTransaction",
]
