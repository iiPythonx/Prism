# Modules
import discord
from json import loads

from requests import get
from discord.ext import commands

# Main Command Class
class Dog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Gets you a random picture of a dog"
        self.usage = "dog"

    @commands.command(aliases = ["doggo", "puppy"])
    async def dog(self, ctx):

        embed = discord.Embed(color = 0x126bf1)
        
        embed.set_image(url = loads(get("https://dog.ceo/api/breeds/image/random").text)["message"])
        
        embed.set_author(name = " | Dog", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Dog(bot))
