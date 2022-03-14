import auth

auth.mycursor.execute("CREATE OR REPLACE USER user@'%' IDENTIFIED BY 'password'")
auth.mycursor.execute("GRANT ALL PRIVILEGES ON *.* TO user@'%' IDENTIFIED BY 'password'")
