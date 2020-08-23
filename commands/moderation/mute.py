# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Mute(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Mutes a member on the server"
        self.usage = "mute [user]"
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def mute(self, ctx, user: discord.Member = None):
    
        if not user:

            return await ctx.send(embed = Tools.error("No user specified to mute."))

        muted = discord.utils.get(ctx.guild.roles, name = "Muted")

        if not muted:

            muted = await ctx.guild.create_role(name = "Muted", reason = "Prism; Muted role")

            for channel in ctx.guild.channels:
                
                await channel.set_permissions(muted, send_messages = False)

        await user.add_roles(muted)

        embed = discord.Embed(title = f"{user} has been muted.", color = 0x126bf1)
        
        embed.set_author(name = " | Mute", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Muted by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Mute(bot))
    