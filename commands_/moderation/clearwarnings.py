# Modules
import discord
from json import loads, dumps

from discord.ext import commands

# Main Command Class
class ClearWarnings(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Clears a users warnings on the server"
    self.usage = "clearwarnings [user]"
        
  @commands.command(aliases = ["clearwarns"])
  @commands.has_permissions(manage_messages = True)
  async def clearwarnings(self, ctx, user: discord.Member = None):
    
    if not user:
        
        user = ctx.author

    db = loads(open("db/users", "r").read())

    if not str(user.id) in db or not str(ctx.guild.id) in db[str(user.id)]["data"]["warnings"]:

      title = f"{user} doesn't have any warnings on this server."

      if ctx.author.id == user.id:

        title = "You don't have any warnings on this server."

      embed = discord.Embed(title = title, color = 0x126bf1)

      embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

      return await ctx.send(embed = embed)

    db[str(user.id)]["data"]["warnings"].pop(str(ctx.guild.id))

    open("db/users", "w").write(dumps(db, indent = 4))

    title = f"{user}'s warnings have been cleared."

    if ctx.author.id == user.id:

      title = "Your warnings have been cleared."

    embed = discord.Embed(title = title, color = 0x126bf1)

    embed.set_author(name = " | Cleared", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(ClearWarnings(bot))
