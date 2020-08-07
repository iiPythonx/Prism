# Prism Rewrite - Basic Command

# Modules
import json
import discord

import requests
from discord.ext import commands

# Main Command Class
class Covid(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Fetches COVID-19 stats"
        self.usage = "covid"

        self.url = "https://covid-simple-api.now.sh/api/world"

    @commands.command(aliases = ["corona"])
    async def covid(self, ctx):

        response = json.loads(requests.get(self.url).text)

        stats = f"""Active Cases (worldwide): {response["activeCases"]}\nClosed Cases (worldwide): {response["closedCases"]}\n\nTotal Cases (worldwide): {response["totalCases"]}\nRecovered (worldwide): {response["recovered"]}\nDeaths (worldwide): {response["deaths"]}\n\nLast update: {response["lastUpdate"]}"""

        embed = discord.Embed(title = stats, color = 0x126bf1)
        
        embed.set_author(name = " | Coronavirus", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Covid(bot))
