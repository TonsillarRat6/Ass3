from Draw import Exchange, Coinbase, Binance
from abc import ABC

class Tradingbot(ABC):
    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    def connect(self): #Dus in Circel moet je dan een draw() functie hebben, en die draw functie heeft dan self.[implementatie].draw()
        self.exchange.connect()

    def get_market_data(self, coin: str):
        return[10, 12, 18, 14]  


variable = Coinbase
coinbase = Tradingbot(variable())
coinbase.connect()

binance = Tradingbot(Binance())
binance.connect()
