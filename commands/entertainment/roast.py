# Modules
import discord
from random import choice

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Roast(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Roasts somebody with an array of epic roasts"
        self.usage = "roast [user]"

        self.roasts = [
            "ass",
            "{}, shUT UP."
        ]

    @commands.command()
    async def roast(self, ctx, user = None):

        if not user:
            
            return await ctx.send(embed = Tools.error("You expect to roast the air?"))
        
        user = await Tools.getClosestUser(ctx, user)

        embed = discord.Embed(title = choice(self.roasts).format(user.name), color = 0x126bf1)
        
        embed.set_footer(text = f" | Roasted and toasted by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Roast(bot))
