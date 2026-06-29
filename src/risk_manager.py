class RiskManager:
    def __init__(self, stop_loss_pct=0.01, take_profit_pct=0.02):
        self.sl_pct = stop_loss_pct
        self.tp_pct = take_profit_pct

    def evaluate_open_position(self, entry_price, current_price, position_type):
        """Enforces strict safety rules to manage open portfolio risk."""
        if position_type == "LONG":
            # Calculate thresholds
            stop_loss_price = entry_price * (1 - self.sl_pct)
            take_profit_price = entry_price * (1 + self.tp_pct)
            
            if current_price <= stop_loss_price:
                return "LIQUIDATE_STOP_LOSS"
            if current_price >= take_profit_price:
                return "LIQUIDATE_TAKE_PROFIT"
                
        return "RUNNING"
