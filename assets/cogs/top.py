# Modules
from os import getenv
from dbl import DBLClient

from discord.ext import commands

# Main extension class
class TopGG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = getenv("DBL_TOKEN")
        self.dblpy = DBLClient(self.bot, self.token, autopost = True)

# Link to le' bot
def setup(bot):
    bot.add_cog(TopGG(bot))
    