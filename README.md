# oua-mbb-combos
python project for Ontario University Basketball coaching staff to analyze opponents' 5-man rotation patterns

### Dependencies:
```
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import copy
import traceback
```
To use the program, `python3 analyze_game.py`\
You will be asked for two inputs, one after the other\
It will look as follows\
```
Enter url of boxscore to scrape: http://www.oua.ca/sports/mbkb/2017-18/boxscores/20180126_d1sm.xml?view=plays
What team are you scouting? Carleton
```

The output will be a list of every single 5-man unit the team played in that game, along with the length of time, points scored, points against and +/-

Unfortunately, the oua.ca play-by-play data is not complete/error-prone so there are mistakes in the output. I will continue to try to make this output as correct as possible given the data's limitations.

For now, my current work-around is to have the user input the 5 players in the game at the start of the 2nd, 3rd and 4th quarters. The OUA play-by-play data seems to be incomplete/wrong at the beginning of quarters.

Make sure to enter the players' names in the following format: `Alan Smith`

To deduce which players are playing at the start of each quarter, consult the play-by-play data.

Enjoy and hopefully you find this program useful!
