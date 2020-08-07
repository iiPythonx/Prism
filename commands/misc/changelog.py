# Prism Rewrite - Basic Command

# Modules
import json
import discord

from discord.ext import commands

# Main Command Class
class Changelog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Checks the bots changelog"
        self.usage = "changelog"

    @commands.command(aliases = ["version", "cl", "updates", "update"])
    async def changelog(self, ctx):
 
        latest_update = json.loads(open("assets/res/plain-text/update.txt", "r").read())

        if ctx.author in self.bot.get_guild(729513002302177311).members:

          message = f"Click here to check the changelog:\n{latest_update['jumpurl']}"

          return await ctx.send(message)

        return await ctx.send(embed = latest_update["content"])

# Link to bot
def setup(bot):
    bot.add_cog(Changelog(bot))
