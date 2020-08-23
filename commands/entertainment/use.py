# Modules
import discord
from random import randint

from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Use(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Consume / use an item in your inventory"
        self.usage = "use [item]"

    @commands.command(aliases = ["consume"])
    async def use(self, ctx, item: str = None):

        if not item:

            return await ctx.send(embed = Tools.error("No item specified to use."))

        return await ctx.send(embed = Tools.error("This command is coming in `v1.4`."))

# Link to bot
def setup(bot):
    bot.add_cog(Use(bot))
