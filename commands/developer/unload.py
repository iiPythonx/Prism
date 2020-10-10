# Modules
import discord
from os import path, listdir

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

        path = None

        for folder in listdir("commands"):

            for file in listdir(f"commands/{folder}"):

                if file == f"{module}.py":

                    path = f"commands.{folder}.{module}"
        
        if not path:

          return await ctx.send(embed = Tools.error("The specified module does not exist."))

        try:

            self.bot.unload_extension(path)
            
        except Exception as e:
            
          embed = discord.Embed(title = f"Module `{path}` failed to unload.", description = f"```\n{e}\n```", color = 0xFF0000)

          return await ctx.send(embed = embed)

        embed = discord.Embed(title = f"The `{path}` module has been unloaded.", color = 0x126bf1)
        
        embed.set_author(name = " | Module Unload", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Unloaded by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Unload(bot))
