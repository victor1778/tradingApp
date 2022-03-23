from turtle import clear
import auth
import time
from twelvedata import TDClient

api = TDClient(apikey="96456b4f8d23437c9fb5dee2aae90779")

#Pulls existing data from SQL database
auth.mycursor.execute("SELECT idTicker, symbol, name FROM tbl_ticker")
rows = auth.mycursor.fetchall()
symbols = [row['symbol'] for row in rows]

stock_dict = {}
for row in rows:
        symbol = row['symbol']
        symbols.append(symbol)
        stock_dict[symbol] = row['idTicker']

#Ticker price processing in chunks - MAX CHUNK_SIZE = 120 
chunk_size = 8
for x in range(0, 7, chunk_size):
    symbol_chunk = symbols[x:x+chunk_size]
    print(symbol_chunk)

    # Construct the necessary time series
    ts = api.time_series(symbol=symbol_chunk, interval="1day", outputsize=1)

print(ts.as_json())