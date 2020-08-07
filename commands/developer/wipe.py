# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Wipe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Removes a user's account from the database"
        self.usage = "wipe [user]"

    @commands.command()
    @commands.is_owner()
    async def wipe(self, ctx, user: discord.User = None):

        if not user:
            
            user = ctx.author

        db = loads(open("db/users", "r").read())
        
        if not str(user.id) in db:
            
            return await ctx.send(embed = Tools.error(f"{user} isn't in the database."))
        
        db.pop(str(user.id))
        
        open("db/users", "w").write(dumps(db, indent = 4))

        embed = discord.Embed(title = f"{user} has had their account wiped.", color = 0x126bf1)
        
        embed.set_author(name = " | Account Removal", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Account removed by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Wipe(bot))
