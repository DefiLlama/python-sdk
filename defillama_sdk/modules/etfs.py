"""ETFs module implementation."""

from urllib.parse import quote

from ..client import BaseClient
from ..types.etfs import EtfFlowItem, EtfSnapshotItem, FdvPeriod, FdvPerformanceItem


class EtfsModule:
    """Access ETF data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getSnapshot(self) -> list[EtfSnapshotItem]:
        """Get every ETF with its current metrics, one row per ticker."""

        return self._client.get(
            "/snapshot",
            requires_auth=True,
            api_namespace="etfs",
        )

    def getFlows(self) -> list[EtfFlowItem]:
        """Get historical daily flows per asset."""

        return self._client.get(
            "/flows",
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
