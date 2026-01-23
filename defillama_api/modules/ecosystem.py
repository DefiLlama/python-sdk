"""Ecosystem module implementation."""

from ..client import BaseClient
from ..types.ecosystem import (
    CategoriesResponse,
    Entity,
    ForksResponse,
    Hack,
    OraclesResponse,
    RaisesResponse,
    Treasury,
)


class EcosystemModule:
    """Access ecosystem-level data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getCategories(self) -> CategoriesResponse:
        """Get TVL grouped by protocol category."""

        return self._client.get("/categories", requires_auth=True)

    def getForks(self) -> ForksResponse:
        """Get protocol fork relationships and TVL."""

        return self._client.get("/forks", requires_auth=True)

    def getOracles(self) -> OraclesResponse:
        """Get oracle usage data across protocols."""

        return self._client.get("/oracles", requires_auth=True)

    def getEntities(self) -> list[Entity]:
        """Get entity treasury and holdings data."""

        return self._client.get("/entities", requires_auth=True)

    def getTreasuries(self) -> list[Treasury]:
        """Get protocol treasury balances."""

        return self._client.get("/treasuries", requires_auth=True)

    def getHacks(self) -> list[Hack]:
        """Get security incidents and exploit data."""

        return self._client.get("/hacks", requires_auth=True)

    def getRaises(self) -> RaisesResponse:
        """Get funding rounds database."""

        return self._client.get("/raises", requires_auth=True)
