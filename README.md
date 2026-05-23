# Binance Futures Testnet Trading Bot

A modular Python CLI application that places MARKET and LIMIT orders on the Binance USDT-M Futures Testnet with structured logging, robust validation, and production-style architecture.

> All orders are placed on the Binance Testnet only — no real funds are used.

## Tech Stack

**Language:** Python 3.9+

**Libraries:** argparse, python-binance, python-dotenv

**Logging:** File + console structured logging

## Features

- Place MARKET and LIMIT orders (BUY and SELL)
- CLI-based input via argparse
- Strong input validation for all parameters
- Automatic Binance timestamp synchronization
- Structured logging to file and console
- Modular production-style architecture

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py           # Binance Futures client wrapper
│   ├── orders.py           # Order building and formatting
│   ├── validators.py       # Input validation
│   └── logging_config.py   # Logging setup
│
├── cli.py                  # CLI entry point
├── requirements.txt
└── logs/
```

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/karthiknani229-art/trading-bot.git
cd trading-bot
```

**2. Create and activate virtual environment**

```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment**

Create a `.env` file in the project root:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

Get your testnet API keys from: https://testnet.binancefuture.com

## Usage

All commands run from the project root.

**MARKET order:**

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

**LIMIT order:**

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 90000
```

**Example output:**

```
===== ORDER SUMMARY =====
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.002

===== ORDER RESPONSE =====
Order ID     : 12345678
Status       : NEW
Executed Qty : 0.000
Avg Price    : 0.00
```

## Logging

Logs are written to `logs/trading_bot.log` and include order request details, Binance API responses, and error traces.

## Validation & Error Handling

Validates: symbol, side (BUY/SELL), order type (MARKET/LIMIT), quantity > 0, price required for LIMIT orders.

Handles: invalid CLI input, Binance API errors, timestamp drift, and network failures.

## Assumptions

- Orders placed on Binance USDT-M Futures Testnet only
- Minimum notional requirements enforced by Binance
- LIMIT orders may stay in NEW status if price is not reached
- MARKET orders on testnet may briefly show NEW before fill

## Author

Penta Karthik — [GitHub](https://github.com/karthiknani229-art)
