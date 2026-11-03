"""Yields module implementation."""

import warnings
from typing import List, Optional
from urllib.parse import quote

from ..client import BaseClient
from ..types.yields import (
    BorrowMarketHistoryResponse,
    BorrowMarketResponse,
    BorrowMarketsResponse,
    BorrowPoolsResponse,
    EarnHistoryResponse,
    EarnPoolResponse,
    EarnQueryParams,
    EarnQueryResponse,
    EarnResponse,
    LendBorrowChartResponse,
    LsdRate,
    PerpsResponse,
    YieldChartResponse,
    YieldHistoryRange,
    YieldPoolsOldResponse,
    YieldPoolsResponse,
)


class YieldsModule:
    """Access yield data from DefiLlama.

    The v1 methods (`getPools`, `getPoolChart`, `getBorrowPools`, ...) are deprecated and
    served from `/yields/v1/*` compatibility routes. Use the v2 methods below.

    Example::

        client = DefiLlama({"api_key": "your-api-key"})

        # All earn pools
        pools = client.yields.getEarn()["data"]

        # Filtered + paginated earn pools (chain/protocol are slugs)
        res = client.yields.queryEarn(
            {"chain": ["ethereum", "arbitrum"], "stablecoin": True, "min_tvl": 1_000_000}
        )
        data, pagination = res["data"], res["pagination"]

        # Daily history for one pool
        history = client.yields.getEarnHistory("747c1d2a-c668-4682-b9f9-296708a3dd90", "30d")["data"]

        # Borrow markets
        markets = client.yields.getBorrowMarkets()["data"]

        # Perpetual funding rates
        perps = client.yields.getPerpFundingRates()
    """

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getPools(self) -> YieldPoolsResponse:
        """Get all yield pools with current APY.

        Deprecated: use `getEarn` (or `queryEarn` to filter server-side).
        Served from the `/yields/v1/pools` compatibility route, which returns the
        `getPoolsOld` superset (extra keys such as `pool_old`, `poolTokenAddress`, `url`).
        Fields v2 does not compute (il7d, apyBase7d, apyBaseInception, mu, sigma, count,
        outlier, predictions.*) are always null.
        """

        warnings.warn(
            "getPools is deprecated: use getEarn (or queryEarn to filter server-side).",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._client.get(
            "/v1/pools",
            requires_auth=True,
            api_namespace="yields",
        )

    def getPoolsOld(self) -> YieldPoolsOldResponse:
        """Get yield pools in legacy format.

        Deprecated: use `getEarn`; v1 `pool_old` is v2 `pool_key`.
        Served from the `/yields/v1/pools` compatibility route (same response as `getPools`).
        """

        warnings.warn(
            "getPoolsOld is deprecated: use getEarn; v1 pool_old is v2 pool_key.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._client.get(
            "/v1/pools",
            requires_auth=True,
            api_namespace="yields",
        )

    def getPoolChart(self, pool: str) -> YieldChartResponse:
        """Get historical APY and TVL for a pool.

        Deprecated: use `getEarnHistory`. Served from `/yields/v1/chart/{pool}`.
        """

        warnings.warn(
            "getPoolChart is deprecated: use getEarnHistory.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._client.get(
            f"/v1/chart/{quote(pool)}",
            requires_auth=True,
            api_namespace="yields",
        )

    def getBorrowPools(self) -> BorrowPoolsResponse:
        """Get lending/borrowing pools.

        Deprecated: use `getBorrowMarkets`. Served from `/yields/v1/poolsBorrow`.
        """

        warnings.warn(
            "getBorrowPools is deprecated: use getBorrowMarkets.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._client.get(
            "/v1/poolsBorrow",
            requires_auth=True,
            api_namespace="yields",
        )

    def getLendBorrowChart(self, pool: str) -> LendBorrowChartResponse:
        """Get historical lend/borrow rates.

        Deprecated: use `getBorrowMarketHistory` (borrow side) plus
        `getEarnHistory` (supply side). Served from `/yields/v1/chartLendBorrow/{pool}`.
        """

        warnings.warn(
            "getLendBorrowChart is deprecated: use getBorrowMarketHistory (borrow side) "
            "plus getEarnHistory (supply side).",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._client.get(
            f"/v1/chartLendBorrow/{quote(pool)}",
            requires_auth=True,
            api_namespace="yields",
        )

    def getPerps(self) -> PerpsResponse:
        """Get perpetual futures funding rates.

        Deprecated: use `getPerpFundingRates`; this is an alias for it.
        Same response shape and markets as the old `/yields/perps`, but `perp_id`
        values differ: match markets on `marketplace` + `market`.
        """

        warnings.warn(
            "getPerps is deprecated: use getPerpFundingRates; this is an alias for it.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.getPerpFundingRates()

    def getLsdRates(self) -> List[LsdRate]:
        """Get liquid staking derivative rates.

        Deprecated: use `getLstRates`; this is an alias for it.
        """

        warnings.warn(
            "getLsdRates is deprecated: use getLstRates; this is an alias for it.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.getLstRates()

    def getEarn(self) -> EarnResponse:
        """Get all earn pools. Replaces `getPools`.

        Changes from v1: `protocol` is a display name (no project slug); lending
        `tvl_usd` is total supplied; APY is nested (`apy.current|avg_7d|avg_30d.{base,reward,total}`);
        tokens are objects; only pools with at least $10K supplied are listed.

        Example::

            data = client.yields.getEarn()["data"]
            top = sorted(
                (p for p in data if p["apy"]["current"]["total"] is not None),
                key=lambda p: p["apy"]["current"]["total"] or 0,
                reverse=True,
            )[:10]
        """

        return self._client.get(
            "/v2/earn",
            requires_auth=True,
            api_namespace="yields",
        )

    def queryEarn(self, params: Optional[EarnQueryParams] = None) -> EarnQueryResponse:
        """Filter and paginate earn pools server-side.

        Rows have the same shape as `getEarn` and are sorted by TVL descending.

        `chain` and `protocol` are slugs (e.g. "ethereum", "aave-v3"), up to 20 values each.
        Responses only carry display names, not slugs.

        Example::

            res = client.yields.queryEarn(
                {"protocol": "aave-v3", "stablecoin": True, "limit": 50, "page": 2}
            )
            data, pagination = res["data"], res["pagination"]
        """

        # Lists go out as repeated keys (chain=a&chain=b); bools as "true"/"false" like the TS SDK.
        query = {k: str(v).lower() if isinstance(v, bool) else v for k, v in (params or {}).items()}
        return self._client.get(
            "/v2/earn/query",
            params=query,
            requires_auth=True,
            api_namespace="yields",
        )

    def getEarnPool(self, id: str) -> EarnPoolResponse:
        """Get one earn pool with holder detail and which history series exist.

        Holder detail is the top 10 holders and holder count changes.

        Args:
            id: Pool UUID (same id as v1 `pool`)

        Raises:
            NotFoundError: if the pool is not in v2
        """

        return self._client.get(
            f"/v2/earn/{quote(id)}",
            requires_auth=True,
            api_namespace="yields",
        )

    def getEarnHistory(self, id: str, range: Optional[YieldHistoryRange] = None) -> EarnHistoryResponse:
        """Get daily TVL/APY history for an earn pool. Replaces `getPoolChart`.

        Changes from v1: one point per day (`date`, YYYY-MM-DD) with nested
        `apy.avg_1d|avg_7d|avg_30d`; lending `tvl_usd` is total supplied.

        Args:
            id: Pool UUID
            range: "30d", "90d" or "max" (server default: "max")

        Raises:
            NotFoundError: if the pool is not in v2
        """

        return self._client.get(
            f"/v2/earn/{quote(id)}/history",
            params={"range": range},
            requires_auth=True,
            api_namespace="yields",
        )

    def getBorrowMarkets(self) -> BorrowMarketsResponse:
        """Get all borrow markets. Replaces `getBorrowPools`.

        Changes from v1: `protocol` is a display name (no project slug); supply and
        borrow APY are nested (`supply_apy`, `borrow_cost_apy`); tokens are objects
        (`collateral_token`, `borrow_token`).
        """

        return self._client.get(
            "/v2/borrow/markets",
            requires_auth=True,
            api_namespace="yields",
        )

    def getBorrowMarket(self, id: str) -> BorrowMarketResponse:
        """Get one borrow market and which history series exist.

        Args:
            id: Pool UUID

        Raises:
            NotFoundError: if the market is not in v2
        """

        return self._client.get(
            f"/v2/borrow/markets/{quote(id)}",
            requires_auth=True,
            api_namespace="yields",
        )

    def getBorrowMarketHistory(
        self, id: str, range: Optional[YieldHistoryRange] = None
    ) -> BorrowMarketHistoryResponse:
        """Get daily borrow-side history for a market.

        Together with `getEarnHistory` (supply side, same id) this replaces `getLendBorrowChart`.

        Args:
            id: Pool UUID
            range: "30d", "90d" or "max" (server default: "max")

        Raises:
            NotFoundError: if the market is not in v2
        """

        return self._client.get(
            f"/v2/borrow/markets/{quote(id)}/history",
            params={"range": range},
            requires_auth=True,
            api_namespace="yields",
        )

    def getLstRates(self) -> List[LsdRate]:
        """Get liquid staking token (LST) exchange rates and peg data.

        Returns:
            LST tokens with expected/market rates and ETH peg deviation

        Example::

            rates = client.yields.getLstRates()
            depegged = [l for l in rates if abs(l.get("ethPeg") or 0) > 1]
        """

        return self._client.get("/lstRates", requires_auth=True)

    def getPerpFundingRates(self) -> PerpsResponse:
        """Get perpetual futures funding rates, open interest and index price.

        Covers Binance and OKX markets, with 7d/30d average and sum of settled funding rates.

        Example::

            data = client.yields.getPerpFundingRates()["data"]
            positive_funding = [p for p in data if (p.get("fundingRate") or 0) > 0]
        """

        return self._client.get("/perpFundingRates", requires_auth=True)
