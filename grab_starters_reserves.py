from bs4 import BeautifulSoup
from urllib.request import urlopen
from Player import Player

def get_url():
    url = input("Enter url of boxscore to scrape: ")
    team = input("What team are you scouting? ")
    return url, team

def scrape_boxscore(url, team):
    players = []
    home_vis = ""
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    box = None
    # Find the correct table - search for full-game boxscore of team being scouted, assign it to box
    for table in soup.findAll('table'):
        try:
            if table.caption.h2.span.text == team:
                if 'home' in table.parent.parent.parent.get('class', ''):
                    home_vis = "home"
                else:
                    home_vis = "visitor"
                box = table
                break
        except:
            continue

    starters = box.findAll('tbody')[0]
    for row in starters.findAll('th', attrs={'scope': 'row'}):
        num = row.span.text.split(" -")[0]
        try:
            name = row.a.text
            oua_id = row.a['href']
        except AttributeError:
            name = row.find('span', attrs={'class': 'player-name'}).text
            oua_id = None
        player = Player(name, num, oua_id, "starter")
        players.append(player)

    reserves = box.findAll('tbody')[1]
    for row in reserves.findAll('th', attrs={'scope': 'row'}):
        num = row.span.text.split(" -")[0]
        if num == "TM":
            continue
        try:
            name = row.a.text
            oua_id = row.a['href']

        except AttributeError:
            name = row.find('span', attrs={'class': 'player-name'}).text
            oua_id = None

        player = Player(name, num, oua_id, "reserve")
        players.append(player)

    return players, home_vis
