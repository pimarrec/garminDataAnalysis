from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager


# api_key_ed="VCvqSJEp9TXI0uao5hpqxtKo2pCqLeGRxbo0i00hIjj6frGhOZYYR1kKox4hrtHT"

api_key = "VCvqSJEp9TXI0uao5hpqxtKo2pCqLeGRxbo0i00hIjj6frGhOZYYR1kKox4hrtHT"

secret_file = "Private_key_rsa"

# with open(secret_file, 'r') as file:
#     api_secret = file.read().replace('\n', '')

api_secret = "Yue9ygaWuPzSA9BoNWRMsYG1yaL4CiyFMRQeZTgJnpduIMllcy0cMCkzlYD96PUu"


client = Client(api_key, api_secret)
#client.API_URL = "https://testnet.binance.vision/api"

# get market depth
#depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function

# get all symbol prices
# prices = client.get_all_tickers()

# print(prices)

info = client.get_account()


# get only the one with either free or locked > 0
balances = [asset for asset in info['balances'] if float(asset['free']) > 0 or float(asset['locked']) > 0]



margin = client.get_margin_account()
margins_balances = [asset for asset in margin['userAssets'] if float(asset['free']) > 0 or float(asset['locked']) > 0]

print(margins_balances)

# print(balances)
import datetime
def timestamp2date(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')

#since 2017
# dhistory = client.get_deposit_history(startTime = 1504137600000)
# print(dhistory)
trades=[]
for i in margins_balances:
    try:
        trades.append(client.get_margin_trades(symbol=i['asset']+'USDT'))
        trades.append(client.get_margin_trades(symbol=i['asset']+'ETH'))
    except:
        print("No trades for ", i['asset']+ 'USDT or '+i['asset']+'ETH')

flatten = lambda l: [item for sublist in l for item in sublist]

# print(trades)

for i in balances:
    try:
        if i['asset'][:2]=="LD":
            i['asset'] = i['asset'][2:]
        trades.append(client.get_my_trades(symbol=i['asset']+'USDT'))
        trades.append(client.get_my_trades(symbol=i['asset']+'ETH'))
        trades.append(client.get_my_trades(symbol=i['asset']+'BUSD'))
        trades.append(client.get_my_trades(symbol=i['asset']+'BNB'))
    except:
        print("No trades for ", i['asset']+ 'USDT or '+i['asset']+'ETH')

for i in balances:
    try:
        if i['asset'][:2]=="LD":
            i['asset'] = i['asset'][2:]
        trades.append(client.get_all_orders(symbol=i['asset']+'USDT'))
        trades.append(client.get_all_orders(symbol=i['asset']+'ETH'))
        trades.append(client.get_all_orders(symbol=i['asset']+'BUSD'))
        trades.append(client.get_all_orders(symbol=i['asset']+'BNB'))
    except:
        print("No trades for ", i['asset']+ 'USDT or '+i['asset']+'ETH')

trades = flatten(trades)


for i in trades:
    date = timestamp2date(int(i['time']))
    symbol = i['symbol']
    price = i['price']
    try:
        qty = i['qty']
        commission = i['commission']
        commissionAsset = i['commissionAsset']
    except:
        qty = i['executedQty']
        commission = 0
        commissionAsset = 0
    
    try:
        achat = i['isBuyer']
        type_op = "Achat" if achat else "Vente"
    except:
        type_op = "Achat" if i["side"] == "BUY" else "Vente"
    try :
        if i["status"] == "FILLED":
            print(f"Date: {date}, {type_op}  Symbol: {symbol}, Price: {price}, Qty: {qty}, Commission: {commission}, CommissionAsset: {commissionAsset}")
    except:
        print(f"Date: {date}, {type_op}  Symbol: {symbol}, Price: {price}, Qty: {qty}, Commission: {commission}, CommissionAsset: {commissionAsset}")

print(trades)

# 23 october in timp stamp
startTime = str(int(datetime.datetime(year=2021,month=3,day=1).timestamp()))

# 23 january
endTime = str(int(datetime.datetime(year=2024,month=2,day=22).timestamp()))
print(startTime,endTime)


# margin_transfer = client.get_margin_transfer_history(startTime=startTime)

#print(margin_transfer)



balance = client.get_asset_balance(asset='ETH')
# print(balance)

trades = client.get_my_trades(symbol='ETHUSDT')
# withdraw 100 ETH
# check docs for assumptions around withdrawals
# from binance.exceptions import BinanceAPIException
# try:
#     result = client.withdraw(
#         asset='ETH',
#         address='<eth_address>',
#         amount=100)
# except BinanceAPIException as e:
#     print(e)
# else:
#     print("Success")



# # fetch list of withdrawals
# withdraws = client.get_withdraw_history()

# # fetch list of ETH withdrawals
# eth_withdraws = client.get_withdraw_history(coin='ETH')

# # get a deposit address for BTC
# address = client.get_deposit_address(coin='BTC')

# # get historical kline data from any date range

# # fetch 1 minute klines for the last day up until now
# klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# # fetch 30 minute klines for the last month of 2017
# klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

# # fetch weekly klines since it listed
# klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")



#### Plan ####
# 1. Get all the trades for each asset and store them in a file
# 2. Get the current price of each asset
# 3. Calculate the buying price of each asset
# 4. Calculate the selling price of each asset
# 5. Calculate the PRU of each asset
# 6. Calculate the profit of each asset
# 7. Calculate the total profit

# Store the last timestamp of the trades in a file
# At the beginning of the script, read the last timestamp of the trades
# Get all the trades from the last timestamp until now



