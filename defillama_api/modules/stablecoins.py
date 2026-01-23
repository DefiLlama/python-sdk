"""Stablecoins module implementation."""

from typing import List, Optional
from urllib.parse import quote

from ..client import BaseClient
from ..types.stablecoins import (
    StablecoinChainDataPoint,
    StablecoinChainMcap,
    StablecoinChartDataPoint,
    StablecoinDetails,
    StablecoinDominanceDataPoint,
    StablecoinPricePoint,
    StablecoinsResponse,
)


class StablecoinsModule:
    """Access stablecoin data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getStablecoins(self, includePrices: Optional[bool] = None) -> StablecoinsResponse:
        """Get all stablecoins with current market caps."""

        params = {"includePrices": includePrices} if includePrices is not None else None
        return self._client.get(
            "/stablecoins",
            base="stablecoins",
            params=params,
        )

    def getAllCharts(self) -> List[StablecoinChartDataPoint]:
        """Get historical market cap data for all stablecoins."""

        return self._client.get("/stablecoincharts/all", base="stablecoins")

    def getChartsByChain(self, chain: str) -> List[StablecoinChainDataPoint]:
        """Get historical market cap data for stablecoins on a chain."""

        return self._client.get(
            f"/stablecoincharts/{quote(chain)}",
            base="stablecoins",
        )

    def getStablecoin(self, asset: str) -> StablecoinDetails:
        """Get detailed information about a stablecoin."""

        return self._client.get(
            f"/stablecoin/{quote(asset)}",
            base="stablecoins",
        )

    def getChains(self) -> List[StablecoinChainMcap]:
        """Get stablecoin market cap for all chains."""

        return self._client.get("/stablecoinchains", base="stablecoins")

    def getPrices(self) -> List[StablecoinPricePoint]:
        """Get historical prices for all stablecoins."""

        return self._client.get("/stablecoinprices", base="stablecoins")

    def getDominance(
        self, chain: str, stablecoinId: Optional[int] = None
    ) -> List[StablecoinDominanceDataPoint]:
        """Get stablecoin dominance data for a chain."""

        params = {"stablecoin": stablecoinId} if stablecoinId is not None else None
        return self._client.get(
            f"/stablecoindominance/{quote(chain)}",
            requires_auth=True,
            api_namespace="stablecoins",
            params=params,
        )
