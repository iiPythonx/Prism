# Modules
import sqlite3

# Classes
class Users():

    def __init__(self):

        self.connection = sqlite3.connect("db/users.db")
        self.cursor = self.connection.cursor()

class Guilds():

    def __init__(self):
        
        self.connection = sqlite3.connect("db/guilds.db")
        self.cursor = self.connection.cursor()

# Setup function
def setup():

    u = Users()
    g = Guilds()

    u.cursor.execute("CREATE TABLE users (id int)")
    g.cursor.execute("CREATE TABLE guilds (id int)")

    u.connection.commit()
    g.connection.commit()

    u.connection.close()
    g.connection.close()
