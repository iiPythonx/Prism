# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads

from requests import get
from random import choice

from discord.ext import commands

# Main Command Class
class Janeway(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Gets you a random GIF of Janeway from Star Trek"
        self.usage = "janeway"
        
        self.api_key = "aueuUJZDMDGgjEjYaIn3kDPSPugvG98N"
        self.api_url = "https://api.giphy.com/v1/gifs/search"
        self.headers = {"api_key": self.api_key, "q": "janeway", "lang": "en"}

    @commands.command(aliases = ["jw"])
    async def janeway(self, ctx):

        embed = discord.Embed(color = 0x126bf1)
        
        embed.set_image(url = choice(loads(get(self.api_url, self.headers).text)["data"])["images"]["downsized_large"]["url"])
        
        embed.set_author(name = " | Janeway", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Janeway(bot))
    