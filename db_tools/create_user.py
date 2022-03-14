import auth

#mycursor.execute("CREATE DATABASE mydatabase")
auth.mycursor.execute("CREATE OR REPLACE USER user@'%' IDENTIFIED BY 'password'")
auth.execute("GRANT ALL PRIVILEGES ON *.* TO user@'%' IDENTIFIED BY 'password'")
