# Modules
from os import getenv
from dbl import DBLClient

from discord.ext import commands

# Main extension class
class TopGG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.__postinit__()

    def __postinit__(self):

        token = getenv("DBL_TOKEN")
        if token is None or not token:
            return

        self.token = token
        self.client = DBLClient(
            self.bot,
            self.token,
            autopost = True
        )

# Link to le' bot
def setup(bot):
    bot.add_cog(TopGG(bot))
