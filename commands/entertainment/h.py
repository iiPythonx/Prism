# Prism Rewrite - Basic Command

# Modules
from discord.ext import commands

# Main Command Class
class H(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "H"
        self.usage = "h"

    @commands.command()
    async def h(self, ctx):

        h = """   `` _    _ 
 | |  | |
 | |__| |
 |  __  |
 | |  | |
 |_|  |_|``
        """

        return await ctx.send(h)

# Link to bot
def setup(bot):
    bot.add_cog(H(bot))
