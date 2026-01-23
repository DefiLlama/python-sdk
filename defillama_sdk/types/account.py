"""Account type definitions."""

from typing import TypedDict


class UsageResponse(TypedDict):
    creditsLeft: int


__all__ = ["UsageResponse"]
