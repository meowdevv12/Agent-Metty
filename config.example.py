"""
Configuration template for Metty DeFi Analytics
Copy this file to config.py and fill in your API keys
"""

# RPC Endpoints
ETHEREUM_RPC = "https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY"
ARBITRUM_RPC = "https://arb-mainnet.g.alchemy.com/v2/YOUR_API_KEY"
BASE_RPC = "https://base-mainnet.g.alchemy.com/v2/YOUR_API_KEY"
SOLANA_RPC = "https://api.mainnet-beta.solana.com"

# API Keys
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_KEY"
COINGECKO_API_KEY = "YOUR_COINGECKO_KEY"

# Analysis Parameters
MIN_TVL_THRESHOLD = 100000  # Minimum TVL in USD
MAX_RISK_SCORE = 70  # Maximum acceptable risk score
CONVICTION_THRESHOLD = 75  # Minimum conviction for DEPLOY

# Database
DATABASE_URL = "sqlite:///metty.db"
