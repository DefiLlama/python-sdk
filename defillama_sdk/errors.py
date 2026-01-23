"""Error types for the DefiLlama SDK."""

from typing import Optional


class DefiLlamaError(Exception):
    """Base error class for DefiLlama SDK errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ApiKeyRequiredError(DefiLlamaError):
    """Raised when a Pro API key is required for an endpoint."""

    def __init__(self, endpoint: str) -> None:
        super().__init__(f"API key required for endpoint: {endpoint}")


class RateLimitError(DefiLlamaError):
    """Raised when the API rate limit is exceeded."""

    def __init__(self, retry_after: Optional[int] = None) -> None:
        super().__init__("Rate limit exceeded")
        self.retry_after = retry_after


class NotFoundError(DefiLlamaError):
    """Raised when a requested resource is not found."""

    def __init__(self, resource: str) -> None:
        super().__init__(f"Resource not found: {resource}")


class ApiError(DefiLlamaError):
    """Raised for non-success API responses."""

    def __init__(self, status_code: int, message: str, response: Optional[object] = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response = response
