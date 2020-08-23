# Modules
from asyncio import sleep
from json import loads, dumps

from discord.ext import commands
from assets.prism import Tools, Cooldowns

# Main Command Class
class Buy(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Purchase an item from the shop"
    self.usage = "buy [id]"

  def save(self, db):

    return open("db/users", "w").write(dumps(db, indent = 4))

  async def purchase(self, ctx, id, amount):

    id, db, items = str(id), loads(open("db/users", "r").read()), loads(open("assets/res/items.json", "r").read())

    if not str(id) in items:

      return await ctx.send(embed = Tools.error("Invalid item ID!"))

    user = db[str(ctx.author.id)]

    item = items[id]

    if not user["balance"] >= item["price"]:

      return await ctx.send(embed = Tools.error("You don't have enough coins."))

    elif "premium" in item["tags"] and not "premium" in user["data"]["tags"]:

      return await ctx.send(embed = Tools.error("You need premium to purchase that."))

    elif ":" in item["name"]:

      if ">" in item["name"]:

        item["name"] = item["name"].split(">")[1]

      else:

        item["name"] = item["name"].split(":")[2]

      if item["name"].startswith(" "):

        item["name"] = item["name"][1:]
        
    if "banklock" in item["tags"]:

      if amount > 1:

        return await ctx.send(embed = Tools.error("You cannot buy more than 1 bank lock."))

      for tag in item["tags"]:

        if tag.startswith("duration-"):

          duration = int(tag.split("duration-")[1])

      if not "protected" in user["data"]["tags"]:

        user["data"]["tags"].append("protected")

      else:

        return await ctx.send(embed = Tools.error("You already have a bank lock active."))

      self.save(db)

      await ctx.send(embed = Tools.bought(item["name"], 1))

      await sleep(duration)

      user["data"]["tags"].remove("protected")

      self.save(db)

    elif item["name"] == "Cooldown Repellent":

      if amount > 1:

        return await ctx.send(embed = Tools.error("You cannot buy more than 1 canister of cooldown repellent."))

      for tag in item["tags"]:

        if tag.startswith("duration-"):

          duration = int(tag.split("duration-")[1])

      if "Cooldown Repellent" in user["data"]["inventory"]:

        return await ctx.send(embed = Tools.error("You already have some Cooldown Repllent."))

      user["data"]["inventory"]["Cooldown Repellent"] = {"count": 1}

      await ctx.send(embed = Tools.bought("Cooldown Repellent", 1))

      Cooldowns.clear_cooldown(ctx.author)

      self.save(db)

      await sleep(duration)

      user["data"]["inventory"].pop("Cooldown Repellent")

      self.save(db)

    else:

      c = 0

      while c < amount:

        if not item["name"] in user["data"]["inventory"]:

          user["data"]["inventory"][item["name"]] = {"count": 0}

        elif user["data"]["inventory"][item["name"]]["count"] > 999:

          return await ctx.send(embed = Tools.error("You have reached the maximum stack limit for that item."))

        user["data"]["inventory"][item["name"]]["count"] += 1

        c += 1

      await ctx.send(embed = Tools.bought(item["name"], amount))

    user["balance"] -= item["price"] * amount

    self.save(db)
    
  @commands.command()
  async def buy(self, ctx, id: int = None, amount: int = 1):

      if not id:
          
        return await ctx.send(embed = Tools.error("You need to specify an item ID."))
      
      elif amount < 0:

        return await ctx.send(embed = Tools.error("Invalid amount specified."))

      return await self.purchase(ctx, id, amount)

# Link to bot
def setup(bot):
  bot.add_cog(Buy(bot))
