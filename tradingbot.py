from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime
import config
from alpaca_trade_api import REST
from timedelta import Timedelta

ALPACA_CREDS = {
    "API_KEY": config.API_KEY,
    "API_SECRET": config.API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def initialize(self, symbol:str="SPY", cash_at_risk:float=.5):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
        self.cash_at_risk = cash_at_risk
        self.api = REST(base_url=config.BASE_URL, key_id=config.API_KEY, secret_key=config.API_SECRET)


    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)
        quantity = round(cash * self.cash_at_risk / last_price, 0)
        return cash, last_price, quantity

    def get_dates(self):
        today = self.get_datetime()
        three_days_prior = today - Timedelta(days=3)
        return today.strfttime('%Y-%m-%d'), three_days_prior.strfttime('%Y-%m-%d')



    def on_traiding_iteration(self):
        cash, last_price, quantity = self.position_sizing()
        if cash > last_price:
            if self.last_trade ==  None:
                order = self.create_order(self.symbol, quantity, "buy", type="bracket", )
                self.submit_order(order)
                self.last_trade = "buy"


start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, parameters={"symbol": "SPY", "cash_at_risk":.5})
strategy.backtest(YahooDataBacktesting, start_date, end_date, parameters={"symbol": "SPY", "cash_at_risk":.5})