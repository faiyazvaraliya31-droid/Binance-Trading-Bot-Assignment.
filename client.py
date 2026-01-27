from binance.client import Client

api_key = "V5ocTOPWVEzmFLNAODKbs2mUexOs8Zsxbtl8S5A2TpEh0CkK3prUNrUafS6wwqcK"
api_secret = "6yvFuTk3i3CgNO8YzUMMAfvb5XFrO44DqChpifY3Lwc122P6hRzyBAx7u0Dv966Y"

def get_client():
    return Client(api_key, api_secret, testnet=True)

if __name__ == "__main__":
    try:
        client = get_client()
        balance = client.futures_account_balance()
        print("Success! Bot Binance se connect ho gaya.")
        print(f"Apka Demo Balance: {balance[1]['balance']} USDT")
    except Exception as e:
        print(f"somthing went wrong: {e}")
