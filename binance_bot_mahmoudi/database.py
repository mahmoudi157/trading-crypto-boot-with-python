
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["autoTrading"]

class Status():
    def save_status(collection, status, time):
        collection = db[collection]
        data = collection.delete_many({})
        new_stat = {"Status":status, "Time":time}
        data =collection.insert_one(new_stat)
        return data

    def find_status(collection):
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            stat = dt["Status"]
        return stat



class Signals():

    def add(collection, ticker, order, zscore, price , volume ):
        collection = db[collection]
        new_signal = {"ticker":ticker, "order":order, "zscore":zscore , "price":price ,"volume":volume }
        data = collection.insert_one(new_signal)
        return data

    def find_all(collection):
        tickers = {}
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            tickers[dt["ticker"]] = [dt["volume"], dt["zscore"] ,dt["order"]] #{"BTCUSDT":[5646548654, -3.5]}
        return tickers

    def clear_all(collection):
        collection = db[collection]
        collection.delete_many({})

    def find_elem(collection,elem):
        collection = db[collection]
        data = collection.find(elem)
        return data

class Orders():
    def save_buy_order(collection, symbol, orderId, Qty, avgPrice):
        collection = db[collection]
        new_order = {"Symbol":symbol, "OrderId":orderId, "Quantity":Qty,
                        "BuyPrice":avgPrice}
        data = collection.insert_one(new_order)
        return data

    def save_oco_order(collection, symbol, orderId, origQty, take_profit, stop_limit, trigger_price):
        collection = db[collection]
        new_order = {"Symbol":symbol, "OrderId":orderId, "Quantity":origQty,
                        "TP":take_profit, "SL":stop_limit, "Trigger":trigger_price}
        data = collection.insert_one(new_order)
        return data
    def save_sell_order(collection, symbol,order):
      collection = db[collection]
      new_order = {"Symbol":symbol,'order':order}
      data = collection.insert_one(new_order)
      return data



class go():
    def chango(m):
        db['tt'].delete_many({})
        db['tt'].insert_one({"t":m})
    def getgo():
        m=db['tt'].find({})[0]['t']
        return m

class toks():
    def add(collection,ticker):
       
        db[collection].insert_one({"ticker":ticker})


    def gets(collection):
        m=db[collection].find({})
        tic={}
        for t in m:
             tic[t["ticker"]]=0
        tic=tic.keys()
        
        return tic


    def rmvtoks(tokn):
         db['list_sell'].delete_one({"ticker":tokn})

    def rmvall(collection):
        db[collection].delete_many({})



"""
n=toks.gets()
tic={}
for t in n:
    tic[t["ticker"]]=""
a=tic.keys()
print(a)
for l in a:
    print(l)
    

d=["bgbhgn","hhghhhh"]
m=toks.gets()
d.extend(m)
print(d)
"""
#toks.rmvtoks('KMDUSDT')
#toks.add("list_sell","WOOUSDT")