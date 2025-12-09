Elite cross-chain liquidity analysis and pool optimization engine
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Overview

Metty is an institutional-grade DeFi liquidity intelligence platform that analyzes pools across Web3 protocols and delivers actionable **DEPLOY / MONITOR / EXIT** verdicts.

### Key Features

- **40+ Liquidity Metrics**: TVL, volume, fee APY, IL exposure, Sharpe ratio, capital efficiency
- **Multi-Chain Support**: Ethereum, Solana, Arbitrum, Base, and more
- **Risk Assessment**: Smart contract analysis, oracle risks, governance quality
- **Arbitrage Detection**: Cross-chain opportunity identification
- **Portfolio Optimization**: Optimal allocation and rebalancing strategies

## Quick Start
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/metty-defi-analytics.git
cd metty-defi-analytics

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp config.example.py config.py
# Edit config.py with your RPC endpoints

# Run analysis
python src/main.py --pool 0x1234... --chain ethereum
```

## Architecture
metty-defi-analytics/
├── src/
│   ├── analyzers/       # Core analysis engines
│   ├── connectors/      # Blockchain connectors
│   ├── models/          # Data models
│   ├── strategies/      # Trading strategies
│   └── utils/           # Helper functions
├── tests/               # Unit tests
├── docs/                # Documentation
└── scripts/             # Deployment scripts
## Supported Protocols

- **Ethereum**: Uniswap V2/V3, Curve, Balancer
- **Solana**: Meteora, Raydium, Orca
- **Arbitrum**: Camelot, GMX
- **Base**: Aerodrome, BaseSwap

## Documentation

See [docs/](docs/) folder for detailed documentation.

## License

MIT License - see [LICENSE](LICENSE) for details.
