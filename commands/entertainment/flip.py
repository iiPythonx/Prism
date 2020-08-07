# Prism Rewrite - Basic Command

# Modules
import discord
from random import choice

from discord.ext import commands

# Main Command Class
class Flip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Flips a fair coin"
        self.usage = "flip"

    @commands.command(aliases = ["coinflip"])
    async def flip(self, ctx):

        embed = discord.Embed(title = f"The coin landed on {choice(['tails', 'heads'])}.", color = 0x126bf1)
        
        embed.set_author(name = " | Coinflip", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Flip(bot))
