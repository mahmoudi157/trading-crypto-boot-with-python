from ast import Try
import get_data as gd
import pandas as pd
import talib as tl
from database import Orders
#import tickers as tkr
import telegram_interface as ti
import format_orders as fo
import place_orders as po
from binance_client import client
import numpy as np
from database import toks

nl = "%0D%0A"


interval = "3m"
depth = "40 hours ago UTC+1"
#tickers=["BTCUSDT", "ETHUSDT", "NEOUSDT", "LTCUSDT", "QTUMUSDT", "ADAUSDT", "XRPUSDT", "EOSUSDT", "IOTAUSDT", "XLMUSDT", "ONTUSDT", "ICXUSDT", "NULSUSDT", "VETUSDT", "LINKUSDT", "WAVESUSDT", "BTTUSDT", "ONGUSDT", "HOTUSDT"]



def zscor(tickers, num):
  for ticker in tickers:
    try:
      data = gd.get_klines(ticker, interval, depth)
      if not data.empty:
                data = pd.DataFrame(data)
                close = np.array(data["Close"].dropna().astype(float))
                close = close[-40:]
                mean = tl.SMA(close, 20)
                deviation = tl.STDDEV(close, 20)
                displacement = close-mean
                #if deviation != 0:
                  #pass
                zscore = displacement/deviation
                #else:
                    #zscore = displacement/displacement
                zscore = pd.DataFrame(zscore).dropna()
                zscore = zscore[0].astype(float)
                a = np.array(zscore)
                #else:
                    
                #zranklo = np.percentile(a, 0)
                #zrankhi = np.percentile(a, 100)
               # zmean = tl.SMA(a, 20)
                #print("zscore= ",a[-1])
                #print("zmean= ",zmean[-1])
                #print("zranklo= ",zranklo)
                #print("zrankhi= ",zrankhi)
                # zscore=zscore.tail(1)
                #volume = float(data["Volume"].tail(1))

                if (a[-1] <=-2.7 and (a[-1]>a[-2] )and a[-1] != "-Infinity"):
                    balance = fo.get_usdt_balance(0)
                    price = fo.get_ticker_price(ticker)
                    if balance >= 20:
                        tbalance = fo.get_token_balance(ticker, 0)
                        if (tbalance*price < 10):
                            #order=fo.buy_market_quantity(ticker , balance)
                            order = fo.execute_buy_limit_order(ticker, 20, fo.format_price(ticker, price))
                            
                            print("Buy order placed successfully")
                            print("Quntite :", fo.get_token_balance(ticker, 0))
                            print("Symbol:", ticker)
                            toks.add('list_sell',ticker)
                            Orders.save_buy_order(collection="Buy_orders", symbol=ticker, orderId=order, Qty=fo.get_token_balance(ticker, 0), avgPrice=price)
                if (a[-1]>=1.7 and a[-1] != "-Infinity"):
                    tbalance = fo.get_token_balance(ticker, 0)
                    price = fo.get_ticker_price(ticker)
                    print(ticker, tbalance*price > 11)
                    if (tbalance*price > 11):
                        print(ticker, tbalance*price)
                        order = fo.execute_sell_market_order(symbol=ticker, quantity=str(fo.format_quantity(ticker, quantity=tbalance)))
                        toks.rmvtoks(ticker)
                        Orders.save_sell_order(collection="sell_orders", symbol=ticker, order=order)
                        print(" sell order placed successfully :",ticker, 'balance =', tbalance)
                        print("price = ", price, '  total =', (price*tbalance))


    except:
      pass
                    # else:
                        # ti.send_msg("sell order not placed  "+nl+"Symbol : "+ticker+nl+"sell price : "+str(price)+str(" USDT")+nl+"balance amount :"+str(tbalance) )
                    #Signals.add(collection = "Signals_sell", ticker = ticker , order= "sell" , zscore=zscore ,  price=price , volume=volume )
    #Signals.add(collection = "Signals_buy", ticker = "End_"+str(num), order = "non", zscore = 0 ,price= 0 , volume=0)
    #Signals.add(collection = "Signals_sell", ticker = "End_"+str(num), order = "non", zscore = 0 ,price= 0 , volume=0)


#zscor(tickers,1)
