# Modules
from discord.ext import commands

# Main Command Class
class Corn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Haha corn go brrr"
        self.usage = "corn"

    @commands.command()
    async def corn(self, ctx):

        return await ctx.send(":corn:")

# Link to bot
def setup(bot):
    bot.add_cog(Corn(bot))
