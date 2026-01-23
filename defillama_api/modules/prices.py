"""Prices module implementation."""

import json
from typing import Dict, List, Optional
from urllib.parse import quote

from ..client import BaseClient
from ..types.prices import (
    BatchHistoricalResponse,
    BlockInfo,
    ChartOptions,
    ChartResponse,
    CoinPricesResponse,
    FirstPriceResponse,
    PercentageOptions,
    PercentageResponse,
)


class PricesModule:
    """Access token price data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getCurrentPrices(
        self, coins: List[str], searchWidth: Optional[str] = None
    ) -> CoinPricesResponse:
        """Get current prices for multiple tokens."""

        coins_param = ",".join(coins)
        params = {"searchWidth": searchWidth} if searchWidth else None
        return self._client.get(
            f"/prices/current/{coins_param}",
            base="coins",
            params=params,
        )

    def getHistoricalPrices(
        self, timestamp: int, coins: List[str], searchWidth: Optional[str] = None
    ) -> CoinPricesResponse:
        """Get historical prices at a specific timestamp."""

        coins_param = ",".join(coins)
        params = {"searchWidth": searchWidth} if searchWidth else None
        return self._client.get(
            f"/prices/historical/{timestamp}/{coins_param}",
            base="coins",
            params=params,
        )

    def getBatchHistoricalPrices(
        self, coins: Dict[str, List[int]], searchWidth: Optional[str] = None
    ) -> BatchHistoricalResponse:
        """Get multiple historical price points in one request."""

        params = {
            "coins": json.dumps(coins),
            "searchWidth": searchWidth,
        }
        return self._client.get(
            "/batchHistorical",
            base="coins",
            params=params,
        )

    def getChart(
        self, coins: List[str], options: Optional[ChartOptions] = None
    ) -> ChartResponse:
        """Get price chart data at regular intervals."""

        coins_param = ",".join(coins)
        params = None
        if options:
            params = {
                "start": options.get("start"),
                "end": options.get("end"),
                "span": options.get("span"),
                "period": options.get("period"),
                "searchWidth": options.get("searchWidth"),
            }
        return self._client.get(
            f"/chart/{coins_param}",
            base="coins",
            params=params,
        )

    def getPercentageChange(
        self, coins: List[str], options: Optional[PercentageOptions] = None
    ) -> PercentageResponse:
        """Get percentage price change over a period."""

        coins_param = ",".join(coins)
        params = None
        if options:
            params = {
                "timestamp": options.get("timestamp"),
                "lookForward": options.get("lookForward"),
                "period": options.get("period"),
            }
        return self._client.get(
            f"/percentage/{coins_param}",
            base="coins",
            params=params,
        )

    def getFirstPrices(self, coins: List[str]) -> FirstPriceResponse:
        """Get the earliest recorded price for tokens."""

        coins_param = ",".join(coins)
        return self._client.get(
            f"/prices/first/{coins_param}",
            base="coins",
        )

    def getBlockAtTimestamp(self, chain: str, timestamp: int) -> BlockInfo:
        """Get the closest block to a given timestamp."""

        return self._client.get(
            f"/block/{quote(chain)}/{timestamp}",
            base="coins",
        )
