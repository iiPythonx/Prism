# Modules
import discord
from os import getenv
from json import loads

from requests import get
from discord.ext import commands

# Main Command Class
class Cat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Gets you a random picture of a cat"
        self.usage = "cat"

        self.key = getenv("CAT_KEY")

    @commands.command(aliases = ["kitten"])
    async def cat(self, ctx):

        url = "https://api.thecatapi.com/v1/images/search"

        headers = {
            "x-api-key": self.key
        }

        data = loads(get(url, headers = headers).text)

        embed = discord.Embed(color = 0x126bf1)
        
        embed.set_image(url = data[0]["url"])
        
        embed.set_author(name = " | Cat", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Cat(bot))