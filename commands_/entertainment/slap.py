# Modules
from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Slap(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Slap the hell out of somebody"
        self.usage = "slap [user]"

    @commands.command()
    async def slap(self, ctx, *, user = None):

        if not user:
            
            return await ctx.send(f"**Prism** just slapped the hell out of **{ctx.author.name}** for not specifying someone to slap.")

        return await ctx.send(f"**{ctx.author.name}** just slapped the hell out of **{user}**.")

# Link to bot
def setup(bot):
    bot.add_cog(Slap(bot))
