# Modules
import json
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Deleted(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Lists the last 5 deleted messages"
    self.usage = "deleted"

  @commands.command(aliases = ["messages", "delmes", "deletedmessages"])
  @commands.has_permissions(manage_messages = True)
  async def deleted(self, ctx):

    db = json.loads(open("db/guilds", "r").read())

    messages = ""

    for message in db[str(ctx.guild.id)]["data"]["deleted_messages"]:

      messages = f"{messages}{message}\n"

    if not messages:

      return await ctx.send(embed = Tools.error("This server doesn't have any deleted messages."))

    embed = discord.Embed(description = messages, color = 0x126bf1)

    embed.set_author(name = " | Deleted Messages", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Deleted(bot))
