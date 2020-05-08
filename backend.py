import numpy as np 
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

def RSI(stock_name, size, k, plot = False):
    ti = TechIndicators(key = k)
    rsi = []
    temp_data, temp_meta = ti.get_rsi(symbol = stock_name, interval = '5min', time_period = '14')
    del temp_meta
    for key in temp_data:
        rsi.append(float(temp_data[key]['RSI']))
    del rsi[size:]
    rsi.reverse()
    return rsi
def MACD(stock_name, size, k):
    ti = TechIndicators(key = k)
    hist = []
    signal = []
    macd = []
    temp_data , temp_meta = ti.get_macd(symbol = stock_name, interval = '5min', fastperiod = '12', slowperiod = '26', signalperiod = '9')
    del temp_meta
    for key in temp_data:
        hist.append(float(temp_data[key]['MACD_Hist']))     
        signal.append(float(temp_data[key]['MACD_Signal']))
        macd.append(float(temp_data[key]['MACD']))
    del hist[size:], signal[size:], macd[size:]
    hist.reverse()
    signal.reverse()
    macd.reverse()
    return hist, signal, macd
def get_price(stock_name, size, k):
    stock = []
    ts = TimeSeries(key = k)
    temp_data , temp_meta = ts.get_intraday(symbol = stock_name, interval = '1min',)
    del temp_meta
    for key in temp_data:
        stock.append(float(temp_data[key]['4. close']))
    del stock[size:]
    stock.reverse()
    return stock