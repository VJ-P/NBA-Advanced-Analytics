import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "username",
    passwd = "password",
    database = "nba_2019_stats"   #to be written after the database is created
)

mycursor = mydb.cursor()

my_url = "https://www.basketball-reference.com/leagues/NBA_2019_advanced.html"

#opening the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grab each player
players = page_soup.findAll("tr",{"class":"full_table"})

#open an .csv file to store the information (IF DATA WAS NEEDED IN AN EXCEL FILE)
'''filename = "advancedStats2019.csv"
f = open(filename, "w")
headers = "Player Name, Minutes Played, Games Played, PER, WS, WS48, OWS, DWS, BPM, OBPM, DBPM, VORP, Usage%, TS%, 3PA rate, FTA rate, ORB%, DRB%, TRB%, AST%, STL%, BLK%, TOV% \n"
f.write(headers)'''

#loop to iterate through the html of each player and retrieve each statistic
for player in players:
    minsPlayed = int(player.find("td", {"data-stat" : "mp"}).text)              #get the minutes played for each player to filter non-rotation players, rotational players, and players who haven't played enough games
    gamesPlayed  = int(player.find("td", {"data-stat" : "g"}).text)             #get the games played for each player to filter non-rotation players, rotational players, and players who haven't played enough games
    if minsPlayed < 500 or gamesPlayed < 30:
        continue

    #ID Stats
    playerName   = player.find("td", {"data-stat" : "player"}).a.text           #get the player name

    #Overall Stats
    per          = float(player.find("td", {"data-stat" : "per"}).text)         #get the player efficiency rating
    winShares    = float(player.find("td", {"data-stat" : "ws"}).text)          #get the win shares of the player
    ws48         = float(player.find("td", {"data-stat" : "ws_per_48"}).text)   #get the win shares per 48 mins of the player
    oWS          = float(player.find("td", {"data-stat" : "ows"}).text)         #get the offensive win shares of the player
    dWS          = float(player.find("td", {"data-stat" : "dws"}).text)         #get the defensive win shares of the player
    bPM          = float(player.find("td", {"data-stat" : "bpm"}).text)         #get the box score plus/minus
    obPM         = float(player.find("td", {"data-stat" : "obpm"}).text)        #get the offensive box score plus/minus
    dbPM         = float(player.find("td", {"data-stat" : "dbpm"}).text)        #get the defensive box score plus/minus
    vorp         = float(player.find("td", {"data-stat" : "vorp"}).text)        #get the value over replacement player
    usage        = float(player.find("td", {"data-stat" : "usg_pct"}).text)     #get the usage percentage

    #Shooting Stats
    trueShooting = float(player.find("td", {"data-stat" : "ts_pct"}).text)      #get the true shooting percentage
    threePAR     = float(player.find("td", {"data-stat" : "fg3a_per_fga_pct"}).text)    #get the 3-point attempt rate percentage
    FTAr         = float(player.find("td", {"data-stat" : "fta_per_fga_pct"}).text)     #get the free throw attempt rate

    #Stat Category Percentages
    orebPCT      = float(player.find("td", {"data-stat" : "orb_pct"}).text)     #get the offensive rebouding percentage
    drebPCT      = float(player.find("td", {"data-stat" : "drb_pct"}).text)     #get the defensive rebouding percentage
    reboundPCT   = float(player.find("td", {"data-stat" : "trb_pct"}).text)     #get the total rebouding percentage
    assistPCT    = float(player.find("td", {"data-stat" : "ast_pct"}).text)     #get the assist percentage
    stealPCT     = float(player.find("td", {"data-stat" : "stl_pct"}).text)     #get the steal percentage
    blockPCT     = float(player.find("td", {"data-stat" : "blk_pct"}).text)     #get the block percentage
    tovPCT       = float(player.find("td", {"data-stat" : "tov_pct"}).text)     #get the turnover percentage

    sql = "INSERT INTO players_advanced (playerName, minutesPlayed, gamesPlayed, PER, WS, WS48, OWS, DWS, BPM, OBPM, DBPM, VORP, UsagePercent, TSpercent, 3PArate, FTArate, ORBpercent, DRBpercent, TRBpercent, ASTpercent, STLpercent, BLKpercent, TOVpercent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (playerName, minsPlayed, gamesPlayed, per, winShares, ws48, oWS, dWS, bPM, obPM, dbPM, vorp, usage, trueShooting, threePAR, FTAr, orebPCT, drebPCT, reboundPCT, assistPCT, stealPCT, blockPCT, tovPCT)
    mycursor.execute(sql, val)
    mydb.commit()

    #Write to excel spreadsheet (IF DATA WAS NEEDED IN AN EXCEL FILE)
    '''f.write(playerName + "," + str(minsPlayed) + "," + str(gamesPlayed) + "," + str(per) + "," + str(winShares) + "," + str(ws48) + "," + str(oWS) + "," + str(dWS) + "," + str(bPM) + ",")
    f.write(str(obPM) + "," + str(dbPM) + "," + str(vorp) + "," + str(usage) + "," + str(trueShooting) + "," + str(threePAR) + "," + str(FTAr) + "," + str(orebPCT) + "," + str(drebPCT) + ",")
    f.write(str(reboundPCT) + "," + str(assistPCT) + "," + str(stealPCT) + "," + str(blockPCT) + "," + str(tovPCT) +"\n")'''

#IF DATA WAS NEEDED IN AN EXCEL FILE
'''f.close()'''
