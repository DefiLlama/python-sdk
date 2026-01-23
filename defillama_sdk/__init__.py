"""DefiLlama Python SDK entry point."""

from typing import Optional

from .client import BaseClient, DefiLlamaConfig
from .errors import ApiError, ApiKeyRequiredError, DefiLlamaError, NotFoundError, RateLimitError
from .modules.account import AccountModule
from .modules.bridges import BridgesModule
from .modules.dat import DatModule
from .modules.ecosystem import EcosystemModule
from .modules.emissions import EmissionsModule
from .modules.etfs import EtfsModule
from .modules.fees import FeesModule
from .modules.prices import PricesModule
from .modules.stablecoins import StablecoinsModule
from .modules.tvl import TvlModule
from .modules.volumes import VolumesModule
from .modules.yields import YieldsModule


class DefiLlama:
    """DefiLlama API client for accessing DeFi data."""

    def __init__(self, config: Optional[DefiLlamaConfig] = None) -> None:
        """Create a new DefiLlama client."""

        self._client = BaseClient(config)
        self.tvl = TvlModule(self._client)
        self.prices = PricesModule(self._client)
        self.stablecoins = StablecoinsModule(self._client)
        self.yields = YieldsModule(self._client)
        self.volumes = VolumesModule(self._client)
        self.fees = FeesModule(self._client)
        self.emissions = EmissionsModule(self._client)
        self.bridges = BridgesModule(self._client)
        self.ecosystem = EcosystemModule(self._client)
        self.etfs = EtfsModule(self._client)
        self.dat = DatModule(self._client)
        self.account = AccountModule(self._client)

    @property
    def isPro(self) -> bool:
        """Return True when the client has a Pro API key configured."""

        return self._client.has_api_key


__all__ = [
    "DefiLlama",
    "DefiLlamaConfig",
    "ApiError",
    "ApiKeyRequiredError",
    "DefiLlamaError",
    "NotFoundError",
    "RateLimitError",
    "TvlModule",
    "PricesModule",
    "StablecoinsModule",
    "YieldsModule",
    "VolumesModule",
    "FeesModule",
    "EmissionsModule",
    "BridgesModule",
    "EcosystemModule",
    "EtfsModule",
    "DatModule",
    "AccountModule",
]

from .constants import *
from .types import *
