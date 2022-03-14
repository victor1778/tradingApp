import auth

auth.mycursor.execute("CREATE TABLE IF NOT EXISTS stock(id INT AUTO_INCREMENT PRIMARY KEY, symbol VARCHAR(255), company VARCHAR(255), exchange VARCHAR(255))")