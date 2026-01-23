"""Fees module implementation."""

from typing import Optional
from urllib.parse import quote

from ..client import BaseClient
from ..types.fees import (
    ChartBreakdownDataPoint,
    ChartDataPoint,
    FeesChartOptions,
    FeesMetricsByProtocolResponse,
    FeesMetricsResponse,
    FeesOverviewOptions,
    FeesOverviewResponse,
    FeesSummaryOptions,
    FeesSummaryResponse,
)


def _data_type_value(value: Optional[object]) -> Optional[str]:
    if value is None:
        return None
    if hasattr(value, "value"):
        return str(getattr(value, "value"))
    return str(value)


class FeesModule:
    """Access fees and revenue data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getOverview(self, options: Optional[FeesOverviewOptions] = None) -> FeesOverviewResponse:
        """Get fees overview across all protocols."""

        params = {}
        if options:
            if options.get("excludeTotalDataChart") is not None:
                params["excludeTotalDataChart"] = options.get("excludeTotalDataChart")
            if options.get("excludeTotalDataChartBreakdown") is not None:
                params["excludeTotalDataChartBreakdown"] = options.get(
                    "excludeTotalDataChartBreakdown"
                )
            data_type = _data_type_value(options.get("dataType"))
            if data_type:
                params["dataType"] = data_type
        return self._client.get(
            "/overview/fees",
            params=params or None,
        )

    def getOverviewByChain(
        self, chain: str, options: Optional[FeesOverviewOptions] = None
    ) -> FeesOverviewResponse:
        """Get fees overview for a chain."""

        params = {}
        if options:
            if options.get("excludeTotalDataChart") is not None:
                params["excludeTotalDataChart"] = options.get("excludeTotalDataChart")
            if options.get("excludeTotalDataChartBreakdown") is not None:
                params["excludeTotalDataChartBreakdown"] = options.get(
                    "excludeTotalDataChartBreakdown"
                )
            data_type = _data_type_value(options.get("dataType"))
            if data_type:
                params["dataType"] = data_type
        return self._client.get(
            f"/overview/fees/{quote(chain)}",
            params=params or None,
        )

    def getSummary(
        self, protocol: str, options: Optional[FeesSummaryOptions] = None
    ) -> FeesSummaryResponse:
        """Get fees summary for a protocol."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/summary/fees/{quote(protocol)}",
            params=params or None,
        )

    def getChart(self, options: Optional[FeesChartOptions] = None) -> list[ChartDataPoint]:
        """Get historical fees chart."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            "/chart/fees",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getChartByChain(
        self, chain: str, options: Optional[FeesChartOptions] = None
    ) -> list[ChartDataPoint]:
        """Get historical fees chart for a chain."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/chart/fees/chain/{quote(chain)}",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getChartByProtocol(
        self, protocol: str, options: Optional[FeesChartOptions] = None
    ) -> list[ChartDataPoint]:
        """Get historical fees chart for a protocol."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/chart/fees/protocol/{quote(protocol)}",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getChartByProtocolChainBreakdown(
        self, protocol: str, options: Optional[FeesChartOptions] = None
    ) -> list[ChartBreakdownDataPoint]:
        """Get fees chart with protocol chain breakdown."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/chart/fees/protocol/{quote(protocol)}/chain-breakdown",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getChartByProtocolVersionBreakdown(
        self, protocol: str, options: Optional[FeesChartOptions] = None
    ) -> list[ChartBreakdownDataPoint]:
        """Get fees chart with protocol version breakdown."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/chart/fees/protocol/{quote(protocol)}/version-breakdown",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getChartByChainProtocolBreakdown(
        self, chain: str, options: Optional[FeesChartOptions] = None
    ) -> list[ChartBreakdownDataPoint]:
        """Get fees chart with chain protocol breakdown."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/chart/fees/chain/{quote(chain)}/protocol-breakdown",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getChartChainBreakdown(
        self, options: Optional[FeesChartOptions] = None
    ) -> list[ChartBreakdownDataPoint]:
        """Get fees chart with chain breakdown across protocols."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            "/chart/fees/chain-breakdown",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getMetrics(self, options: Optional[FeesChartOptions] = None) -> FeesMetricsResponse:
        """Get fee metrics across protocols."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            "/metrics/fees",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getMetricsByChain(
        self, chain: str, options: Optional[FeesChartOptions] = None
    ) -> FeesMetricsResponse:
        """Get fee metrics for a chain."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/metrics/fees/chain/{quote(chain)}",
            base="v2",
            requires_auth=True,
            params=params or None,
        )

    def getMetricsByProtocol(
        self, protocol: str, options: Optional[FeesChartOptions] = None
    ) -> FeesMetricsByProtocolResponse:
        """Get fee metrics for a protocol."""

        params = {}
        data_type = _data_type_value(options.get("dataType") if options else None)
        if data_type:
            params["dataType"] = data_type
        return self._client.get(
            f"/metrics/fees/protocol/{quote(protocol)}",
            base="v2",
            requires_auth=True,
            params=params or None,
        )
