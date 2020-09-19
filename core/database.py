# Modules
import sqlite3

# Classes
class User():

    def __init__(self, resp, user):
        self.balance = resp[1]
        self.level = resp[2]
        self.experience = resp[3]
        self.user = user
        self.has_acc = True if self.user else False

# SQLite Functions
def sql_identifier(s):

  return "\"" + s.replace("\"", "\"\"") + "\""

def get_key(cursor, table, user, key):

    cursor.execute(f"SELECT * FROM {table} WHERE id=?", (user.id,))
    
    item = cursor.fetchone()

    return User(item if item else None, user)

# Classes
class Users():

  def __init__(self):

    self.conn = sqlite3.connect("prism.db")
    self.cursor = self.conn.cursor()

  def get_user(self, user):

    return get_key(self.cursor, "users", user)

  def setup_user(self, id):

    self.cursor.execute("INSERT INTO users VALUES (?,?,?,?)", (id, 250, 1, 0))

  def save(self):

    self.conn.commit()

    self.conn.close()

class Guilds():

  def __init__(self):

    self.conn = sqlite3.connect("prism.db")
    self.cursor = self.conn.cursor()

  def get_guild(self, id, key = None):

    return get_key(self.cursor, "guilds", id, key)

  def setup_guild(self, id):

    self.cursor.execute("INSERT INTO guilds VALUES (?,?)", (id, "p!"))

  def save(self):

    self.conn.commit()

    self.conn.close()

# Setup function
def setup():

  print("Setting up database..")

  db = sqlite3.connect("prism.db")
  cur = db.cursor()

  print("[db]: Created database file.")

  cur.execute("CREATE TABLE users (id bigint, balance int, level int, xp int)")

  cur.execute("CREATE TABLE guilds (id bigint, prefix text)")

  print("[db]: Tables created.")

  db.commit()

  db.close()

  print("[db]: Database saved.")
