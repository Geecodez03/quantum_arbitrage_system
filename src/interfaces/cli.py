import argparse
from typing import List
from ..core.analysis.arbitrage import ArbitrageEngine

# Ensure ArbitrageOpportunity is defined in arbitrage module or remove its usage
from ..core.execution.router import OrderRouter


class TradingCLI:
    def __init__(self):
        self.arb_engine: ArbitrageEngine = ArbitrageEngine()
        self.router: OrderRouter = OrderRouter()

    def live_mode(self) -> None:
        """Real-time trading interface"""
        print("Starting live trading mode...")
        try:
            while True:
                opportunities: List[ArbitrageOpportunity] = (
                    self.arb_engine.find_opportunities()
                )
                if opportunities:
                    # process opportunities here, e.g., execute orders
                    pass
                    # execution logic
        except KeyboardInterrupt:
            print("\nExiting live mode...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["live", "backtest"], default="live")
    args = parser.parse_args()

    cli = TradingCLI()
    if args.mode == "live":
        cli.live_mode()
    else:
        print("Backtest mode not yet implemented")
