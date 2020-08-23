# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Unmute(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Unmutes a member on the server"
        self.usage = "unmute [user]"
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unmute(self, ctx, user: discord.Member = None):
    
        if not user:

            return await ctx.send(embed = Tools.error("No user specified to unmute."))

        muted = discord.utils.get(ctx.guild.roles, name = "Muted")
        
        if not muted:
            
            return await ctx.send(embed = Tools.error("No role called mute exists on this server."))

        is_muted = False

        for role in user.roles:
            
            if role.name == "Muted":
                
                is_muted = True
            
        if not is_muted:
            
            return await ctx.send(embed = Tools.error(f"{user} isn't muted."))

        await user.remove_roles(muted)

        embed = discord.Embed(title = f"{user} has been unmuted.", color = 0x126bf1)
        
        embed.set_author(name = " | Unmute", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Unmuted by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Unmute(bot))
    