import requests

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()
    price = data["bitcoin"]["usd"]
    return price

def main():
    price = get_btc_price()
    print(f"Bitcoin price: ${price:,}")

main()
