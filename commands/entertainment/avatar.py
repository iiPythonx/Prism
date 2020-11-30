# Modules
import discord
from random import choice

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Avatar(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "View a Discord user's profile picture"
    self.usage = "avatar [user]"

    self.options = [
      "Looking good, {}.",
      "Nice, {}.",
      "{} is looking good today."
    ]

  @commands.command(aliases = ["pfp", "picture"])
  async def avatar(self, ctx, *, user: discord.User = None):

    user = await Tools.getClosestUser(ctx, user if user else ctx.author)

    embed = discord.Embed(title = choice(self.options).format(user.name), color = 0x126bf1)
    embed.set_image(url = user.avatar_url)
    embed.set_author(name = " | Avatar", icon_url = self.bot.user.avatar_url)
    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Avatar(bot))
