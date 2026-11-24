"""The free hosts never read an API key, so a client with a key must send every request to pro-api.

Run: python -m unittest discover tests
"""

import re
import unittest
from unittest import mock

from defillama_sdk import DefiLlama

CALLS = {
    "tvl.getProtocols": lambda c: c.tvl.getProtocols(),
    "prices.getCurrentPrices": lambda c: c.prices.getCurrentPrices(["coingecko:ethereum"]),
    "stablecoins.getStablecoins": lambda c: c.stablecoins.getStablecoins(),
    "fees.getOverview": lambda c: c.fees.getOverview(),
    "volumes.getDexOverview": lambda c: c.volumes.getDexOverview(),
}


def url_for(config, call):
    """Return the first URL the call requests, without touching the network."""

    response = mock.Mock(ok=True)
    response.json.return_value = {}
    with mock.patch("defillama_sdk.client.requests.get", return_value=response) as get:
        try:
            call(DefiLlama(config))
        except Exception:
            pass
    return get.call_args[0][0]


class KeyRoutingTest(unittest.TestCase):
    def test_keyed_client_uses_pro_api(self):
        for name, call in CALLS.items():
            with self.subTest(name):
                self.assertRegex(url_for({"api_key": "test-key"}, call), r"^https://pro-api\.llama\.fi/test-key/")

    def test_keyless_client_stays_on_free_hosts(self):
        for name, call in CALLS.items():
            with self.subTest(name):
                self.assertRegex(url_for({}, call), r"^https://(api|coins|stablecoins)\.llama\.fi/")

    def test_free_paths_get_their_pro_prefix(self):
        self.assertEqual(url_for({"api_key": "k"}, CALLS["tvl.getProtocols"]), "https://pro-api.llama.fi/k/api/protocols")
        self.assertTrue(
            re.match(r"^https://pro-api\.llama\.fi/k/coins/prices/current/", url_for({"api_key": "k"}, CALLS["prices.getCurrentPrices"]))
        )
        self.assertEqual(
            url_for({"api_key": "k"}, CALLS["stablecoins.getStablecoins"]), "https://pro-api.llama.fi/k/stablecoins/stablecoins"
        )


if __name__ == "__main__":
    unittest.main()
