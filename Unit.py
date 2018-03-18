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

