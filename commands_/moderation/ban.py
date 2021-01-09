# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Bans a member on the server"
        self.usage = "ban [user] [reason]"

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member = None, *, reason: str = None):
    
        if not user:
            
            return await ctx.send(embed = Tools.error("Please specify a user to ban."))

        elif user.id == ctx.author.id:
            
            return await ctx.send(embed = Tools.error("Stop trying to ban yourself lmao"))
        
        elif user.id == self.bot.user.id:
            
            return await ctx.send(embed = Tools.error("You cannot ban me. >:)"))

        if reason:
            
            if len(reason) > 512:
        
                return await ctx.send(embed = Tools.error("You can't have a reason over 512 characters."))
            
            await user.ban(reason = reason)
            
        else:
            
            await user.ban()
                
        embed = discord.Embed(title = f"{ctx.author.name} just banned {user.name} from the server.", description = reason, color = 0x126bf1)
     
        embed.set_author(name = " | Ban", icon_url = self.bot.user.avatar_url)
     
        embed.set_footer(text = f" | Banned by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Ban(bot))
