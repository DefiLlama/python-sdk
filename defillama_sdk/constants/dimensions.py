"""Dimension constants used by fees and volume endpoints."""

from enum import Enum
from typing import Dict, Literal


class AdapterType(str, Enum):
    DEXS = "dexs"
    FEES = "fees"
    AGGREGATORS = "aggregators"
    DERIVATIVES = "derivatives"
    AGGREGATOR_DERIVATIVES = "aggregator-derivatives"
    OPTIONS = "options"
    BRIDGE_AGGREGATORS = "bridge-aggregators"
    OPEN_INTEREST = "open-interest"


class FeeDataType(str, Enum):
    DAILY_FEES = "dailyFees"
    DAILY_REVENUE = "dailyRevenue"
    DAILY_HOLDERS_REVENUE = "dailyHoldersRevenue"
    DAILY_SUPPLY_SIDE_REVENUE = "dailySupplySideRevenue"
    DAILY_BRIBES_REVENUE = "dailyBribesRevenue"
    DAILY_TOKEN_TAXES = "dailyTokenTaxes"
    DAILY_APP_FEES = "dailyAppFees"
    DAILY_APP_REVENUE = "dailyAppRevenue"
    DAILY_EARNINGS = "dailyEarnings"


class VolumeDataType(str, Enum):
    DAILY_VOLUME = "dailyVolume"
    TOTAL_VOLUME = "totalVolume"
    DAILY_NOTIONAL_VOLUME = "dailyNotionalVolume"
    DAILY_PREMIUM_VOLUME = "dailyPremiumVolume"
    DAILY_BRIDGE_VOLUME = "dailyBridgeVolume"
    OPEN_INTEREST_AT_END = "openInterestAtEnd"


DataTypeShortKeys: Dict[str, str] = {
    "dailyFees": "df",
    "dailyRevenue": "dr",
    "dailyHoldersRevenue": "dhr",
    "dailySupplySideRevenue": "dssr",
    "dailyBribesRevenue": "dbr",
    "dailyTokenTaxes": "dtt",
    "dailyAppRevenue": "dar",
    "dailyAppFees": "daf",
    "dailyNotionalVolume": "dnv",
    "dailyPremiumVolume": "dpv",
    "openInterestAtEnd": "doi",
    "dailyVolume": "dv",
    "dailyBridgeVolume": "dbv",
}

DataTypeShortKey = Literal[
    "dailyFees",
    "dailyRevenue",
    "dailyHoldersRevenue",
    "dailySupplySideRevenue",
    "dailyBribesRevenue",
    "dailyTokenTaxes",
    "dailyAppRevenue",
    "dailyAppFees",
    "dailyNotionalVolume",
    "dailyPremiumVolume",
    "openInterestAtEnd",
    "dailyVolume",
    "dailyBridgeVolume",
]
