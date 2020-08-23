# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Deposit(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Puts coins in your bank"
    self.usage = "deposit [amount]"

  @commands.command(aliases = ["dep"])
  async def deposit(self, ctx, amount = None):

    if not amount:

      return await ctx.send(embed = Tools.error("No amount was specified to deposit."))

    db = loads(open("db/users", "r").read())

    user = db[str(ctx.author.id)]

    if not user["bank"]["data"]:

      return await ctx.send(embed = Tools.error("You don't have a bank account, get one with the `bank` command."))

    limit = int(user["bank"]["data"]["limit"].replace(",", ""))

    if user["bank"]["balance"] == limit:

      return await ctx.send(embed = Tools.error("You're bank is full."))

    if amount == "all":

      amount = user["balance"]

    else:

      try:

        amount = int(amount)

      except:

        return await ctx.send(embed = Tools.error("That isn't a valid amount."))

    todeposit = 0

    if amount + user["bank"]["balance"] > limit:

      todeposit = limit - user["bank"]["balance"]

    else:

      todeposit = amount

    user["balance"] -= todeposit

    user["bank"]["balance"] += todeposit

    open("db/users", "w").write(dumps(db, indent = 4))

    if len(str(todeposit)) > 5:

      a = len(str(todeposit)) - 5

      todeposit = str(todeposit[:-a]) + ".."

    return await ctx.send(embed = discord.Embed(title = f"{todeposit} coins deposited to bank.", color = 0x126bf1))

# Link to bot
def setup(bot):
  bot.add_cog(Deposit(bot))
