"""Yields module implementation."""

from typing import List
from urllib.parse import quote

from ..client import BaseClient
from ..types.yields import (
    BorrowPoolsResponse,
    LendBorrowChartResponse,
    LsdRate,
    PerpsResponse,
    YieldChartResponse,
    YieldPoolsOldResponse,
    YieldPoolsResponse,
)


class YieldsModule:
    """Access yield data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getPools(self) -> YieldPoolsResponse:
        """Get all yield pools with current APY."""

        return self._client.get(
            "/pools",
            requires_auth=True,
            api_namespace="yields",
        )

    def getPoolsOld(self) -> YieldPoolsOldResponse:
        """Get yield pools in legacy format."""

        return self._client.get(
            "/poolsOld",
            requires_auth=True,
            api_namespace="yields",
        )

    def getPoolChart(self, pool: str) -> YieldChartResponse:
        """Get historical APY and TVL for a pool."""

        return self._client.get(
            f"/chart/{quote(pool)}",
            requires_auth=True,
            api_namespace="yields",
        )

    def getBorrowPools(self) -> BorrowPoolsResponse:
        """Get lending/borrowing pools."""

        return self._client.get(
            "/poolsBorrow",
            requires_auth=True,
            api_namespace="yields",
        )

    def getLendBorrowChart(self, pool: str) -> LendBorrowChartResponse:
        """Get historical lend/borrow rates."""

        return self._client.get(
            f"/chartLendBorrow/{quote(pool)}",
            requires_auth=True,
            api_namespace="yields",
        )

    def getPerps(self) -> PerpsResponse:
        """Get perpetual futures funding rates."""

        return self._client.get(
            "/perps",
            requires_auth=True,
            api_namespace="yields",
        )

    def getLsdRates(self) -> List[LsdRate]:
        """Get liquid staking derivative rates."""

        return self._client.get(
            "/lsdRates",
            requires_auth=True,
            api_namespace="yields",
        )
