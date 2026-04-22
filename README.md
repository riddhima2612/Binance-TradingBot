# Binance Futures Trading Bot (Testnet)

#  Overview

This is a simple Python-based trading bot that interacts with Binance Futures Testnet (USDT-M).
It supports placing MARKET and LIMIT orders via a CLI interface, with proper logging and input validation.


# Setup Instructions

1. Clone the repository:

   ```bash
   git clone <your-repo-link>
   cd TradingBot
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add:

   ```
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   ```



# How to Run

# MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

# LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 80000
```


# Output

The CLI prints:

* Order ID
* Status
* Executed Quantity
* Average Price



# Logging

* Logs are stored in `bot.log`
* Includes:

  * Order requests
  * API responses
  * Errors (if any)

The log file contains entries for:

* One MARKET order
* One LIMIT order

---

# Project Structure

```
TradingBot/
│── bot/
│    ├── client.py
│    ├── orders.py
│    ├── validators.py
│    ├── logging_config.py
│    ├── __init__.py
│
│── cli.py
│── requirements.txt
│── README.md
│── bot.log
```

---

# Features

* Place MARKET and LIMIT orders
* CLI-based input using argparse
* Input validation
* Logging of API requests/responses
* Error handling for invalid inputs and API failures

---

# Assumptions

* Binance Futures Testnet is used (not live trading)
* User has valid API credentials
* Symbol format follows Binance standard (e.g., BTCUSDT)
* LIMIT order price must be valid relative to market price

---

# Requirements

* Python 3.x
* python-binance
* python-dotenv

---

# Notes

* This project is for educational/testing purposes only
* No real funds are involved
* Ensure API keys are kept secure
