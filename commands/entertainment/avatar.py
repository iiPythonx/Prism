# Prism Rewrite - Basic Command

# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Avatar(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Check somebodies avatar"
    self.usage = "avatar [user]"

  @commands.command(aliases = ["pfp", "picture"])
  async def avatar(self, ctx, *, user: str = None):

    if not user:
        
      user = ctx.author

    user = Tools.getClosestUser(ctx, user)

    if not user:

      return await ctx.send(embed = Tools.error("I wasn't able to find that user."))

    embed = discord.Embed(title = f"Looking good, {user.name}.", color = 0x126bf1)
    
    embed.set_image(url = user.avatar_url)
    
    embed.set_author(name = " | Avatar", icon_url = self.bot.user.avatar_url)
    
    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Avatar(bot))
