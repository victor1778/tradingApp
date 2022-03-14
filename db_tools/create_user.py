import auth

#mycursor.execute("CREATE DATABASE mydatabase")
auth.mycursor.execute("CREATE OR REPLACE USER interlinked@'%' IDENTIFIED BY '1778'")
auth.execute("GRANT ALL PRIVILEGES ON *.* TO interlinked@'%' IDENTIFIED BY '1778'")