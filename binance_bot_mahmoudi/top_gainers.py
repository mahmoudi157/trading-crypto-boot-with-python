from tkinter import Y
from binance.client import Client
import pandas as pd
import requests
from database import toks
from database import db
from binance_client import client
from database import toks


def get_all_24hours_pct(top):
    tickers_pc = []
    tickers = []
    prices = client.get_ticker()
    for ticker in prices:
        if 'USDT' in ticker['symbol'] and ticker['symbol']   :
            if not ('UP' and 'DOWN')in ticker['symbol'] and ticker['symbol']:
             pairs = {'Symbol':ticker['symbol'] , 'pct' :float(ticker['priceChangePercent']) }
             tickers_pc.append(pairs)
    tickers_pc = sorted(tickers_pc, key=lambda x : x['pct'], reverse=True)
    tickers_pc = tickers_pc[:top]
    for ticker in tickers_pc :
        tickers.append(ticker['Symbol'])
    
    return tickers
m=get_all_24hours_pct(120)

i=0
toks.rmvall("list_2")
while i<20: 
   
    toks.add("list_2",str(m[i]))
    i=i+1
    print(i)
i=20
toks.rmvall("list_3")
while i<40: 
   
    toks.add("list_3",str(m[i]))
    i=i+1
    print(i)
i=40
toks.rmvall("list_4")
while i<60: 
    
    toks.add("list_4",str(m[i]))
    i=i+1
    print(i)
i=60
toks.rmvall("list_5")
while i<80: 
    
    toks.add("list_5",str(m[i]))
    i=i+1
    print(i)
i=80
toks.rmvall("list_6")
while i<100: 
    
    toks.add("list_6",str(m[i]))
    i=i+1
    print(i)

i=100
toks.rmvall("list_7")
while i<120: 
    
    toks.add("list_7",str(m[i]))
    i=i+1
    print(i)
