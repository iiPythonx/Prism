# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Hold(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Give your pet something to hold"
    self.usage = "hold [item]"

  @commands.command()
  async def hold(self, ctx, *, item: str = None):

    db = loads(open("db/users", "r").read())

    if not item:

      return await ctx.send(embed = Tools.error("You need to specify an item."))

    elif not db[str(ctx.author.id)]["pet"]["level"]:

      return await ctx.send(embed = Tools.error("You don't own a pet."))
 
    elif db[str(ctx.author.id)]["pet"]["holding"]:

      return await ctx.send(embed = Tools.error("Your pet is already holding an item; try the ``takeback`` command."))

    for inv_item in db[str(ctx.author.id)]["data"]["inventory"]:

      if inv_item.lower() == item.lower():

        item = inv_item

    if not item in db[str(ctx.author.id)]["data"]["inventory"]:

      return await ctx.send(embed = Tools.error("You don't have that item in your inventory."))

    db[str(ctx.author.id)]["data"]["inventory"][item]["count"] -= 1

    if db[str(ctx.author.id)]["data"]["inventory"][item]["count"] == 0:

      db[str(ctx.author.id)]["data"]["inventory"].remove(item)

    db[str(ctx.author.id)]["pet"]["holding"] = item

    open("db/users", "w").write(dumps(db, indent = 4))

    embed = discord.Embed(title = f"Your pet is now holding a {item}.", color = 0x126bf1)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Hold(bot))
