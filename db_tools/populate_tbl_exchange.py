import auth
import json
from twelvedata import TDClient

#Array declaration
placeholder = []
exchange = []

#Subject to change
country = 1 

#Pulls updated data from API into json, then converts it to dictionary
api = TDClient(apikey="demo")
raw_data = api.get_stocks_list(country="United States").as_raw_json();
assets = json.loads(raw_data)

#Pulls existing data from SQL database
auth.mycursor.execute("SELECT exchangeName FROM tbl_exchange")
rows = auth.mycursor.fetchall()
temp = [row['exchangeName'] for row in rows]

#Compares updated json with existing db, and only adds new entries to placeholder
for data in assets['data']:
    if data['exchange'] not in temp:
        placeholder.append(data['exchange'])

#Duplicate elimination
for x in placeholder:
    if x not in exchange:
        exchange.append(x)

#SQL insert    
for x in range(0, len(exchange), 1):
    try:
        auth.mycursor.execute("INSERT INTO tbl_exchange(exchangeName, idCountry) VALUES (?,?)", (exchange[x], country))
        print("Successfully added: ", exchange[x])
        auth.conn.commit()
    except auth.mariadb.Error as e:
        print(f"Error: {e}")
        auth.conn.rollback()

auth.conn.close()