# Prism Rewrite - Basic Command

# Modules
import discord
from os import listdir

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Unload(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Unloads a Prism module"
    self.usage = "unload [module]"

  @commands.command()
  @commands.is_owner()
  async def unload(self, ctx, module = None):

    if not module:
        
      return await ctx.send(embed = Tools.error("Please specify a module to unload."))

    module = module.split('.')[-1]

    exists = False

    for folder in listdir("commands"):

      for command in listdir(f"commands/{folder}"):

        if f"{module}.py" == command:

          module_path = f"commands.{folder}.{module}"

          exists = True

    if not exists:

      return await ctx.send(embed = Tools.error("The specified module does not exist."))

    try:

        self.bot.unload_extension(module_path)
        
    except Exception as e:
        
        await ctx.author.send(f"```Module {module} failed to unload:\n\n{e}```")
        
        return await ctx.send(embed = Tools.error(f"Module {module} failed to unload."))

    embed = discord.Embed(title = f"The {module} module has been unloaded.", color = 0x126bf1)
    
    embed.set_author(name = " | Module Unload", icon_url = self.bot.user.avatar_url)
    
    embed.set_footer(text = f" | Loaded by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Unload(bot))
