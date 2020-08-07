# Prism Rewrite - Basic Command

# Modules
import discord
from random import randint

from json import loads, dumps

from discord.ext import commands
from assets.prism import Cooldowns, Tools

# Main Command Class
class Sock(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Socks somebody in the face"
    self.usage = "sock [user]"

  @commands.command()
  async def sock(self, ctx, user: str = None):

    if Cooldowns.on_cooldown(ctx, "sock"):

      return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "sock"))

    elif not user:
        
      return await ctx.send(embed = Tools.error("I need to know who your trying to sock."))

    user = Tools.getClosestUser(ctx, user)

    if not user:

      return await ctx.send(embed = Tools.error(f"I couldn't find that user; try again with more letters."))

    db = loads(open("db/users", "r").read())

    if user.id == ctx.author.id:

      return await ctx.send(embed = Tools.error("Stop trying to sock yourself."))

    elif not str(user.id) in db:

      earnings = randint(0, 100)

      db[str(ctx.author.id)]["balance"] += earnings

      open("db/users", "w").write(dumps(db, indent = 4))

      embed = discord.Embed(title = f"You just socked **{user.name}** so hard that they dropped **{earnings} coins**.", color = 0x126bf1)

      embed.set_author(name = " | Sock", icon_url = self.bot.user.avatar_url)

      embed.set_footer(text = f" | Socked by the great {ctx.author}.", icon_url = ctx.author.avatar_url)

      await ctx.send(embed = embed)

      return await Cooldowns.set_cooldown(ctx, "sock", 300)

    earnings = randint(0, 100)

    db[str(ctx.author.id)]["balance"] += earnings

    db[str(user.id)]["balance"] -= earnings

    open("db/users", "w").write(dumps(db, indent = 4))

    embed = discord.Embed(title = f"You just socked **{user.name}** so hard that they dropped **{earnings} coins**.", color = 0x126bf1)

    embed.set_author(name = " | Sock", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Socked by the great {ctx.author}.", icon_url = ctx.author.avatar_url)

    await ctx.send(embed = embed)

    return await Cooldowns.set_cooldown(ctx, "sock", 300)

# Link to bot
def setup(bot):
  bot.add_cog(Sock(bot))
