# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

from assets.prism import Constants

# Main Command Class
class Blacklist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Blacklists a user from the Prism interface"
        self.usage = "blacklist [user]"

    @commands.command(aliases = ["bl"])
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.User = None):

        if not user:
            
            return await ctx.send(embed = Tools.error("Please specify somebody to blacklist."))
        
        db = loads(open("db/users", "r").read())
        
        if not str(user.id) in db:
            
            db[str(user.id)] = Constants.user_preset
            
        elif Tools.has_flag(db, user, "blacklisted"):
            
            return await ctx.send(embed = Tools.error(f"{user} is already blacklisted."))
            
        db[str(user.id)]["data"]["tags"].append("blacklisted")
        
        open("db/users", "w").write(dumps(db, indent = 4))

        embed = discord.Embed(title = f"{user} has been blacklisted from Prism.", color = 0x126bf1)
        
        embed.set_author(name = " | Blacklist", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Blacklisted by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Blacklist(bot))
