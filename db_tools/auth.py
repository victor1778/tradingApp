import mariadb
import sys

try:
    conn = mariadb.connect(
        user="#",
        password="#",
        host="#",
        port=3306,
        database="test"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

mycursor = conn.cursor(dictionary = True)
