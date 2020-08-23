# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Kicks a member on the server"
        self.usage = "kick [user] [reason]"

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member = None, *, reason: str = None):
    
        if not user:
            
            return await ctx.send(embed = Tools.error("Please specify a user to kick."))

        elif user.id == ctx.author.id:
            
            return await ctx.send(embed = Tools.error("Stop trying to kick yourself lmao"))
        
        elif user.id == self.bot.user.id:
            
           return await ctx.send(embed = Tools.error("You cannot kick me. >:)"))

        if reason:
            
            if len(reason) > 512:
        
                return await ctx.send(embed = Tools.error("You can't have a reason over 512 characters."))
            
            await user.kick(reason = reason)
            
        else:
            
            await user.kick()
                
        embed = discord.Embed(title = f"{ctx.author.name} just kicked {user.name} from the server.", description = reason, color = 0x126bf1)
     
        embed.set_author(name = " | Kick", icon_url = self.bot.user.avatar_url)
     
        embed.set_footer(text = f" | Kicked by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Kick(bot))
