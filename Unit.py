class Unit:

    def __init__(self, players):
        self.players = players
        self.min = 0.0
        self.pts_for = 0
        self.q = None
        self.pts_against = 0
        self.old_pts_for = 0
        self.old_pts_against = 0
        self.toc_b = None
        self.toc_e = None

    def edit_min(self, min):
        self.min = min

    def print_info(self):
        print("Game Clock: " + self.toc_b + " - " + self.toc_e)
        print("Time Elapsed: " + self.min)
        print("Players:")
        for player in self.players:
            print(player.name, end="  |  ")
        print("")
        print("Old Points For: " + str(self.old_pts_for))
        print("Old Points Against: " + str(self.old_pts_against))
        print("Points For: " + str(self.pts_for))
        print("Points Against: " + str(self.pts_against))

        print("+/- " + str(self.pts_for - self.pts_against))
        print("*******************************************************\n")