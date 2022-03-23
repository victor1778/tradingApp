import auth
import json
from twelvedata import TDClient

#Array declaration
symbol = []
name = []
currency = []
id_exchange = []

#Pulls updated data from API into json, then converts it to dictionary
api = TDClient(apikey="demo")
raw_data = api.get_stocks_list(country="United States").as_raw_json();
assets = json.loads(raw_data)

#Pulls existing data from SQL database
auth.mycursor.execute("SELECT symbol, name FROM tbl_ticker")
rows = auth.mycursor.fetchall()
temp = [row['symbol'] for row in rows]

#Compares updated json with existing db, and only adds new entries to arrays
for data in assets['data']:
    if data['symbol'] not in temp:
        symbol.append(data['symbol'])
        name.append(data['name'])
        currency.append(data['currency'])
        id_exchange.append(data['exchange'])      

#Changes id_exchange[x] from str to int 
for x in range(0, len(id_exchange), 1):
    if id_exchange[x] == "NYSE":
        id_exchange[x] = 1
    elif id_exchange[x] == "OTC":
        id_exchange[x] = 2
    elif id_exchange[x] == "NASDAQ":
        id_exchange[x] = 3
    elif id_exchange[x] == "CBOE":
        id_exchange[x] = 4

#SQL insert 
for x in range(0, len(id_exchange), 1):
    try:
        auth.mycursor.execute("INSERT INTO tbl_ticker(symbol,name,currency,idExchange) VALUES (?,?,?,?)", (symbol[x], name[x], currency[x], id_exchange[x]))
        print("Successfully added: ", symbol[x])
        auth.conn.commit()
    except auth.mariadb.Error as e:
        print(f"Error: {e}")
        auth.conn.rollback()

auth.conn.close()

