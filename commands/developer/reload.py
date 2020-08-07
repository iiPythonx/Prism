# Prism Rewrite - Basic Command

# Modules
import discord
from os import path

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Reload(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Reloads a Prism module"
        self.usage = "reload [module]"

    @commands.command(aliases = ["rl"])
    @commands.is_owner()
    async def reload(self, ctx, module = None):

        if not module:
            
          return await ctx.send(embed = Tools.error("Please specify a module to reload."))

        elif not "." in module or not path.exists(module.replace(".", "/") + ".py"):

          return await ctx.send(embed = Tools.error("The specified module does not exist."))

        try:

            self.bot.unload_extension(module)

            self.bot.load_extension(module)
            
        except Exception as e:
            
            await ctx.author.send(f"```Module {module.split('.')[2]} failed to reload:\n\n{e}```")
            
            return await ctx.send(embed = Tools.error(f"Module {module.split('.')[2]} failed to reload."))

        embed = discord.Embed(title = f"The {module.split('.')[2]} module has been reloaded.", color = 0x126bf1)
        
        embed.set_author(name = " | Module Reload", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Reloaded by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Reload(bot))
