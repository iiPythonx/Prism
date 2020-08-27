# Modules
from assets.prism import Tools
from discord.ext import commands
from assets.effects import Effects as Eff

# Main Command Class
class Effects(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Checks out your effects"
    self.usage = "effects"

  @commands.command()
  async def effects(self, ctx):
    
    effects = Eff(ctx.author.id)

    if not len(effects):

      return await ctx.send(embed = Tools.error("You don't have any effects."))

    return await ctx.send(str(effects))

# Link to bot
def setup(bot):
  bot.add_cog(Effects(bot))
