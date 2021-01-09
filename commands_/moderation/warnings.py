# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Warnings(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Checks a users warnings on the server"
    self.usage = "warnings [user]"
        
  @commands.command(aliases = ["warns"])
  async def warnings(self, ctx, user: discord.Member = None):
    
    if not user:
        
        user = ctx.author
    
    elif user.id == self.bot.user.id:
        
        return await ctx.send(embed = Tools.error("I don't have any warnings."))

    db = loads(open("db/users", "r").read())

    if not str(user.id) in db or not str(ctx.guild.id) in db[str(user.id)]["data"]["warnings"]:

      title = f"{user.name} doesn't have any warnings on this server."

      if ctx.author.id == user.id:

        title = "You don't have any warnings on this server."

      return await ctx.send(embed = Tools.error(title))

    warnings = ""

    for warning in db[str(user.id)]["data"]["warnings"][str(ctx.guild.id)]:

      warnings = f"{warnings}{warning}\n"

    title = f"{user.name}'s Warnings"

    if ctx.author.id == user.id:

      title = "Your Warnings"

    embed = discord.Embed(title = title, description = warnings, color = 0x126bf1)

    embed.set_author(name = " | Warnings", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Warnings(bot))
