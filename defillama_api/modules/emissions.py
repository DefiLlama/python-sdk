"""Emissions module implementation."""

import json
from urllib.parse import quote

from ..client import BaseClient
from ..types.emissions import EmissionDetailResponse, EmissionToken


class EmissionsModule:
    """Access emission and unlock schedule data."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getAll(self) -> list[EmissionToken]:
        """Get all tokens with unlock schedules."""

        return self._client.get("/emissions", requires_auth=True)

    def getByProtocol(self, protocol: str) -> EmissionDetailResponse:
        """Get detailed emission data for a protocol."""

        response = self._client.get(
            f"/emission/{quote(protocol)}",
            requires_auth=True,
        )
        body = json.loads(response.get("body", "{}"))
        return {
            "body": body,
            "lastModified": response.get("lastModified"),
        }
