import requests
import csv
import os
from datetime import datetime

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()
    btc = data["bitcoin"]["usd"]
    eth = data["ethereum"]["usd"]
    return btc, eth

def save_to_csv(btc, eth):
    file = "prices.csv"
    file_exists = os.path.exists(file)
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "bitcoin_usd", "ethereum_usd"])
        writer.writerow([datetime.now(), btc, eth])

def main():
    btc, eth = get_prices()
    print(f"Bitcoin:  ${btc:,}")
    print(f"Ethereum: ${eth:,}")
    save_to_csv(btc, eth)
    print("Saved to prices.csv")

main()
