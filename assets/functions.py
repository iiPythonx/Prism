# assets/functions.py
# Just a bunch of helpful functions that DO NOT require the bot instance.

# Modules
from os import name, system
from json import loads, dumps

# Functions
def clear():

    if name == "nt":

      system("cls")

    elif name == "posix":

      system("clear")

    else:

        raise SystemError("This is an unsupported operating system.")

def server_check(bot):

    constant = loads(open("db/guilds", "r").read())

    data = loads(open("db/guilds", "r").read())
    
    for server in constant:
        
      if not bot.get_guild(int(server)):
          
        data.pop(server)
            
    for server in bot.guilds:
        
      if not str(server.id) in constant:
            
        data[str(server.id)] = Constants.guild_preset
    
    open("db/guilds", "w").write(dumps(data, indent = 4))

    data = loads(open("db/users", "r").read())

    for user in data:

      if "protected" in data[user]["data"]["tags"]:

        data[user]["data"]["tags"].remove("protected")

    open("db/users", "w").write(dumps(data, indent = 4))
