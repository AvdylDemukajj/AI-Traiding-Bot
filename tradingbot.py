from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime
import config

ALPACA_CREDS = {
    "API_KEY": config.API_KEY,
    "API_SECRET": config.API_SECRET,
    "PAPER": True
}

