# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Withdraw(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Takes coins in your bank"
    self.usage = "withdraw [amount]"

  @commands.command(aliases = ["wd", "with"])
  async def withdraw(self, ctx, amount = None):

    if not amount:

      return await ctx.send(embed = Tools.error("No amount was specified to withdraw."))

    db = loads(open("db/users", "r").read())

    user = db[str(ctx.author.id)]

    if not user["bank"]["data"]:

      return await ctx.send(embed = Tools.error("You don't have a bank account, get one with the `bank` command."))

    if amount == "all":

      amount = user["bank"]["balance"]

    else:

      try:

        amount = int(amount)

      except:

        return await ctx.send(embed = Tools.error("That isn't a valid amount."))

    if amount > user["bank"]["balance"]:

        return await ctx.send(embed = Tools.error("You don't have that much money in your bank."))

    user["balance"] += amount

    user["bank"]["balance"] -= amount

    open("db/users", "w").write(dumps(db, indent = 4))

    if len(str(amount)) > 5:

      a = len(str(amount)) - 5

      amount = str(amount[:-a]) + ".."

    return await ctx.send(embed = discord.Embed(title = f"{amount} coins withdrew from bank.", color = 0x126bf1))

# Link to bot
def setup(bot):
  bot.add_cog(Withdraw(bot))
