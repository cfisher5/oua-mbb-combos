class Player:

    def __init__(self, name, number, oua_id, type):
        self.name = name
        self.number = number
        self.oua_id = oua_id
        self.type = type
        self.pbp_name = self.alter_name()

    def alter_name(self):
        names = self.name.split(" ")
        if len(names) == 2:
            new_name = names[1].upper() + "," + names[0].upper()
        else:
            new_name = names[2].upper() + "," + names[0].upper() + " " + names[1].upper()
        return new_name