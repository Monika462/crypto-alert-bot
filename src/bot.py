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
```

**Save — Cmd+S. Close TextEdit.**

Install requests, then run it:
```
pip install requests
python3 src/bot.py
```

You should see something like:
```
Bitcoin price: $83,241
```

Now commit:
```
git add src/bot.py
git commit -m "feat: fetch BTC price from API"
git push origin main