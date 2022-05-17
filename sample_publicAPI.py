import requests
import json

# Private API
URL_ticker = 'https://coincheck.com/api/ticker'
ticker = requests.get(URL_ticker).json()
print("ticker")
print(ticker)
print()

URL_trades = 'https://coincheck.com/api/trades'
trades = requests.get(URL_trades, params={"offset": 5}).json()
print(trades)
print()

URL_order_books = 'https://coincheck.com/api/order_books'
order_books = requests.get(URL_order_books).json()
print(order_books)
print()

# define either amount or price
URL_rate = 'https://coincheck.com/api/exchange/orders/rate'
params = {'order_type': 'sell', 'pair': 'btc_jpy', 'amount': 0.1}
rate = requests.get(URL_rate, params=params).json()
print(rate)
print()

coins = {'BTC': 'btc_jpy', 'ETH': 'eth_jpy',
         'XEM': 'xem_jpy', 'BCH': 'bch_jpy'}
URL_rate_ = 'https://coincheck.com/api/rate/'
for key, item in coins.items():
    rate = requests.get(URL_rate_+item).json()
    print(key, rate)
