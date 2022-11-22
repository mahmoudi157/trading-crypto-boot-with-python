import binance.client 
from binance.client import Client 
import pandas as pd 
import binance_client as api


client = api.client
def balance(coin):
    json = client.get_asset_balance(asset=coin)
    free = float(json['free'])
    return free
def format_value(valuetoformatx,fractionfactorx):
					value = valuetoformatx
					fractionfactor = fractionfactorx
					Precision = abs(int(f'{fractionfactor:e}'.split('e')[-1]))
					FormattedValue = float('{:0.0{}f}'.format(value, Precision))
					return FormattedValue		

def pairPriceinfo(ticker,client): 
				info = client.get_symbol_info(ticker)
				minPrice = pd.to_numeric(info['filters'][0]['minPrice'])  #  0 to isolate  price precision   #  2 to isloate qty 
				return minPrice

def pairQtyinfo(ticker,client):
					info = client.get_symbol_info(ticker)
					minQty = pd.to_numeric(info['filters'][2]['minQty'])   
					#print()
					return minQty 



def buy(ticker,persentage):
    freeUSDT =balance('USDT')
    #send market buy order 
    price = client.get_avg_price(symbol=ticker)
    price = float(price['price'])
    pctUse = (persentage/100)
    USDT = freeUSDT*pctUse
    qty = USDT/price
    minQty = pairQtyinfo(ticker,client)
    qtyFormatted = format_value(qty,minQty)
    order = client.order_market_buy(symbol = ticker, quantity = qtyFormatted)
    #send market buy order

    
def selloco(coin,ticker,limit,stopPrice):
    asset=coin.upper()
    ticker=ticker.upper()
    assetBalance=balance(asset)
    minQty = pairQtyinfo(ticker,client)
    assetBalance = format_value(assetBalance,minQty)
    price = client.get_avg_price(symbol=ticker)
    price = float(price['price'])
    pct_tp = limit/100
    pct_sl = stopPrice/100
    minPrice = pairPriceinfo(ticker,client)
    Above = price+(price*pct_tp)
    Above = format_value(Above,minPrice)
    belowTrigger = price-(price*pct_sl)
    belowTrigger = format_value(belowTrigger,minPrice)
    belowLimit = belowTrigger-(belowTrigger*0.001)
    belowLimit = format_value(belowLimit,minPrice)
    orderoco = client.create_oco_order(symbol= ticker,side ='SELL',quantity= assetBalance,price = Above ,stopPrice= belowTrigger, stopLimitPrice = belowLimit,limitIcebergQty =0,stopIcebergQty = 0,stopLimitTimeInForce= 'GTC')

def sell(ticker):
     ticker=ticker.upper()
     asset = ticker[:-4].upper()
     qty=balance(asset)
     minQty = pairQtyinfo(ticker,client) 
     qty = format_value(qty,minQty)
     order = client.order_market_sell(symbol = ticker, quantity = qty)