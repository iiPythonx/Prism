# Prism Rewrite - Basic Command

# Modules
import discord
from random import choice

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Roast(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Lets Commuter roast somebody"
        self.usage = "roast [user]"

        self.roasts = [
            "ass",
            "shUT UP"
        ]

    @commands.command()
    @commands.is_owner()
    async def roast(self, ctx, user = None):

        if not ctx.author.id == 666839157502378014:

            return await ctx.send("idiot you arent commuter")

        elif not user:
            
            return await ctx.send("who do you want to roast????")
        
        user = Tools.getClosestUser(ctx, user)

        if not user:

            return await ctx.send("that isnt a person")

        await ctx.send("Commuter is thinking of a roast..")

        embed = discord.Embed(title = f"{user.name}, {choice(self.roasts)}", color = 0x126bf1)
        
        embed.set_footer(text = f" | Roasted and toasted by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Roast(bot))
