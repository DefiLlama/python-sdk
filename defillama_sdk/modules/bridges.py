"""Bridges module implementation."""

from typing import List, Optional
from urllib.parse import quote

from ..client import BaseClient
from ..types.bridges import (
    BridgeDayStatsResponse,
    BridgeDetail,
    BridgeTransaction,
    BridgeTransactionsOptions,
    BridgeVolumeDataPoint,
    BridgesOptions,
    BridgesResponse,
)


class BridgesModule:
    """Access bridge volume and transaction data."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getAll(self, options: Optional[BridgesOptions] = None) -> BridgesResponse:
        """Get all bridges with volume data."""

        params = None
        if options and options.get("includeChains") is not None:
            params = {"includeChains": options.get("includeChains")}
        return self._client.get(
            "/bridges",
            base="bridges",
            params=params,
        )

    def getById(self, bridge_id: int) -> BridgeDetail:
        """Get detailed bridge information by ID."""

        return self._client.get(
            f"/bridge/{bridge_id}",
            base="bridges",
        )

    def getVolumeByChain(self, chain: str) -> List[BridgeVolumeDataPoint]:
        """Get bridge volume for a chain."""

        return self._client.get(
            f"/bridgevolume/{quote(chain)}",
            base="bridges",
        )

    def getDayStats(self, timestamp: int, chain: str) -> BridgeDayStatsResponse:
        """Get daily bridge statistics for a chain."""

        return self._client.get(
            f"/bridgedaystats/{timestamp}/{quote(chain)}",
            base="bridges",
        )

    def getTransactions(
        self, bridge_id: int, options: Optional[BridgeTransactionsOptions] = None
    ) -> List[BridgeTransaction]:
        """Get bridge transactions."""

        params = {}
        if options:
            if options.get("limit") is not None:
                params["limit"] = options.get("limit")
            if options.get("startTimestamp") is not None:
                params["startTimestamp"] = options.get("startTimestamp")
            if options.get("endTimestamp") is not None:
                params["endTimestamp"] = options.get("endTimestamp")
            if options.get("sourceChain"):
                params["sourceChain"] = options.get("sourceChain")
            if options.get("address"):
                params["address"] = options.get("address")
        return self._client.get(
            f"/transactions/{bridge_id}",
            base="bridges",
            params=params or None,
        )
