"""ETFs module implementation."""

from urllib.parse import quote

from ..client import BaseClient
from ..types.etfs import EtfHistoryItem, EtfOverviewItem, FdvPeriod, FdvPerformanceItem


class EtfsModule:
    """Access ETF data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getOverview(self) -> list[EtfOverviewItem]:
        """Get Bitcoin ETF overview."""

        return self._client.get(
            "/overview",
            requires_auth=True,
            api_namespace="etfs",
        )

    def getOverviewEth(self) -> list[EtfOverviewItem]:
        """Get Ethereum ETF overview."""

        return self._client.get(
            "/overviewEth",
            requires_auth=True,
            api_namespace="etfs",
        )

    def getHistory(self) -> list[EtfHistoryItem]:
        """Get Bitcoin ETF flow history."""

        return self._client.get(
            "/history",
            requires_auth=True,
            api_namespace="etfs",
        )

    def getHistoryEth(self) -> list[EtfHistoryItem]:
        """Get Ethereum ETF flow history."""

        return self._client.get(
            "/historyEth",
            requires_auth=True,
            api_namespace="etfs",
        )

    def getFdvPerformance(self, period: FdvPeriod) -> list[FdvPerformanceItem]:
        """Get FDV performance data."""

        return self._client.get(
            f"/performance/{quote(period)}",
            requires_auth=True,
            api_namespace="fdv",
        )
