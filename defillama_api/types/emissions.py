"""Emission type definitions."""

from typing import Dict, List, Optional, TypedDict, Union


class EmissionEvent(TypedDict, total=False):
    description: str
    timestamp: int
    noOfTokens: List[float]
    category: str
    unlockType: str
    rateDurationDays: Optional[int]


class NextEvent(TypedDict):
    date: int
    toUnlock: float


class EmissionToken(TypedDict, total=False):
    token: str
    sources: List[str]
    protocolId: str
    name: str
    circSupply: float
    circSupply30d: float
    totalLocked: float
    maxSupply: float
    gecko_id: str
    events: List[EmissionEvent]
    unlockEvents: Optional[List[object]]
    nextEvent: Optional[NextEvent]
    unlocksPerDay: Optional[float]
    mcap: float


class UnlockDataPoint(TypedDict):
    timestamp: int
    unlocked: float
    rawEmission: float
    burned: float


class EmissionCategoryData(TypedDict):
    label: str
    data: List[UnlockDataPoint]


TokenAllocationBreakdown = Dict[str, float]


class TokenAllocationBySection(TypedDict):
    current: Dict[str, float]
    final: Dict[str, float]
    progress: Dict[str, float]


class TokenAllocation(TypedDict, total=False):
    current: TokenAllocationBreakdown
    final: TokenAllocationBreakdown
    progress: TokenAllocationBreakdown
    bySection: Optional[TokenAllocationBySection]


class EmissionDocumentedData(TypedDict):
    data: List[EmissionCategoryData]
    tokenAllocation: TokenAllocation


class CliffAllocation(TypedDict):
    recipient: str
    category: str
    unlockType: str
    amount: float


class LinearAllocation(TypedDict):
    recipient: str
    category: str
    unlockType: str
    previousRatePerWeek: float
    newRatePerWeek: float
    endTimestamp: int


class UnlockEventSummary(TypedDict, total=False):
    totalTokensCliff: Optional[float]
    netChangeInWeeklyRate: Optional[float]
    totalNewWeeklyRate: Optional[float]


class UnlockEventItem(TypedDict):
    timestamp: int
    cliffAllocations: List[CliffAllocation]
    linearAllocations: List[LinearAllocation]
    summary: UnlockEventSummary


class EmissionMetadata(TypedDict, total=False):
    token: str
    sources: List[str]
    protocolIds: List[str]
    events: List[EmissionEvent]
    notes: List[str]
    total: Optional[float]
    chain: Optional[str]
    unlockEvents: List[UnlockEventItem]


class SupplyMetrics(TypedDict, total=False):
    maxSupply: Optional[float]
    adjustedSupply: Optional[float]
    tbdAmount: Optional[float]
    incentiveAmount: Optional[float]
    nonIncentiveAmount: Optional[float]


class EmissionBody(TypedDict, total=False):
    documentedData: EmissionDocumentedData
    metadata: EmissionMetadata
    name: str
    gecko_id: str
    defillamaIds: List[str]
    categories: Dict[str, List[str]]
    protocolCategory: str
    chainName: str
    pId: str
    unlockUsdChart: List[object]
    supplyMetrics: SupplyMetrics


class EmissionDetailResponse(TypedDict):
    body: EmissionBody
    lastModified: str


__all__ = [
    "EmissionEvent",
    "NextEvent",
    "EmissionToken",
    "UnlockDataPoint",
    "EmissionCategoryData",
    "TokenAllocationBreakdown",
    "TokenAllocationBySection",
    "TokenAllocation",
    "EmissionDocumentedData",
    "CliffAllocation",
    "LinearAllocation",
    "UnlockEventItem",
    "EmissionMetadata",
    "SupplyMetrics",
    "EmissionBody",
    "EmissionDetailResponse",
]
