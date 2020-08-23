# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Profile(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Displays someones Prism profile"
    self.usage = "profile [user]"
    
  @commands.command(aliases = ["account"])
  async def profile(self, ctx, user = None):
          
    db = loads(open("db/users", "r").read())
        
    user = await Tools.getClosestUser(ctx, user if user else ctx.author)

    if not str(user.id) in db:
        
        return await ctx.send(embed = Tools.error(f"{user.name} does not have a Prism account."))
        
    data = db[str(user.id)]

    pet_string = ""

    if data["pet"]["name"]:

      pet_level = data["pet"]["level"]
      
      if len(str(pet_level)) > 100:
          
        pet_level = "∞"

      pet_string = f"""Pet: [{Tools.uppercase(data["pet"]["type"])}] {data["pet"]["name"]} - Level {pet_level}"""

      if data["pet"]["holding"]:

        pet_string = f"{pet_string} (Holding a {data['pet']['holding']})"

      pet_string = f"{pet_string}\n"

    favorite_command = sorted(data["data"]["commands"]["used"].items(), key = lambda x: x[1], reverse = True)[0]

    favorite_command = f"{Tools.uppercase(favorite_command[0])} ({favorite_command[1]} times)"

    balance = str(data["balance"])

    if len(balance) > 100:
        
        balance = "∞"

    profile = f"""
      Balance: <:coin:733723405118865479> {balance} coins
      Level: {data["data"]["levels"]["level"]} ({data["data"]["levels"]["xp"]} / {data["data"]["levels"]["level"] * 1000})
      Reputation: {data["data"]["levels"]["rep"]}
      {pet_string}Inventory Size: {len(data["data"]["inventory"])} items
      Commands Used: {data["data"]["commands"]["sent"]}
      Favorite Command: {favorite_command}
    """

    premium = ":medal: | " if "premium" in data["data"]["tags"] else ""

    embed = discord.Embed(title = premium + user.name + "#" + user.discriminator, description = data["data"]["bio"], color = 0x126bf1)

    embed.add_field(name = "Details:", value = profile, inline = False)

    embed.set_author(name = f" | Profile", icon_url = user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Profile(bot))
