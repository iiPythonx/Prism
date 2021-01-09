# Modules
import discord
from random import randint

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Rolldice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Rolls a dice"
        self.usage = "dice [max sides]"

    @commands.command(aliases = ["roll", "rolldice", "diceroll"])
    async def dice(self, ctx, maximum: int = 6):
        
        if maximum > 100 or maximum < 2:
            
            return await ctx.send(embed = Tools.error("Maximum side count is 100; minimum is 2."))
            
        embed = discord.Embed(title = f"{maximum} sided diceroll.", description = f"The dice landed on {randint(1, maximum)}.", color = 0x126bf1)
        
        embed.set_author(name = " | Dice Roll", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Rolldice(bot))
