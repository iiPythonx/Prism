# Modules
import json
import random

import discord
from asyncio import sleep

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Fight(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Fights another user via your pet"
    self.usage = "fight [user]"

  @commands.command(aliases = ["challenge"])
  async def fight(self, ctx, user: discord.User = None):

    if not user:

      return await ctx.send(embed = Tools.error("You need to specify someone to fight."))

    elif user.id == self.bot.user.id:

      return await ctx.send(embed = Tools.error("You cannot fight me; I am over 9000."))

    elif user.id == ctx.author.id:

      return await ctx.send(embed = Tools.error("You cannot fight yourself."))

    db = json.loads(open("db/users", "r").read())

    if not str(user.id) in db or not db[str(user.id)]["pet"]["name"]:

      return await ctx.send(embed = Tools.error(f"{user.name} doesn't have a pet for you to fight."))

    elif not db[str(ctx.author.id)]["pet"]["name"]:

      return await ctx.send(embed = Tools.error(f"You don't have a pet to fight with."))

    embed = discord.Embed(description = f":clock1: \t **Now waiting for {user.name} to say accept.**", color = 0x126bf1)

    await ctx.send(embed = embed)

    def usercheck(m):

      return m.author == user and m.channel == ctx.channel

    while True:

      try:

        message = await self.bot.wait_for("message", check = usercheck, timeout = 30)

      except:

        return await ctx.send(embed = Tools.error(f"{user.name} never accepted your request."))

      if message.content.lower() in ["accept", "yes", "yea", "si", "ye", "ya"]:

        break

      elif message.content.lower() in ["deny", "cancel", "no", "stop"]:

        return await ctx.send(embed = Tools.error(f"{user.name} denied your request."))

    def make_embed(text):

      return discord.Embed(title = text, color = 0x126bf1)

    user_db = db[str(user.id)]
    user_health = 120 * user_db["pet"]["level"]
    
    author_db = db[str(ctx.author.id)]
    author_health = 120 * author_db["pet"]["level"]

    if random.randint(1, 4) != 1:

      damage = random.randint(15 * user_db["pet"]["level"], 30 * user_db["pet"]["level"])

      author_health -= damage

      m = await ctx.send(embed = make_embed(f"{user_db['pet']['name']} just attacked {author_db['pet']['name']} and dealt {damage} damage."))

      await sleep(3)

    else:

      m = await ctx.send(embed = make_embed(f"{user_db['pet']['name']} tried to attack but missed!"))

      await sleep(3)

    while True:

      try:

        if user_health <= 0:

          rep = random.randint(9, 20)

          author_db["data"]["levels"]["rep"] += rep

          open("db/users", "w").write(json.dumps(db, indent = 4))

          embed = discord.Embed(title = f"Congrats, {ctx.author.name}; you won the battle and gained {rep} reputation.", color = 0x126bf1)

          return await m.edit(embed = embed)

        elif author_health <= 0:

          rep = random.randint(9, 20)

          user_db["data"]["levels"]["rep"] += rep

          open("db/users", "w").write(json.dumps(db, indent = 4))

          embed = discord.Embed(title = f"Congrats, {user.name}; you won the battle and gained {rep} reputation.", color = 0x126bf1)

          return await m.edit(embed = embed)

        elif len(str(author_db["pet"]["level"])) > 50:
            
          rep = random.randint(20, 40)

          author_db["data"]["levels"]["rep"] += rep

          open("db/users", "w").write(json.dumps(db, indent = 4))
              
          embed = discord.Embed(title = f"Congrats, {ctx.author.name}; you just one shot {user_db['pet']['name']} and gained {rep} reputation.", color = 0x126bf1)
              
          return await m.edit(embed = embed)

        elif len(str(user_db["pet"]["level"])) > 50:
            
          rep = random.randint(20, 40)

          user_db["data"]["levels"]["rep"] += rep

          open("db/users", "w").write(json.dumps(db, indent = 4))

          embed = discord.Embed(title = f"Congrats, {ctx.author.name}; you just one shot {user_db['pet']['name']} and gained {rep} reputation.", color = 0x126bf1)
            
          return await m.edit(embed = embed)
          
        elif random.randint(1, 4) != 1:

          damage = random.randint(15 * user_db["pet"]["level"], 30 * user_db["pet"]["level"])

          author_health -= damage

          await m.edit(embed = make_embed(f"{user_db['pet']['name']} just attacked {author_db['pet']['name']} and dealt {damage} damage."))

          await sleep(3)

        else:

          await m.edit(embed = make_embed(f"{user_db['pet']['name']} tried to attack but missed!"))

          await sleep(3)

        if random.randint(1, 4) != 1:

          damage = random.randint(15 * author_db["pet"]["level"], 30 * author_db["pet"]["level"])

          user_health -= damage

          await m.edit(embed = make_embed(f"{author_db['pet']['name']} just attacked {user_db['pet']['name']} and dealt {damage} damage."))

          await sleep(3)

        else:

          await m.edit(embed = make_embed(f"{author_db['pet']['name']} tried to attack but missed!"))

          await sleep(3) 

      except Exception as e:

        await ctx.send(e)

        return await ctx.send(embed = Tools.error("It seems someone deleted my message."))

# Link to bot
def setup(bot):
  bot.add_cog(Fight(bot))
