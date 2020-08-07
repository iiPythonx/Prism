# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads

from requests import get
from discord.ext import commands

# Main Command Class
class Joke(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Get a random joke pretty much everytime"
    self.usage = "joke"

  @commands.command(aliases = ["funny", "laugh"])
  async def joke(self, ctx):

    embed = discord.Embed(title = loads(get("https://icanhazdadjoke.com", headers = {"Accept": "application/json"}).text)["joke"], color = 0x126bf1)
    
    embed.set_author(name = " | Joke", icon_url = self.bot.user.avatar_url)
    
    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Joke(bot))
