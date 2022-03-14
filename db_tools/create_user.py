import auth

#change user in user@'%' for username, change '%' to specify database access, and change 'password' to set user passwd.
auth.mycursor.execute("CREATE OR REPLACE USER user@'%' IDENTIFIED BY 'password'")
auth.mycursor.execute("GRANT ALL PRIVILEGES ON *.* TO user@'%' IDENTIFIED BY 'password'")
