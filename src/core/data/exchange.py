# Unified market data fetcher (WS + REST)
from dataclasses import dataclass
from typing import Dict


@dataclass
class MarketData:
    symbol: str
    bid: float
    ask: float
    timestamp: int


class ExchangeAPI:
    def __init__(self):
        self.rate_limit = 100  # requests per minute
        self.connection_pool = []

    async def get_orderbook(self, symbol: str) -> Dict[str, float]:
        """Fetch order book with depth"""
        # Example implementation returning mock data using the symbol
        return {"bid": 100.0, "ask": 101.0}
