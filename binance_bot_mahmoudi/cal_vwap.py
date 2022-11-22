import numpy as np
import get_data as gd
import pandas as pd
import pandas_ta as ta
import time
#import mplfinance as mpf
import tickers1

def vwap(df, period):
    klines = df
    klines["tP"] = ta.hlc3(high = klines["High"], low = klines["Low"], close = klines["Close"])
    klines["tPV"] = klines["tP"] * klines["Volume"]
    klines["mtPV"] = ta.sma(klines["tPV"], length = period)
    klines["mV"] = ta.sma(klines["Volume"], length = period)
    klines["vwap"] = klines["mtPV"] / klines["mV"]

    vwap = klines["vwap"]
    columns = klines.columns
    for i in range(6, len(columns)):
        del klines[columns[i]]

    return vwap

tickers = tickers1.usdt_tickers
x = 1
for ticker in tickers:
    #data = gd.get_klines("BTCUSDT", "4h", "500 hours ago UTC+1")
    data = gd.get_klines("BTCUSDT", "15m", "100 hours ago UTC+1")
    if not data.empty:
        #vwap_48 = vwap(data, 48) for 4h
        #vwap_84 = vwap(data, 84)

        vwap_48 = vwap(data, 7)
        vwap_84 = vwap(data, 14)

        data["vwap_48"] = vwap_48
        data["vwap_84"] = vwap_84
        data["vwap_buy"] = ta.cross(data["vwap_48"],data["vwap_84"])
        data["vwap_sell"] = ta.cross(data["vwap_84"],data["vwap_48"])
        cross_buy = data.iloc[-1]["vwap_buy"] > 0
        cross_sell = data.iloc[-1]["vwap_sell"] > 0

        #data['signal'] = np.where(data['vwap_buy'].shift(3) > 0 & data['vwap_buy'].shift(2) < 0 & data['vwap_buy'].shift(1) < 0 & data['vwap_buy'] < 0  , 1 , 0 )


        #data['vwap_buy'] = np.where(data['vwap_buy'] == True , 1 , -1)
        #data['signal'] = np.where((data['vwap_buy'].shift(3) > 0) & (data['vwap_buy'].shift(2) < 0) & (data['vwap_buy'].shift(1) < 0 )& (data['vwap_buy'] < 0)  , 1 , 0 )

        data['signal'] = np.where((data['vwap_buy'].shift(3) > 0) & (data['vwap_buy'].shift(2) < 0) & (data['vwap_buy'].shift(1) < 0 ) & (data['vwap_buy'] < 0)  , 1 , 0 )
        vclos1 = data['signal'].iloc[-1]

        #if data.loc[data.signal==1]:
        if data['signal'].iloc[-1] == 1 :
            print('You have a signal ')
            print("Yes Here is cross Sir ", vclos1)
            time.sleep(11)


        #data['signal']= np.where(data['vwap_buy'].shift(3) > 0  &data['vwap_buy'].shift(2) > 0 & data['vwap_buy'].shift(1) > 0 & data['vwap_buy'] > 0  , 1 ,0)
        #print(ticker, cross_buy,cross_sell,  " 48 :",vwap_48,    " 84: ",vwap_84)
        print(ticker, cross_buy,cross_sell, "No: ", x)
        print(ticker, " cross-close: ", vclos1)

        x = x+1
    else:
        print("No data for: ",ticker)
        pass

        '''
        close1 = ta.cross(data['close'],data['vwap_48'])
        close1 = df.close1.rolling(3)
        #Df.close.rolling(3)ذا يعطيك الclose الي تبيه انت باقي بس تمرر قيمته في ta.cross
        data['signal']= np.where(data['vwap_buy'].shift(3) > 0  &data['vwap_buy'].shift(2) > 0 & data['vwap_buy'].shift(1) > 0 & data['vwap_buy'] > 0  , 1 ,0)
        '''

'''
data = gd.get_klines("BTCUSDT", "4h", "1400 hours ago UTC+1")
vwap_48 = vwap(data, 48)
vwap_84 = vwap(data, 84)

data["vwap_48"] = vwap_48
data["vwap_84"] = vwap_84

addition_plot = [mpf.make_addplot(data["vwap_48"], type = "scatter", markersize = 1, color = "#f3ff00"), mpf.make_addplot(data["vwap_84"], type = "scatter", markersize = 1, color = "#acff35")]
mpf.plot(data, type = "candle", volume = True, addplot = addition_plot,  style = 'yahoo')

'''
