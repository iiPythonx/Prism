# Modules
import json
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Biography(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Changes your public biography"
        self.usage = "biography [text]"

    @commands.command(aliases = ["bio"])
    async def biography(self, ctx, *, bio: str = None):
 
        if not bio:
            
            return await ctx.send(embed = Tools.error("Please specify a biography."))
 
        elif len(bio) > 40:
            
            return await ctx.send(embed = Tools.error("You're biography is way too long (40 characters max)."))
 
        db = json.loads(open("db/users", "r").read())
        
        db[str(ctx.author.id)]["data"]["bio"] = bio
        
        open("db/users", "w").write(json.dumps(db, indent = 4))
 
        embed = discord.Embed(title = "Your biography has been set.", description = bio, color = 0x126bf1)
        
        embed.set_author(name = " | Biography", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Biography(bot))
