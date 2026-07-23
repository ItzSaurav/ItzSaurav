import numpy as np
import pandas as pd

def simulate_bitcoin_prices(days=60, initial_price=60000, volatility=0.04, mu=0.001):
    prices = [initial_price]
    for _ in range(1, days):
        # Geometric Brownian Motion step for realistic volatility
        returns = np.random.normal(loc=mu, scale=volatility)
        prices.append(prices[-1] * (1 + returns))

    df = pd.DataFrame({
        'Day': range(1, days + 1),
        'Price': prices
    })
    return df

def calculate_moving_averages(df):
    df['MA7'] = df['Price'].rolling(window=7).mean()
    df['MA30'] = df['Price'].rolling(window=30).mean()
    return df

def run_trading_simulation(df, initial_cash=10000):
    cash = initial_cash
    btc_held = 0

    print("--- Trading Ledger ---")
    trades_executed = 0

    for i in range(len(df)):
        day = df.loc[i, 'Day']
        price = df.loc[i, 'Price']
        ma7 = df.loc[i, 'MA7']
        ma30 = df.loc[i, 'MA30']

        # We need both MAs to make a decision
        if pd.isna(ma30) or pd.isna(ma7):
            continue

        # Get yesterday's MAs to detect crossovers
        if i == 0 or pd.isna(df.loc[i-1, 'MA30']):
            continue

        prev_ma7 = df.loc[i-1, 'MA7']
        prev_ma30 = df.loc[i-1, 'MA30']

        # Golden Cross: MA7 crosses above MA30
        if prev_ma7 <= prev_ma30 and ma7 > ma30:
            if cash > 0:
                btc_bought = cash / price
                print(f"Day {day:02d}: Golden Cross (Buy Signal)! Bought {btc_bought:.6f} BTC at ${price:.2f}")
                btc_held += btc_bought
                cash = 0
                trades_executed += 1

        # Death Cross (Sell signal): MA7 crosses below MA30
        elif prev_ma7 >= prev_ma30 and ma7 < ma30:
            if btc_held > 0:
                cash_earned = btc_held * price
                print(f"Day {day:02d}: Death Cross (Sell Signal)! Sold {btc_held:.6f} BTC at ${price:.2f}")
                cash += cash_earned
                btc_held = 0
                trades_executed += 1

    if trades_executed == 0:
        print("No trades executed during this period (no crossovers detected).")

    final_price = df['Price'].iloc[-1]
    final_portfolio_value = cash + (btc_held * final_price)

    print("\n--- Final Portfolio Performance ---")
    print(f"Initial Cash: ${initial_cash:.2f}")
    print(f"Final Cash: ${cash:.2f}")
    print(f"Final BTC Held: {btc_held:.6f} BTC (Value: ${btc_held * final_price:.2f})")
    print(f"Total Portfolio Value: ${final_portfolio_value:.2f}")
    profit = final_portfolio_value - initial_cash
    print(f"Total Profit/Loss: ${profit:.2f} ({(profit/initial_cash) * 100:.2f}%)")

if __name__ == "__main__":
    df = simulate_bitcoin_prices(60)
    df = calculate_moving_averages(df)
    run_trading_simulation(df)
