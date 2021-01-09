# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Removebalance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Removes money from a user's balance"
        self.usage = "rembal [user] [amount]"

    @commands.command(aliases = ["removebalance", "rb"])
    @commands.is_owner()
    async def rembal(self, ctx, user: discord.User = None, amount: int = 1000):

        if not user:
            
            user = ctx.author

        db = loads(open("db/users", "r").read())
        
        if not str(user.id) in db:
            
            return await ctx.send(embed = Tools.error(f"{user} is not in the database."))
        
        db[str(user.id)]["balance"] -= amount
        
        open("db/users", "w").write(dumps(db, indent = 4))

        embed = discord.Embed(title = f"{user} has had ${amount} removed from their balance.", color = 0x126bf1)
        
        embed.set_author(name = " | Balance Update", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Balance remove from by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Removebalance(bot))
