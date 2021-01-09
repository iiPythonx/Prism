# Modules
import discord
from json import loads

from random import randint
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Gayness(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Check how gay somebody is (100% legit)"
    self.usage = "gay [user]"

  @commands.command()
  @commands.is_nsfw()
  async def gay(self, ctx, user: discord.User = None):

    db = loads(open("db/guilds", "r").read())

    if "nsfw-enabled" not in db[str(ctx.guild.id)]["tags"]:
      return await ctx.send(embed = Tools.error("NSFW is not enabled in this server."))

    user = await Tools.getClosestUser(ctx, user if user else ctx.author)

    rating = randint(0, 100)
    message = f"You are {rating}% gay."
    
    if ctx.author.id != user.id:
      message = f"{user.name} is {rating}% gay."
        
    # Embed
    embed = discord.Embed(title = message, color = 0x126bf1)
    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Gayness(bot))
