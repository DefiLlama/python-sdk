"""Account module implementation."""

import requests

from ..client import BaseClient
from ..errors import ApiKeyRequiredError, ApiError
from ..types.account import UsageResponse


class AccountModule:
    """Access API account and usage data."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def getUsage(self) -> UsageResponse:
        """Get API usage statistics for the configured key."""

        api_key = self._client.get_api_key()
        if not api_key:
            raise ApiKeyRequiredError("/usage")
        response = requests.get(
            f"https://pro-api.llama.fi/usage/{api_key}",
            headers={"Accept": "application/json"},
            timeout=self._client.timeout,
        )
        if not response.ok:
            raise ApiError(response.status_code, f"Failed to fetch usage: {response.reason}")
        return response.json()
