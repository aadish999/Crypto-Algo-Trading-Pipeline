import numpy as np

class AlphaIndicators:
    @staticmethod
    def calculate_sma(price_history, window):
        """Calculates the Simple Moving Average over a rolling window."""
        if len(price_history) < window:
            return None
        return round(float(np.mean(price_history[-window:])), 2)

    @staticmethod
    def evaluate_momentum(price_history):
        """Evaluates price momentum to detect overbought or oversold cycles."""
        if len(price_history) < 3:
            return "HOLD"
        
        recent_delta = price_history[-1] - price_history[-3]
        if recent_delta > (price_history[-3] * 0.005):
            return "BUY_SIGNAL"
        elif recent_delta < -(price_history[-3] * 0.005):
            return "SELL_SIGNAL"
        return "HOLD"
