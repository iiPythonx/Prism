# Modules
from json import loads, dumps

# Master effect class
class Effects(object):

    def __init__(self, id):

        self.id = str(id)

        self.db = loads(open("db/users", "r").read())
        self.data = self.db[self.id]["data"]
        
        self.effects = self.data["effects"]

        self.refresh_data()

    def __len__(self):

        return len(self.effects)

    def refresh_data(self):

        self.db = loads(open("db/users", "r").read())

        self.data = self.db[self.id]["data"]

    def dump_data(self):

        open("db/users", "w").write(dumps(self.db, indent = 4))

    def add_effect(self, name, duration):

        refresh_data()

        self.data["effects"][name] = duration

        dump_data()
