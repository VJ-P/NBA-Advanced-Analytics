import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "username",
    passwd = "password",
    database = "nba_2019_stats"   #to be written after the database is created
)

mycursor = mydb.cursor()

#create mysql database
'''mycursor.execute("CREATE DATABASE nba_2019_stats")'''

'''mycursor.execute("DROP TABLE players_advanced")'''

#create table for players
mycursor.execute("CREATE TABLE players_advanced (playerName VARCHAR(255), minutesPlayed INT(10), gamesPlayed INT(5), PER FLOAT, WS FLOAT, WS48 FLOAT, OWS FLOAT, DWS FLOAT, BPM FLOAT, OBPM FLOAT, DBPM FLOAT, VORP FLOAT, UsagePercent FLOAT, TSpercent FLOAT, 3PArate FLOAT, FTArate FLOAT, ORBpercent FLOAT, DRBpercent FLOAT, TRBpercent FLOAT, ASTpercent FLOAT, STLpercent FLOAT, BLKpercent FLOAT, TOVpercent FLOAT)")
