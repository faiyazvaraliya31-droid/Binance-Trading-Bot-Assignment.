from order import place_market_order
from client import get_client
import time

def start_bot():
    print("Bot shuru ho raha hai...")
    client = get_client()

    while True:
        try:
            price_info = client.futures_symbol_ticker(symbol='BTCUSDT')
            current_price = float(price_info['price'])
            print(f"BTC ka abhi ka price: {current_price}")

            if current_price < 105000:
                print("Price kam hai! Khareed rahe hain...")
                place_market_order('BTCUSDT', 'BUY', 0.002)
                break
            
            time.sleep(10)
            
        except Exception as e:
            print(f"Bot mein error aaya: {e}")
            break

if __name__ == "__main__":
    start_bot()
