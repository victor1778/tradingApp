import mariadb
import sys

try:
    conn = mariadb.connect(
        user="interlinked",
        password="Temporal2022+",
        host="localhost",
        port=3306,
        database="billionsdb"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

mycursor = conn.cursor(dictionary = True)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
from fastapi.encoders import jsonable_encoder
templates = Jinja2Templates(directory="templates")

@app.get("/get")
async def get_tickers():
    #Pulls existing data from SQL database
    mycursor.execute("SELECT idTicker, symbol, name FROM tbl_ticker")
    rows = mycursor.fetchall()
    return rows
    #return templates.TemplateResponse("index.html", {"request": request, "tickers": rows})
