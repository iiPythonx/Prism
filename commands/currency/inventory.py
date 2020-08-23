# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Inventory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Checks a user's inventory"
        self.usage = "inventory"

    @commands.command(aliases = ["inv"])
    async def inventory(self, ctx, user = None):
        
        user = await Tools.getClosestUser(ctx, user if user else ctx.author)

        db = loads(open("db/users", "r").read())
        
        if not str(user.id) in db:
            
            return await ctx.send(embed = Tools.error(f"{user.name} doesn't have an account."))
        
        inventory = ""
        
        for item in db[str(user.id)]["data"]["inventory"]:
            
            inventory = f"{inventory}{item} (x{db[str(user.id)]['data']['inventory'][item]['count']}), "
        
        if not inventory:
            
            inventory = "Nothing to display.  "
            
        message = f"{user.name}'s Inventory"
        
        if ctx.author.id == user.id:
            
            message = "Your Inventory"
        
        embed = discord.Embed(title = message, description = inventory[:-2], color = 0x126bf1)
        
        embed.set_author(name = " | Inventory", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        try:

          return await ctx.send(embed = embed)

        except:

          return await ctx.send(embed = Tools.error(f"{user.name} has way too many items."))

# Link to bot
def setup(bot):
    bot.add_cog(Inventory(bot))
