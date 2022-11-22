import binance.client
from binance.client import Client
#import format_orders as fo
#import place_orders as po
Pkey = ''
Skey = ''

client = Client(api_key=Pkey, api_secret=Skey)
"""
tbalance=po.get_token_balance("IOTAUSDT", 0)
print(tbalance)
quantity=fo.format_quantity("IOTAUSDT", tbalance)
print(quantity)
order=fo.execute_sell_market_order(symbol="IOTAUSDT", quantity=quantity)"""
