import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "username",
    passwd = "password",
    database = "nba_2019_stats"   #to be written after the database is created
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM players_advanced")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
