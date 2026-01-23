# DefiLlama Python SDK

Official Python SDK for the [DefiLlama API](https://api-docs.defillama.com/). Access DeFi protocol data including TVL, prices, yields, volumes, fees, bridges, and more.

## Installation

```bash
pip install defillama-sdk
```

```bash
uv pip install defillama-sdk
```

## Quick Start

```python
from defillama_sdk import DefiLlama

# Free tier
client = DefiLlama()

# Pro tier (required for premium endpoints)
pro_client = DefiLlama({"api_key": "your-api-key"})

# Get all protocols
protocols = client.tvl.getProtocols()

# Get current token prices
prices = client.prices.getCurrentPrices(
    [
        "ethereum:0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "coingecko:bitcoin",
    ]
)
```

## Configuration

```python
config = {
    "api_key": "your-api-key",
    "timeout": 30000,
}

client = DefiLlama(config)
```

## Modules

- TVL
- Prices
- Stablecoins
- Yields (Pro)
- Volumes
- Fees
- Emissions (Pro)
- Bridges (Pro)
- Ecosystem (Pro)
- ETFs (Pro)
- DAT (Pro)
- Account (Pro)

🔐 = Requires Pro API key

---

## TVL

Total Value Locked data for protocols and chains.

### getProtocols

Get all protocols with current TVL.

```python
protocols = client.tvl.getProtocols()
```

### getProtocol

Get detailed protocol information including historical TVL.

```python
aave = client.tvl.getProtocol("aave")
```

### getTvl

Get only current TVL for a protocol.

```python
tvl = client.tvl.getTvl("uniswap")
```

### getChains

Get current TVL for all chains.

```python
chains = client.tvl.getChains()
```

### getHistoricalChainTvl

Get historical TVL data.

```python
all_history = client.tvl.getHistoricalChainTvl()
eth_history = client.tvl.getHistoricalChainTvl("Ethereum")
```

### getTokenProtocols 🔐

Get protocols holding a specific token.

```python
holders = pro_client.tvl.getTokenProtocols("ETH")
```

### getInflows 🔐

Get token inflows/outflows between timestamps.

```python
inflows = pro_client.tvl.getInflows(
    "lido",
    1704067200,
    1704153600,
    "ETH,USDC",
)
```

### getChainAssets 🔐

Get asset breakdown for all chains.

```python
assets = pro_client.tvl.getChainAssets()
```

---

## Prices

Token price data and historical charts.

### getCurrentPrices

```python
prices = client.prices.getCurrentPrices(
    [
        "ethereum:0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "coingecko:bitcoin",
        "solana:So11111111111111111111111111111111111111112",
    ]
)
```

### getHistoricalPrices

```python
prices = client.prices.getHistoricalPrices(
    1704067200,
    ["ethereum:0xdac17f958d2ee523a2206206994597c13d831ec7"],
)
```

### getBatchHistoricalPrices

```python
prices = client.prices.getBatchHistoricalPrices(
    {
        "ethereum:0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48": [
            1704067200,
            1704153600,
            1704240000,
        ]
    }
)
```

### getChart

```python
chart = client.prices.getChart(
    ["coingecko:ethereum"],
    {"start": 1704067200, "period": "1d", "span": 30},
)
```

### getPercentageChange

```python
change = client.prices.getPercentageChange(
    ["coingecko:bitcoin"],
    {"period": "24h"},
)
```

### getFirstPrices

```python
first = client.prices.getFirstPrices(
    ["ethereum:0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"]
)
```

### getBlockAtTimestamp

```python
block = client.prices.getBlockAtTimestamp("ethereum", 1704067200)
```

---

## Stablecoins

Stablecoin market cap and dominance data.

### getStablecoins

```python
stables = client.stablecoins.getStablecoins(True)
```

### getAllCharts

```python
charts = client.stablecoins.getAllCharts()
```

### getChartsByChain

```python
eth_charts = client.stablecoins.getChartsByChain("Ethereum")
```

### getStablecoin

```python
usdt = client.stablecoins.getStablecoin("1")
```

### getChains

```python
chains = client.stablecoins.getChains()
```

### getPrices

```python
prices = client.stablecoins.getPrices()
```

### getDominance 🔐

```python
dominance = pro_client.stablecoins.getDominance("ethereum", 1)
```

---

## Yields 🔐

Yield farming, lending, staking, and perpetual funding rates.

### getPools

```python
pools = pro_client.yields.getPools()
```

### getPoolsOld

```python
pools = pro_client.yields.getPoolsOld()
```

### getPoolChart

```python
chart = pro_client.yields.getPoolChart("pool-uuid-here")
```

### getBorrowPools

```python
borrow_pools = pro_client.yields.getBorrowPools()
```

### getLendBorrowChart

```python
chart = pro_client.yields.getLendBorrowChart("pool-uuid-here")
```

### getPerps

```python
perps = pro_client.yields.getPerps()
```

### getLsdRates

```python
lsd_rates = pro_client.yields.getLsdRates()
```

---

## Volumes

DEX, options, and derivatives trading volume data.

### getDexOverview

```python
overview = client.volumes.getDexOverview()
overview = client.volumes.getDexOverview(
    {"excludeTotalDataChart": True, "dataType": "dailyVolume"}
)
```

### getDexOverviewByChain

```python
eth_volume = client.volumes.getDexOverviewByChain("Ethereum")
```

### getDexSummary

```python
uniswap = client.volumes.getDexSummary("uniswap")
```

### getOptionsOverview

```python
options = client.volumes.getOptionsOverview()
```

### getOptionsOverviewByChain

```python
eth_options = client.volumes.getOptionsOverviewByChain("Ethereum")
```

### getOptionsSummary

```python
derive = client.volumes.getOptionsSummary("derive")
```

### getDerivativesOverview 🔐

```python
derivatives = pro_client.volumes.getDerivativesOverview()
```

### getDerivativesSummary 🔐

```python
gmx = pro_client.volumes.getDerivativesSummary("gmx")
```

---

## Fees

Protocol fees and revenue data.

### Fee Data Types

```python
from defillama_sdk import FeeDataType

FeeDataType.DAILY_FEES
FeeDataType.DAILY_REVENUE
FeeDataType.DAILY_HOLDERS_REVENUE
FeeDataType.DAILY_SUPPLY_SIDE_REVENUE
FeeDataType.DAILY_BRIBES_REVENUE
FeeDataType.DAILY_TOKEN_TAXES
FeeDataType.DAILY_APP_FEES
FeeDataType.DAILY_APP_REVENUE
FeeDataType.DAILY_EARNINGS
```

### getOverview

```python
fees = client.fees.getOverview()
revenue = client.fees.getOverview({"dataType": FeeDataType.DAILY_REVENUE})
```

### getOverviewByChain

```python
eth_fees = client.fees.getOverviewByChain("Ethereum")
```

### getSummary

```python
uniswap_fees = client.fees.getSummary("uniswap")
```

### getChart 🔐

```python
chart = pro_client.fees.getChart()
eth_chart = pro_client.fees.getChartByChain("Ethereum")
protocol_chart = pro_client.fees.getChartByProtocol("aave")
```

### getChartByProtocolChainBreakdown 🔐

```python
breakdown = pro_client.fees.getChartByProtocolChainBreakdown("aave")
```

### getChartByProtocolVersionBreakdown 🔐

```python
breakdown = pro_client.fees.getChartByProtocolVersionBreakdown("uniswap")
```

### getChartByChainProtocolBreakdown 🔐

```python
breakdown = pro_client.fees.getChartByChainProtocolBreakdown("Ethereum")
```

### getChartChainBreakdown 🔐

```python
breakdown = pro_client.fees.getChartChainBreakdown()
```

### getMetrics 🔐

```python
metrics = pro_client.fees.getMetrics()
chain_metrics = pro_client.fees.getMetricsByChain("Ethereum")
protocol_metrics = pro_client.fees.getMetricsByProtocol("aave")
```

---

## Emissions 🔐

Token unlock schedules and vesting data.

### getAll

```python
emissions = pro_client.emissions.getAll()
```

### getByProtocol

```python
arbitrum = pro_client.emissions.getByProtocol("arbitrum")
```

---

## Bridges 🔐

Cross-chain bridge volume and transaction data.

### getAll

```python
bridges = pro_client.bridges.getAll()
bridges = pro_client.bridges.getAll({"includeChains": True})
```

### getById

```python
bridge = pro_client.bridges.getById(1)
```

### getVolumeByChain

```python
volume = pro_client.bridges.getVolumeByChain("Ethereum")
```

### getDayStats

```python
stats = pro_client.bridges.getDayStats(1704067200, "Ethereum")
```

### getTransactions

```python
txs = pro_client.bridges.getTransactions(
    1,
    {
        "limit": 100,
        "startTimestamp": 1704067200,
        "endTimestamp": 1704153600,
        "sourceChain": "Ethereum",
        "address": "0x...",
    },
)
```

---

## Ecosystem 🔐

Ecosystem-level data.

### getCategories

```python
categories = pro_client.ecosystem.getCategories()
```

### getForks

```python
forks = pro_client.ecosystem.getForks()
```

### getOracles

```python
oracles = pro_client.ecosystem.getOracles()
```

### getEntities

```python
entities = pro_client.ecosystem.getEntities()
```

### getTreasuries

```python
treasuries = pro_client.ecosystem.getTreasuries()
```

### getHacks

```python
hacks = pro_client.ecosystem.getHacks()
```

### getRaises

```python
raises = pro_client.ecosystem.getRaises()
```

---

## ETFs 🔐

Bitcoin and Ethereum ETF data.

### getOverview

```python
btc_etfs = pro_client.etfs.getOverview()
```

### getOverviewEth

```python
eth_etfs = pro_client.etfs.getOverviewEth()
```

### getHistory

```python
history = pro_client.etfs.getHistory()
```

### getHistoryEth

```python
history_eth = pro_client.etfs.getHistoryEth()
```

### getFdvPerformance

```python
perf = pro_client.etfs.getFdvPerformance("30")
```

---

## DAT 🔐

Digital Asset Treasury data and institutional holdings.

### getInstitutions

```python
data = pro_client.dat.getInstitutions()
```

### getInstitution

```python
mstr = pro_client.dat.getInstitution("MSTR")
```

---

## Account 🔐

API usage management.

### getUsage

```python
usage = pro_client.account.getUsage()
```

---

## Error Handling

```python
from defillama_sdk import ApiKeyRequiredError, RateLimitError, NotFoundError, ApiError

try:
    data = pro_client.yields.getPools()
except ApiKeyRequiredError:
    print("Pro API key required for this endpoint")
except RateLimitError as exc:
    print(f"Rate limited. Retry after {exc.retry_after} seconds")
except NotFoundError:
    print("Resource not found")
except ApiError as exc:
    print(f"API error: {exc.status_code}")
```

---

## Type Exports

All types are available from `defillama_sdk.types`, and are re-exported at the top level:

```python
from defillama_sdk import Protocol, CoinPricesResponse, Stablecoin, YieldPool
```

---

## Constants

```python
from defillama_sdk import AdapterType, FeeDataType, VolumeDataType

AdapterType.DEXS
VolumeDataType.DAILY_VOLUME
FeeDataType.DAILY_FEES
```

---

## Requirements

- Python >= 3.9

## License

MIT
