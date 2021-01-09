# Modules
import json
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Deleted(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Lists the last 10 deleted messages"
    self.usage = "deleted"

  @commands.command(aliases = ["messages", "delmes", "deletedmessages"])
  @commands.has_permissions(manage_messages = True)
  async def deleted(self, ctx):

    db = json.loads(open("db/guilds", "r").read())
    msgs = db[str(ctx.guild.id)]["data"]["deleted_messages"]

    if not msgs:
      return await ctx.send(embed = Tools.error("This server doesn't have any deleted messages."))

    embed = discord.Embed(title = "Last 10 deleted messages", description = "This does not list embeds or messages longer than 100 characters.", color = 0x126bf1)
    embed.set_author(name = " | Deleted Messages", icon_url = self.bot.user.avatar_url)
    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    for msg in msgs:
      embed.add_field(name = f"{msg['author']} ({msg['date']}):", value = msg['content'], inline = False)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Deleted(bot))
