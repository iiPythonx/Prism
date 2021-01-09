# Prism Rewrite - Basic Command

# Modules
import discord

from discord.ext import commands
from assets.prism import Cooldowns

# Main Command Class
class ClearCooldowns(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Resets all of a user's cooldowns"
        self.usage = "clearcooldowns [user]"

    @commands.command()
    @commands.is_owner()
    async def clearcooldowns(self, ctx, user: discord.User = None):
        
        if not user:

          user = ctx.author

        Cooldowns.clear_cooldown(user)

        embed = discord.Embed(title = f"{user}'s cooldowns have been cleared.", color = 0x126bf1)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(ClearCooldowns(bot))
