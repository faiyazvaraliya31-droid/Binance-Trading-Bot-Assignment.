from client import get_client

def place_market_order(symbol, side, quantity):
    try:
        client = get_client()
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        print(f"Order Successful! Aapne {quantity} {symbol} {side} kiya hai.")
        return order
    except Exception as e:
        print(f"Order nahi lag paya: {e}")

if __name__ == "__main__":
    place_market_order('BTCUSDT', 'BUY', 0.002)
