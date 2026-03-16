# Crypto Alert Bot 🚨

A Python bot that monitors real-time cryptocurrency prices and sends 
instant Google Chat notifications when a price target is hit.

## What it does

- Fetches live BTC, ETH prices from the CoinGecko API (free, no auth needed)
- Compares current prices against your custom target prices
- Sends a Google Chat webhook notification when any target is triggered
- Runs on a schedule — checks every 10 minutes automatically
- Stores price history in SQLite for later analysis

## Tech used

- Python 3
- requests (API calls)
- sqlite3 (price history storage)
- schedule (automated runs)
- Google Chat webhooks (notifications)

## Project status

🚧 In progress — building this to learn Python 3, API integrations, 
and SQLite as part of my data engineering learning journey.

## Author

Monika Pant — learning data engineering one project at a time.
