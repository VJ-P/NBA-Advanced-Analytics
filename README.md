# NBA-Advanced-Analytics
A  webscraper designed in python to scrape the advanced analytics for every player from basketball-reference.com. The scraper filters out injured and non-rotational players and store everything into a MySQL database.

To run, first run the createNbaDatabase.py script, followed by the BBallRefWebScraper.py script. The database can then be used in the usedata.py script. An initial edit to connect to your SQL server will need to be made at the top of each script.
