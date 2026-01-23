"""HTTP client for the DefiLlama API."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Literal, TypedDict

import requests

from .errors import ApiError, ApiKeyRequiredError, NotFoundError, RateLimitError


class DefiLlamaConfig(TypedDict, total=False):
    api_key: str
    apiKey: str
    timeout: int


BaseUrl = Literal["main", "v2", "bridges", "coins", "stablecoins"]

BASE_URLS: Dict[str, str] = {
    "main": "https://api.llama.fi",
    "v2": "https://api.llama.fi/v2",
    "pro": "https://pro-api.llama.fi",
    "bridges": "https://bridges.llama.fi",
    "coins": "https://coins.llama.fi",
    "stablecoins": "https://stablecoins.llama.fi",
}


class BaseClient:
    """Low-level HTTP client used by all modules."""

    def __init__(self, config: Optional[Mapping[str, Any]] = None) -> None:
        config = config or {}
        api_key = None
        if "api_key" in config:
            api_key = config.get("api_key")
        elif "apiKey" in config:
            api_key = config.get("apiKey")
        self._api_key = api_key
        timeout_ms = config.get("timeout", 30000)
        self._timeout = timeout_ms / 1000.0

    @property
    def has_api_key(self) -> bool:
        """Return True when a Pro API key is configured."""

        return bool(self._api_key)

    @property
    def timeout(self) -> float:
        """Return the configured request timeout in seconds."""

        return self._timeout

    def get_api_key(self) -> Optional[str]:
        """Return the configured API key, if any."""

        return self._api_key

    def _build_url(
        self,
        endpoint: str,
        requires_auth: bool,
        base: BaseUrl = "main",
        api_namespace: str = "api",
    ) -> str:
        if base == "v2":
            if not self._api_key:
                raise ApiKeyRequiredError(endpoint)
            return f"{BASE_URLS['pro']}/{self._api_key}/api/v2{endpoint}"
        if base == "bridges":
            if not self._api_key:
                raise ApiKeyRequiredError(endpoint)
            return f"{BASE_URLS['pro']}/{self._api_key}/bridges{endpoint}"
        if base == "coins":
            return f"{BASE_URLS['coins']}{endpoint}"
        if base == "stablecoins":
            return f"{BASE_URLS['stablecoins']}{endpoint}"
        if requires_auth:
            if not self._api_key:
                raise ApiKeyRequiredError(endpoint)
            namespace = f"/{api_namespace}" if api_namespace else ""
            return f"{BASE_URLS['pro']}/{self._api_key}{namespace}{endpoint}"
        return f"{BASE_URLS['main']}{endpoint}"

    def _handle_response(self, response: requests.Response, endpoint: str) -> Any:
        if response.ok:
            return response.json()
        text = response.text
        if response.status_code == 404:
            raise NotFoundError(endpoint)
        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            retry_value = int(retry_after) if retry_after and retry_after.isdigit() else None
            raise RateLimitError(retry_value)
        try:
            error_body = response.json()
        except ValueError:
            error_body = text
        raise ApiError(
            response.status_code,
            f"API request failed: {response.reason}",
            error_body,
        )

    def _filter_params(self, params: Optional[Mapping[str, Any]]) -> Optional[Dict[str, Any]]:
        if not params:
            return None
        filtered: Dict[str, Any] = {}
        for key, value in params.items():
            if value is not None:
                filtered[key] = value
        return filtered or None

    def get(
        self,
        endpoint: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        requires_auth: bool = False,
        base: BaseUrl = "main",
        api_namespace: str = "api",
    ) -> Any:
        """Perform a GET request and return parsed JSON."""

        url = self._build_url(endpoint, requires_auth, base, api_namespace)
        response = requests.get(
            url,
            params=self._filter_params(params),
            timeout=self._timeout,
            headers={"Accept": "application/json"},
        )
        return self._handle_response(response, endpoint)

    def post(
        self,
        endpoint: str,
        body: Any,
        *,
        requires_auth: bool = False,
        base: BaseUrl = "main",
        api_namespace: str = "api",
    ) -> Any:
        """Perform a POST request and return parsed JSON."""

        url = self._build_url(endpoint, requires_auth, base, api_namespace)
        response = requests.post(
            url,
            json=body,
            timeout=self._timeout,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        return self._handle_response(response, endpoint)
