import requests
import csv
import os
from datetime import datetime

NTFY_TOPIC = "monika-crypto-alert"

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()
    btc = data["bitcoin"]["usd"]
    eth = data["ethereum"]["usd"]
    return btc, eth

def read_last_row():
    file = "prices.csv"
    if not os.path.exists(file):
        return None, None
    with open(file, "r") as f:
        rows = list(csv.reader(f))
    if len(rows) < 2:
        return None, None
    last = rows[-1]
    return float(last[1]), float(last[2])

def send_alert(title, message):
    requests.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=message.encode("utf-8"),
        headers={"Title": title, "Priority": "high", "Tags": "rotating_light"}
    )
    print("Alert sent to your phone!")

def check_change(old, new, coin):
    if old is None:
        return
    change = ((new - old) / old) * 100
    direction = "UP" if change > 0 else "DOWN"
    print(f"{coin} change: {change:+.2f}%")
    if abs(change) >= 0.1:
        send_alert(
            f"{coin} moved {direction} {abs(change):.2f}%",
            f"Current price: ${new:,}"
        )

def save_to_csv(btc, eth):
    file = "prices.csv"
    file_exists = os.path.exists(file)
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "bitcoin_usd", "ethereum_usd"])
        writer.writerow([datetime.now(), btc, eth])

def main():
    old_btc, old_eth = read_last_row()
    btc, eth = get_prices()
    print(f"Bitcoin:  ${btc:,}")
    print(f"Ethereum: ${eth:,}")
    check_change(old_btc, btc, "Bitcoin")
    check_change(old_eth, eth, "Ethereum")
    save_to_csv(btc, eth)
    print("Saved to prices.csv")

main()
