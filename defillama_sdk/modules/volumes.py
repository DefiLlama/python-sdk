"""Volumes module implementation."""

from typing import Optional
from urllib.parse import quote

from ..client import BaseClient
from ..types.volumes import (
    DexOverviewOptions,
    DexOverviewResponse,
    DexSummaryOptions,
    DexSummaryResponse,
    DerivativesOverviewResponse,
    DerivativesSummaryResponse,
    OptionsOverviewOptions,
    OptionsOverviewResponse,
    OptionsSummaryResponse,
)


class VolumesModule:
    """Access volume data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getDexOverview(
        self, options: Optional[DexOverviewOptions] = None
    ) -> DexOverviewResponse:
        """Get overview of DEX volume data."""

        params = {}
        if options:
            if options.get("excludeTotalDataChart") is not None:
                params["excludeTotalDataChart"] = options.get("excludeTotalDataChart")
            if options.get("dataType"):
                params["dataType"] = options.get("dataType")
        params["excludeTotalDataChartBreakdown"] = not (
            options and options.get("excludeTotalDataChartBreakdown") is False
        )
        return self._client.get(
            "/overview/dexs",
            params=params or None,
        )

    def getDexOverviewByChain(
        self, chain: str, options: Optional[DexOverviewOptions] = None
    ) -> DexOverviewResponse:
        """Get DEX volume overview for a chain."""

        params = {}
        if options:
            if options.get("excludeTotalDataChart") is not None:
                params["excludeTotalDataChart"] = options.get("excludeTotalDataChart")
        params["excludeTotalDataChartBreakdown"] = not (
            options and options.get("excludeTotalDataChartBreakdown") is False
        )
        return self._client.get(
            f"/overview/dexs/{quote(chain)}",
            params=params or None,
        )

    def getDexSummary(
        self, protocol: str, options: Optional[DexSummaryOptions] = None
    ) -> DexSummaryResponse:
        """Get DEX volume summary for a protocol."""

        params = {}
        if options and options.get("dataType"):
            params["dataType"] = options.get("dataType")
        return self._client.get(
            f"/summary/dexs/{quote(protocol)}",
            params=params or None,
        )

    def getOptionsOverview(
        self, options: Optional[OptionsOverviewOptions] = None
    ) -> OptionsOverviewResponse:
        """Get options volume overview."""

        params = {}
        if options:
            if options.get("excludeTotalDataChart") is not None:
                params["excludeTotalDataChart"] = options.get("excludeTotalDataChart")
        params["excludeTotalDataChartBreakdown"] = not (
            options and options.get("excludeTotalDataChartBreakdown") is False
        )
        return self._client.get(
            "/overview/options",
            params=params or None,
        )

    def getOptionsOverviewByChain(self, chain: str) -> OptionsOverviewResponse:
        """Get options volume for a chain."""

        return self._client.get(f"/overview/options/{quote(chain)}")

    def getOptionsSummary(self, protocol: str) -> OptionsSummaryResponse:
        """Get options volume summary for a protocol."""

        return self._client.get(f"/summary/options/{quote(protocol)}")

    def getDerivativesOverview(self) -> DerivativesOverviewResponse:
        """Get derivatives volume overview."""

        return self._client.get("/overview/derivatives", requires_auth=True)

    def getDerivativesSummary(self, protocol: str) -> DerivativesSummaryResponse:
        """Get derivatives volume summary for a protocol."""

        return self._client.get(
            f"/summary/derivatives/{quote(protocol)}",
            requires_auth=True,
        )
