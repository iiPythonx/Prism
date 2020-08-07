# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from discord.ext import commands
from assets.prism import Constants, Tools

# Main Command Class
class Whitelist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Whitelists a blacklisted user on the Prism interface"
        self.usage = "whitelist [user]"

    @commands.command(aliases = ["wl"])
    @commands.is_owner()
    async def whitelist(self, ctx, user: discord.User = None):

        if not user:
            
            return await ctx.send(embed = Tools.error("Please specify somebody to whitelist."))
        
        db = loads(open("db/users", "r").read())
            
        if not str(user.id) in db or not Tools.has_flag(db, user, "blacklisted"):
            
            return await ctx.send(embed = Tools.error(f"{user} isn't blacklisted."))
            
        db[str(user.id)]["data"]["tags"].remove("blacklisted")
        
        open("db/users", "w").write(dumps(db, indent = 4))

        embed = discord.Embed(title = f"{user} has been whitelisted.", color = 0x126bf1)
        
        embed.set_author(name = " | Whitelist", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Whitelisted by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Whitelist(bot))
