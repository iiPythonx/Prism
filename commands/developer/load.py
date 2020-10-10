# Modules
import discord
from os import path, listdir

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Load(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Loads a Prism module"
        self.usage = "load [module]"

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, module = None):

        if not module:
            
          return await ctx.send(embed = Tools.error("Please specify a module to load."))

        path = None

        for folder in listdir("commands"):

            for file in listdir(f"commands/{folder}"):

                if file == f"{module}.py":

                    path = f"commands.{folder}.{module}"
        
        if not path:

          return await ctx.send(embed = Tools.error("The specified module does not exist."))

        try:

            self.bot.load_extension(path)
            
        except Exception as e:
            
            embed = discord.Embed(title = f"Module `{path}` failed to load.", description = f"```\n{e}\n```", color = 0xFF0000)

            return await ctx.send(embed = embed)

        embed = discord.Embed(title = f"The `{path}` module has been loaded.", color = 0x126bf1)
        
        embed.set_author(name = " | Module Load", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Loaded by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Load(bot))
