import time
from config import TRACKED_COINS, UPDATE_INTERVAL
from services.coingecko import get_prices

def main():
    while True:
        prices = get_prices(TRACKED_COINS)
        print("💰 Актуальные цены:")
        for coin, price in prices.items():
            print(f"{coin.capitalize()}: ${price}")
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
