# Crypto Alert Bot 🚨

A Python bot that monitors real-time Bitcoin and Ethereum prices,
detects significant price changes, and sends instant phone notifications.

Runs automatically every hour — no manual work needed.

## What it does

- Fetches live BTC and ETH prices from the CoinGecko API (free, no auth needed)
- Compares current price against the previous check
- Sends a phone notification via ntfy when price moves more than 3%
- Saves every price check to a CSV file with timestamp
- Logs all activity and errors to bot.log
- Runs automatically every hour using the schedule library

## Demo

![Bot running in terminal](screenshots/bot-running.png)

## Tech used

- Python 3
- requests — API calls and sending notifications
- schedule — running the bot every hour automatically
- csv — storing price history with timestamps
- logging — tracking all activity and errors
- ntfy.sh — free phone notifications, no account needed

## Project structure

crypto-alert-bot/
├── src/
│   └── bot.py
├── screenshots/
│   └── bot-running.png
├── .gitignore
├── requirements.txt
└── README.md

## How to run
```bash
git clone https://github.com/Monika462/crypto-alert-bot.git
cd crypto-alert-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/bot.py
```

## How to receive alerts on your phone

1. Install the **ntfy** app on your phone (free, App Store or Play Store)
2. Subscribe to the topic: `monika-crypto-alert`
3. Run the bot — alerts will arrive on your phone instantly

## What I learned building this

- Calling a REST API with Python and parsing JSON responses
- Storing time-series data in CSV with automatic headers
- Detecting percentage change between two data points
- Sending real-time phone notifications without any paid service
- Scheduling automated runs with the schedule library
- Structured error handling with try/except for network failures
- Writing logs to a file for debugging and monitoring

## Author

Monika Pant — Software Engineer learning Data Engineering.
Building one real project at a time.
GitHub: github.com/Monika462

## Part of my data engineering learning journey

This is Project 1 of 10 in my roadmap to become a Data Engineer.
Each project teaches real tools through real problems.
