"""
Metty DeFi Analytics - Main Entry Point
"""

import argparse
from analyzers.liquidity_analyzer import LiquidityAnalyzer

def main():
    parser = argparse.ArgumentParser(description='Metty DeFi Analytics')
    parser.add_argument('--pool', required=True, help='Pool contract address')
    parser.add_argument('--chain', required=True, help='Blockchain network')
    
    args = parser.parse_args()
    
    # Initialize analyzer
    config = {}  # Load from config.py
    analyzer = LiquidityAnalyzer(config)
    
    # Analyze pool
    print(f"Analyzing pool {args.pool} on {args.chain}...")
    analysis = analyzer.analyze_pool(args.pool, args.chain)
    
    # Display results
    print(f"\n{'='*50}")
    print(f"VERDICT: {analysis.verdict}")
    print(f"CONVICTION: {analysis.conviction_score}/100")
    print(f"APY RANGE: {analysis.apy_range[0]:.1f}% - {analysis.apy_range[1]:.1f}%")
    print(f"IL EXPOSURE: {analysis.il_exposure:.1f}%")
    print(f"CAPITAL EFFICIENCY: {analysis.capital_efficiency:.1f}/100")
    print(f"RISK SCORE: {analysis.risk_score:.1f}/100")
    print(f"\nRATIONALE: {analysis.rationale}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()
