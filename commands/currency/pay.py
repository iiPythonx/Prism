# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Pay(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Pay somebody some coins"
    self.usage = "pay [user] [amount]"

  @commands.command()
  async def pay(self, ctx, user = None, amount = None):

    if not user:
        
      return await ctx.send(embed = Tools.error("No user specified to pay."))
    
    elif not amount:
        
      return await ctx.send(embed = Tools.error("No amount specified to pay."))
    
    user = await Tools.getClosestUser(ctx, user)

    if user.id == ctx.author.id:
        
      return await ctx.send(embed = Tools.error("No paying yourself. >:C"))
    
    elif user.id == self.bot.user.id:
        
      return await ctx.send(embed = Tools.error("I don't need your coins. thx doe :D"))
    
    db = loads(open("db/users", "r").read())

    try:

      amount = int(amount)

      if len(str(amount)) > 100:

        return await ctx.send(embed = Tools.error("That is way too many coins."))

      elif amount <= 0:

        return await ctx.send(embed = Tools.error("Please enter a valid amount."))

    except:

      if amount != "all":

        return await ctx.send(embed = Tools.error("Please enter a valid amount."))

      else:

        amount = db[str(ctx.author.id)]["balance"]
    
    if not str(user.id) in db:
        
      return await ctx.send(embed = Tools.error(f"{user.name} doesn't have an account."))
        
    elif db[str(ctx.author.id)]["balance"] < amount:

      return await ctx.send(embed = Tools.error(f"You don't have that many coins in your account."))

    db[str(ctx.author.id)]["balance"] -= amount
    
    db[str(user.id)]["balance"] += amount
        
    open("db/users", "w").write(dumps(db, indent = 4))
        
    embed = discord.Embed(title = f"{user.name} has been payed {amount} coins.", color = 0x126bf1)
    
    embed.set_author(name = " | Balance Update", icon_url = self.bot.user.avatar_url)
    
    embed.set_footer(text = f" | Transaction initiated by {ctx.author}.", icon_url = ctx.author.avatar_url)
    
    try:

      return await ctx.send(embed = embed)

    except:

      embed = discord.Embed(title = f"{user.name} has been payed your entire balance.", color = 0x126bf1)
    
      embed.set_author(name = " | Balance Update", icon_url = self.bot.user.avatar_url)
      
      embed.set_footer(text = f" | Transaction initiated by {ctx.author}.", icon_url = ctx.author.avatar_url)
      
      return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Pay(bot))
