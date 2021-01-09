# Modules
from discord.ext import commands

# Command class
class Test(commands.Cog):

    """Simple command to test Prism v3"""

    def __init__(self, bot):
        self.bot = bot
        self.core = bot.core

    @commands.command()
    async def test(self, ctx):
        return await ctx.send(f"Prism v1.0.4 alpha - {self.bot.latency} {self.core.database}")

# Setup
def setup(bot):
    bot.add_cog(Test(bot))
