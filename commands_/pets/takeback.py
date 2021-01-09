# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Takeback(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Grab whatever your pet is holding"
    self.usage = "takeback"

  @commands.command()
  async def takeback(self, ctx,):

    db = loads(open("db/users", "r").read())

    if not db[str(ctx.author.id)]["pet"]["level"]:

      return await ctx.send(embed = Tools.error("You don't own a pet."))
 
    elif not db[str(ctx.author.id)]["pet"]["holding"]:

      return await ctx.send(embed = Tools.error("Your pet isn't holding an item."))

    user = db[str(ctx.author.id)]

    if user["pet"]["holding"] in user["data"]["inventory"] and user["data"]["inventory"][user["pet"]["holding"]]["count"] > 999:

        return await ctx.send(embed = Tools.error("You have too many of those in your inventory; sell an item."))

    elif user["pet"]["holding"] in user["data"]["inventory"]:

        user["data"]["inventory"][user["pet"]["holding"]]["count"] += 1

    else:

        user["data"]["inventory"][user["pet"]["holding"]] = {"count": 1}

    db[str(ctx.author.id)]["pet"]["holding"] = None

    open("db/users", "w").write(dumps(db, indent = 4))

    embed = discord.Embed(title = f"You grabbed the item from your pet.", color = 0x126bf1)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Takeback(bot))
