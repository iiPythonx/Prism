# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads

from requests import get
from discord.ext import commands

# Main Command Class
class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Fresh memes coming straight at you"
        self.usage = "meme"

    @commands.command(aliases = ["memes"])
    async def meme(self, ctx):
        
        embed = discord.Embed(color = 0x126bf1)
        
        embed.set_image(url = loads(get("https://meme-api.glitch.me/moderate").text)["meme"])
        
        embed.set_author(name = " | Meme", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Meme(bot))
