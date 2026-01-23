"""DAT module implementation."""

from urllib.parse import quote

from ..client import BaseClient
from ..types.dat import DatInstitutionResponse, DatInstitutionsResponse


class DatModule:
    """Access Digital Asset Treasury data from DefiLlama."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getInstitutions(self) -> DatInstitutionsResponse:
        """Get comprehensive DAT data for all institutions."""

        return self._client.get(
            "/dat/institutions",
            requires_auth=True,
            api_namespace="",
        )

    def getInstitution(self, symbol: str) -> DatInstitutionResponse:
        """Get detailed DAT data for a specific institution."""

        return self._client.get(
            f"/dat/institutions/{quote(symbol)}",
            requires_auth=True,
            api_namespace="",
        )
