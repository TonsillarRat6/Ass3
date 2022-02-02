from typing import List
from abc import ABC, abstractmethod

class Exchange(ABC): #Dit is de Draw method
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_market_data(self):
        pass

class Binance(Exchange): #Dit is dan Draw TKInter
    def connect(self):
        print("Connecting to Binance...")
    
    def get_market_data(self, coin: str) -> List[float]:
        return[10, 12, 18, 14]  

class Coinbase(Exchange): #Dit is dan Draw SVG
    def connect(self):
        print("Connecting to Coinbase...")
    
    def get_market_data(self, coin: str) -> List[float]:
        return[20, 22, 28, 24]  