"""TVL module implementation."""

from typing import List, Optional, Union
from urllib.parse import quote

from ..client import BaseClient
from ..types.tvl import (
    Chain,
    ChainAssetsResponse,
    HistoricalChainTvl,
    HistoricalChainsTvl,
    Protocol,
    ProtocolDetails,
    ProtocolInflowsResponse,
    TokenProtocolHolding,
)


class TvlModule:
    """Access TVL data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getProtocols(self) -> List[Protocol]:
        """Get all protocols with current TVL."""

        return self._client.get("/protocols")

    def getProtocol(self, protocol: str) -> ProtocolDetails:
        """Get detailed protocol information with historical TVL."""

        return self._client.get(f"/protocol/{quote(protocol)}")

    def getTvl(self, protocol: str) -> float:
        """Get current TVL for a protocol."""

        return self._client.get(f"/tvl/{quote(protocol)}")

    def getChains(self) -> List[Chain]:
        """Get current TVL for all chains."""

        return self._client.get("/v2/chains")

    def getHistoricalChainTvl(
        self, chain: Optional[str] = None
    ) -> Union[List[HistoricalChainsTvl], List[HistoricalChainTvl]]:
        """Get historical TVL data for all chains or a specific chain."""

        if chain:
            return self._client.get(f"/v2/historicalChainTvl/{quote(chain)}")
        return self._client.get("/v2/historicalChainTvl")

    def getTokenProtocols(self, symbol: str) -> List[TokenProtocolHolding]:
        """Get protocols that hold a specific token."""

        return self._client.get(
            f"/tokenProtocols/{quote(symbol)}",
            requires_auth=True,
        )

    def getInflows(
        self,
        protocol: str,
        start_timestamp: int,
        end_timestamp: int,
        tokens_to_exclude: Optional[str] = None,
    ) -> ProtocolInflowsResponse:
        """Get token inflows/outflows for a protocol."""

        params = {
            "end": end_timestamp,
            "tokensToExclude": tokens_to_exclude or "",
        }
        return self._client.get(
            f"/inflows/{quote(protocol)}/{start_timestamp}",
            requires_auth=True,
            params=params,
        )

    def getChainAssets(self) -> ChainAssetsResponse:
        """Get asset breakdown for all chains."""

        return self._client.get("/chainAssets", requires_auth=True)
