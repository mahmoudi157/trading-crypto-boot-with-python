from binance_client import client
import time
import pandas as pd
import threading
#import tickers as tkr
#import engulfing_2_ema_stgy as stgy
import filter_orders as fo
import zscore as stgy
from database import Signals
from database import go
from database import toks

#interval = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
interval =[0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57]

def inter():
   interval =[0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57]
   return interval



#interval=inter()
def server_tm():
    time_srv = client.get_server_time()
    time = pd.to_datetime(time_srv["serverTime"], unit = "ms")
    min_ = time.strftime("%M")
    min_ = int(min_)
    sec_ = time.strftime("%S")
    sec_ = int(sec_)
    last=go.getgo()
    for i in interval:
        
        if (min_ == i) and (sec_ == 3 ) and (last!=min_):
            go.chango(min_)
            
            print("Searching for opportunities -----------------------------------------------------------------------")
            list_1 =toks.gets('list_sell')
            list_2 =toks.gets('list_2')
            list_3=toks.gets('list_3')
            list_4=toks.gets('list_4')
            list_5=toks.gets('list_5')
            list_6=toks.gets('list_6')
            list_7=toks.gets('list_7')
            
            # run strategy
            threading.Thread(target = stgy.zscor, args = (list_1, 1)).start()
            threading.Thread(target = stgy.zscor, args = (list_2, 2)).start()
            threading.Thread(target = stgy.zscor, args = (list_3, 3)).start()
            threading.Thread(target = stgy.zscor, args = (list_4, 4)).start()
            threading.Thread(target = stgy.zscor, args = (list_5, 5)).start()
            threading.Thread(target = stgy.zscor, args = (list_6, 6)).start()
            threading.Thread(target = stgy.zscor, args = (list_7, 7)).start()
            #threading.Thread(target = stgy.zscor, args = (tkr.list_6, 6)).start()
            #threading.Thread(target = fo.filter_order).start()
            #threading.Thread(target = fo.filter_order_sell).start()
            
            time.sleep(1000)
            
            #while m<20:
                #Signals.clear_all(collection = "Signals_sell")
                #Signals.clear_all(collection = "Signals_buy")
