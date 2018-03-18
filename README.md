# oua-mbb-combos
python project for Ontario University Basketball coaching staff to analyze opponents' 5-man rotation patterns

### Dependencies:
```
from urllib.request import urlopen\
from bs4 import BeautifulSoup\
import time\
import copy\
import traceback
```
To use the program, `python3 analyze_game.py`\
You will be asked for two inputs, one after the other\
It will look as follows\
Enter url of boxscore to scrape: http://www.oua.ca/sports/mbkb/2017-18/boxscores/20180126_d1sm.xml?view=plays\
What team are you scouting? Carleton\

The output will be a list of every single 5-man unit the team played in that game, along with the length of time, points scored, points, against and +/-\
Unfortunately, the oua.ca data is not complete, so there are mistakes in the output. I will continue to try to make this output as correct as possible given the data's limitations.

Enjoy and hopefully you find this program useful!
