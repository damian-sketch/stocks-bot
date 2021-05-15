import yfinance as yf
import pandas as pd
from telegram import Update

def get_price_change():
    
 
    crypto = yf.Ticker("ETH-USD")
    ''' Get the info of your currency'''
    # eth = crypto.info
    '''Get  the history of a custom timeframe'''
    hist = crypto.history(period="1d")
    
    # Make the data readable
    data = pd.DataFrame(hist)
    dats = data.to_json()
    return(dats)



get_price_change()
