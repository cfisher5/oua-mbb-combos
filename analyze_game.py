from grab_starters_reserves import *
from Rotation import Rotation
from Unit import Unit
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import copy
import traceback

url, team = get_url()
players, home_vis = scrape_boxscore(url, team)

print("")
rotation = Rotation()
starters = []
for player in players:
    if player.type == "starter":
        starters.append(player)

initial_unit = Unit(starters)
initial_unit.toc_b = "10:00"
initial_unit.q = "prd1"

page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

unit = initial_unit
if home_vis == "home":
    td_index = 1
else:
    td_index = 0

for quarter in soup.findAll('table', attrs={'role': 'presentation'}):
    q = quarter.caption.h2.span.get("id", "")
    for entry in quarter.findAll('tr', attrs={'class': home_vis}):

        try:
            tds = entry.findAll('td', attrs={'class': 'play'})

            num_players_switching = 0
            keep_checking = True
            if "enters the game" in tds[td_index].span.text:

                time_left = entry.find("td", attrs={'class': 'time'}).text
                # don't create a new unit
                if time_left == unit.toc_b:
                    continue

                unit.toc_e = time_left

                players_out = []
                players_in = []
                name = tds[td_index].span.text.strip().split("  ")[0].replace("\n", "")
                players_in.append(name)
                num_players_switching += 1
                temp = entry

                while(keep_checking):
                    next = temp.next_sibling.next_sibling.findAll('td', attrs={'class': 'play'})[td_index].span.text
                    if "enters the game" in next:
                        num_players_switching += 1
                        name = next.strip().split("  ")[0].replace("\n", "")
                        players_in.append(name)
                        temp = temp.next_sibling.next_sibling
                    else:
                        keep_checking = False



                if num_players_switching == 1:
                    players_out.append(entry.next_sibling.next_sibling.findAll('td', attrs={'class': 'play'})[td_index].span.text.strip().split("  ")[0].replace("\n", ""))

                elif num_players_switching == 2:
                    players_out.append(entry.next_sibling.next_sibling.next_sibling.next_sibling.findAll('td', attrs={'class': 'play'})[
                                           td_index].span.text.strip().split("  ")[0].replace("\n", ""))
                    players_out.append(entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll('td', attrs={
                        'class': 'play'})[td_index].span.text.strip().split("  ")[0].replace("\n", ""))

                elif num_players_switching == 3:
                    players_out.append(entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll('td', attrs={'class': 'play'})[
                                           td_index].span.text.strip().split("  ")[0].replace("\n", ""))
                    players_out.append(entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll('td', attrs={
                        'class': 'play'})[td_index].span.text.strip().split("  ")[0].replace("\n", ""))
                    players_out.append(
                        entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll(
                            'td', attrs={
                                'class': 'play'})[td_index].span.text.strip().split("  ")[0].replace("\n", ""))

                else:
                    players_out.append(
                        entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll(
                            'td', attrs={'class': 'play'})[
                            td_index].span.text.strip().split("  ")[0].replace("\n", ""))
                    players_out.append(
                        entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll(
                            'td', attrs={
                                'class': 'play'})[td_index].span.text.strip().split("  ")[0].replace("\n", ""))
                    players_out.append(
                        entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll(
                            'td', attrs={
                                'class': 'play'})[td_index].span.text.strip().split("  ")[0].replace("\n", ""))
                    players_out.append(
                        entry.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.findAll(
                            'td', attrs={
                                'class': 'play'})[td_index].span.text.strip().split("  ")[0].replace("\n", ""))


                h_for = int(entry.find('td', attrs={'class': 'score'}).find('span', attrs={'class': 'h-score'}).text)
                v_for = int(entry.find('td', attrs={'class': 'score'}).find('span', attrs={'class': 'v-score'}).text)

                # calculate points for + against
                if home_vis == "home":
                    unit.pts_for = h_for - unit.old_pts_for
                    unit.pts_against = v_for - unit.old_pts_against
                else:
                    unit.pts_for = v_for - unit.old_pts_for
                    unit.pts_against = h_for - unit.old_pts_against


                # calculate min
                beg_min, beg_sec = unit.toc_b.split(":")
                total_beg_time = int(beg_min) * 60 + int(beg_sec)

                end_min, end_sec = time_left.split(":")
                total_end_time = int(end_min) * 60 + int(end_sec)

                if q != unit.q:
                    # quarter change
                    total_time = total_beg_time + (600 - total_end_time)
                else:
                    total_time = total_beg_time - total_end_time

                unit.edit_min(time.strftime('%M:%S', time.gmtime(total_time)))

                print("Game Clock: " + unit.toc_b + " - " + time_left)
                print("Time Elapsed: " + unit.min)
                print("Players:")
                for player in unit.players:
                    print(player.name, end="  |  ")
                print("")
                print("Points For: " + str(unit.pts_for))
                print("Points Against: " +str(unit.pts_against))

                print("+/- " + str(unit.pts_for - unit.pts_against))
                print("*******************************************************\n")

                # create new unit
                players_copy = copy.deepcopy(unit.players)

                for p_name in players_out:
                    for player in players_copy:
                        if p_name == player.pbp_name:
                            players_copy.remove(player)

                for incoming_player in players_in:
                    for player in players:
                        if incoming_player == player.pbp_name:
                            exists = False
                            for p in players_copy:
                                if p.pbp_name == incoming_player:
                                    print(incoming_player + " is already in unit")
                                    exists = True
                            if not exists:
                                players_copy.append(player)
                                break

                print("PLAYERS IN: " + str(players_in))
                print("PLAYERS OUT: " + str(players_out))

                # print("NEW UNIT:")
                # for player in players_copy:
                #     print(player.name)

                rotation.add_unit(unit)
                new_unit = Unit(players_copy)
                new_unit.toc_b = time_left
                new_unit.q = q
                if home_vis == "home":
                    new_unit.old_pts_for = h_for
                    new_unit.old_pts_against = v_for

                else:
                    new_unit.old_pts_for = v_for
                    new_unit.old_pts_against = h_for
                unit = new_unit

        except AttributeError:
            traceback.print_exc()

