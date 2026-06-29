import time
from src.market_simulator import MarketSimulator
from src.alpha_indicators import AlphaIndicators
from src.risk_manager import RiskManager

def main():
    print("⚡ Launching Automated Crypto Algorithmic Trading Pipeline...\n")
    
    # Initialize Core Engines
    exchange = MarketSimulator(initial_price=65000.0)
    risk_unit = RiskManager()
    
    price_history = []
    portfolio = {"USDT": 10000.0, "BTC": 0.0, "position_open": False, "entry_price": 0.0}
    
    print(f"Initial Balance: {portfolio['USDT']} USDT | Assets: {portfolio['BTC']} BTC\n")
    print("--- Streaming Live Exchange Telemetry ---")
    
    for tick in range(1, 8):
        current_price = exchange.get_next_ticker()
        price_history.append(current_price)
        
        # 1. Calculate Analytical Indicators
        sma_3 = AlphaIndicators.calculate_sma(price_history, window=3)
        signal = AlphaIndicators.evaluate_momentum(price_history)
        
        print(f"Tick {tick} | BTC/USDT: ${current_price} | 3-Tick SMA: ${sma_3 if sma_3 else 'Calculating...'}")
        
        # 2. Risk Management Core Evaluation
        if portfolio["position_open"]:
            risk_status = risk_unit.evaluate_open_position(portfolio["entry_price"], current_price, "LONG")
            if "LIQUIDATE" in risk_status:
                usdt_received = portfolio["BTC"] * current_price
                portfolio["USDT"] = round(usdt_received, 2)
                portfolio["BTC"] = 0.0
                portfolio["position_open"] = False
                print(f"🚨 RISK ALARM Triggered -> Closed position via {risk_status} at ${current_price}")
        
        # 3. Alpha Strategy Processing
        elif signal == "BUY_SIGNAL" and not portfolio["position_open"]:
            # Deploy 50% available capital
            capital_to_deploy = portfolio["USDT"] * 0.5
            portfolio["BTC"] = round(capital_to_deploy / current_price, 4)
            portfolio["USDT"] -= capital_to_deploy
            portfolio["entry_price"] = current_price
            portfolio["position_open"] = True
            print(f"🟩 STRATEGY BUY Execution -> Bought {portfolio['BTC']} BTC at ${current_price}")
            
        elif signal == "SELL_SIGNAL" and portfolio["position_open"]:
            usdt_received = portfolio["BTC"] * current_price
            portfolio["USDT"] = round(portfolio["USDT"] + usdt_received, 2)
            portfolio["BTC"] = 0.0
            portfolio["position_open"] = False
            print(f"🟥 STRATEGY SELL Execution -> Sold all BTC holdings at ${current_price}")

    print(f"\n--- Post-Session Trading Audit Ledger ---")
    print(f"Final Cash Balance: {portfolio['USDT']} USDT")
    print(f"Final Asset Hold: {portfolio['BTC']} BTC")

if __name__ == "__main__":
    main()
