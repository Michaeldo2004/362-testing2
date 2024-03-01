# Library to import real-time UTC
from datetime import datetime, timedelta

# Library to call yahoo's historical data
import yfinance as yahoo

# Library to handle and use financial data
import pandas as pd

# ML file
from ML_Predictions import *


class Stock():
       
    def __init__(self, stock):
        self.stock = stock    
    
    # Returns the current price of the Stock
    def currentPrice(stock):
        stock_stat = yahoo.Ticker(stock)
        return stock_stat.info['ask']

    # Returns the # of shares
    def stockCount(stock):
        return yahoo.Ticker(stock).info.get('sharesOutstanding', 'N/A')
    
    # Returns Market Cap
    def marketCap(stock):
        try:
            stock_data = yahoo.Ticker(stock)
            info = stock_data.info
            market_cap = info.get('marketCap', None)
            return market_cap
        except Exception as e:
            return -1
    
    # Calls the historical data of stock
    # 1 weeks worth of data
    def historyCall(stock):

        # Obtains the current date and time (UTC)
        # Also obtains the date and time 1 week before
        current_date = datetime.now()
        one_week_prior = current_date - timedelta(days=30)
        
        historical_data = yahoo.download(stock, start=one_week_prior, end=current_date)

        return historical_data
            
