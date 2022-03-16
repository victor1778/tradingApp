import auth
import json
from twelvedata import TDClient

#Pulls updated data from API into json, then converts it to dictionary    
api = TDClient(apikey="demo")
raw_data = api.get_stocks_list(country="United States").as_raw_json();
assets = json.loads(raw_data)

#Line 9-18 subject to change if more countries needed
insert_stmt = "INSERT INTO tbl_country (countryName) VALUES ('United States')"

#SQL insert 
try:
    auth.mycursor.execute(insert_stmt)
    auth.conn.commit()
    print("Successfully added.")
except auth.mariadb.Error as e:
    print(f"Error: {e}")
    auth.conn.rollback()

auth.conn.close()

"""
PARTLY FUNCTIONAL/WORK IN PROGRESS
"""