# Modules
import discord
from requests import get

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Covid(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Fetches COVID-19 stats"
        self.usage = "covid"

        self.url = "https://covid-simple-api.now.sh/api/world"

    @commands.command(aliases = ["corona", "covid19"])
    async def covid(self, ctx):

        try:

            r = get(self.url, timeout = 10).json()

        except:

            return await ctx.send(embed = Tools.error("API is currently down, try again later."))

        embed = discord.Embed(title = "Coronavirus Pandemic", description = ":mask: Make sure you wear a mask!", color = 0x126bf1)
        
        embed.add_field(name = "Active", value = f"`{r['activeCases']}`")

        embed.add_field(name = "Recovered", value = f"`{r['recovered']}`")

        embed.add_field(name = "Closed", value = f"`{r['closedCases']}`")

        embed.add_field(name = "Deaths", value = f"`{r['deaths']}`")

        embed.add_field(name = "Total", value = f"`{r['totalCases']}`")

        embed.set_author(name = " | Covid-19", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}. | Last updated on {r['lastUpdate']}", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Covid(bot))
