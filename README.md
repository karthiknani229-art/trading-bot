 Binance Futures Testnet Trading Bot

A clean, modular Python CLI application that places MARKET and LIMIT orders on the Binance USDT-M Futures Testnet with structured logging, robust validation, and production-style architecture.

This project was built as part of the Python Developer Internship assignment.

 Overview

This trading bot demonstrates:

Proper separation of concerns

Robust CLI input validation

Structured logging to file and console

Error handling for API and network failures

Successful order placement on Binance Futures Testnet

The bot interacts only with the testnet environment — no real funds are used.

 Features

 Place MARKET orders

 Place LIMIT orders

 Supports BUY and SELL

 CLI-based user input (argparse)

 Strong input validation

 Structured logging

 Automatic Binance timestamp synchronization

 Modular, production-style code

 Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures client wrapper
│   ├── orders.py          # Order building & formatting
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
└── logs/
 Requirements

Python 3.9+

Binance Futures Testnet account

Testnet API Key & Secret

 Environment Setup

Create a .env file in the project root:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here


PowerShell

python -m venv venv
.\venv\Scripts\Activate.ps1
3 Install dependencies
pip install -r requirements.txt
▶ How to Run

All commands must be executed from the project root.
MARKET Order Exmaple
pyhton cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0002 LIMIT Order Exmaple
pyhton cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0002 --price 90000
Example CLI Output

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
Logging

Logs are automatically written to:

logs/trading_bot.log

The log file contains:

Order request details

Binance API responses

Error traces

 Includes evidence of:

one MARKET order

one LIMIT order

(as required by the assignment)

 Validation & Error Handling

The application validates:

symbol presence

side (BUY/SELL)

order type (MARKET/LIMIT)

quantity > 0

price required for LIMIT

Handled failures include:

invalid CLI input

Binance API errors

timestamp drift

network issues

 Assumptions

Orders are placed on Binance USDT-M Futures Testnet

Minimum notional requirements are enforced by Binance

LIMIT orders may remain in NEW status if price is not reached

MARKET orders on testnet may briefly show NEW before fill


 Author

Penta Karthik
