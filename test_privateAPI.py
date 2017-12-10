from coincheck import Coincheck
import time

access_key = "Your Access Key"
secret_key = "Your Secret Key"

coincheck = Coincheck(access_key, secret_key)

path_orders = '/api/exchange/orders'
params = {
    "pair": "btc_jpy",
    "order_type": "buy",
    "rate": 100000,
    "amount": 0.01,
}
orders = coincheck.post(path_orders, params)
print(orders)
print()

path_opens = '/api/exchange/orders/opens'
opens = coincheck.get(path_opens)
print(opens)
print()

# replace [id]
# path_cancel = '/api/exchange/orders/[id]'
# cancel = coincheck.delete(path_cancel)
# print(cancel)
# print()

path_transactions = '/api/exchange/orders/transactions'
transactions = coincheck.get(path_transactions)
print(transactions)
print()

path_transactions_pagination = '/api/exchange/orders/transactions_pagination'
transactions_pagination = coincheck.get(path_transactions_pagination)
print(transactions_pagination)
print()

path_positions = '/api/exchange/leverage/positions'
positions = coincheck.get(path_positions)
print(positions)
print()

path_balance = '/api/accounts/balance'
balance = coincheck.get(path_balance)
print(balance)
print()

path_leverage_balance = '/api/accounts/leverage_balance'
leverage_balance = coincheck.get(path_leverage_balance)
print(leverage_balance)
print()

# path_send_money = '/api/send_money'
# params = {
#     "address": "input address",
#     "amount": 0.1
# }
# send_money = coincheck.post(path_send_money, params)
# print(send_money)

# replace [id]
# path_fast = '/api/deposit_money/[id]/fast'
# params = {
#     "id": id
# }
# fast = coincheck.post(path_fast, params)
# print(fast)

path_accounts = '/api/accounts'
accounts = coincheck.get(path_accounts)
print(accounts)
print()

# path_borrows = '/api/lending/borrows'
# borrows = {
#     "amount": 0.1,
#     "curreny": "BTH"
# }
# borrows = coincheck.post(path_borrows, params)
# print(borrows)

path_matches = '/api/lending/borrows/matches'
matches = coincheck.get(path_matches)
print(matches)
print()

# replace [id]
# path_replay = '/api/lending/borrows/[id]/repay'
# params = {
#     "id": 12345678
# }
# replay = coincheck.post(path_replay, params)
# print(replay)
# print()

path_to_leverage = '/api/exchange/transfers/to_leverage'
params = {
    "currency": "JPY",
    "amount": 10000
}
to_leverage = coincheck.post(path_to_leverage, params)
print(to_leverage)
print()


path_from_leverage = '/api/exchange/transfers/from_leverage'
params = {
    "currency": "JPY",
    "amount": 10000
}
from_leverage = coincheck.post(path_from_leverage, params)
print(from_leverage)
