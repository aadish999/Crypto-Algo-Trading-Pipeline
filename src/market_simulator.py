import numpy as np

class MarketSimulator:
    def __init__(self, initial_price=50000.0, volatility=0.002):
        """Initializes market stream parameters for an asset (e.g., BTC/USDT)."""
        self.price = initial_price
        self.volatility = volatility

    def get_next_ticker(self):
        """Generates the next live market price tick using a geometric random walk."""
        price_change_pct = np.random.normal(0, self.volatility)
        self.price *= (1 + price_change_pct)
        return round(self.price, 2)
