import auth
import json
from twelvedata import TDClient
    
api = TDClient(apikey="demo")
raw_data = api.get_stocks_list(country="United States").as_raw_json();

assets = json.loads(raw_data)

symbol = []
company = []
exchange = []
currency = []

for data in assets['data']:
    for x in range(1):
        symbol.append(data['symbol'])
        company.append(data['name'])
        exchange.append(data['exchange'])
        currency.append(data['currency'])

for x in range(0, len(symbol), 1):
    print(symbol[x], company[x], exchange[x], currency[x])

for x in range(0, len(symbol), 1):
    try:
        auth.mycursor.execute("INSERT INTO stock(symbol,company,exchange,currency) VALUES (?,?,?,?)", (symbol[x],company[x],exchange[x],currency[x]))
        print("Successfully added: ", symbol[x])
    except auth.mariadb.Error as e:
        print(f"Error: {e}")

auth.conn.commit()