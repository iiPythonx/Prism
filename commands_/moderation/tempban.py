# Modules
import discord
from asyncio import sleep

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Temporaryban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Bans a member on the server for a specified amount of seconds"
        self.usage = "tempban [user] [seconds]"
        
    @commands.command(aliases = ["tempbanish", "tban"])
    @commands.has_permissions(ban_members = True)
    async def tempban(self, ctx, user: discord.Member = None, seconds: int = 60, *, reason: str = None):
    
        if not user:
            
            return await ctx.send(embed = Tools.error("No user specified to ban."))

        elif user.id == ctx.author.id:
            
            return await ctx.send(embed = Tools.error("You can't ban youself."))
        
        elif user.id == self.bot.user.id:
            
            await ctx.send("If that's what you really want, then aight.")
            
            return await ctx.guild.leave()

        if reason and len(reason) > 512:

            return await ctx.send(embed = Tools.error("That reason is too long (max is 512 characters)."))

        await user.ban(reason = reason)
                
        embed = discord.Embed(title = f"{ctx.author} just tempbanned {user} for {seconds} seconds.", description = reason, color = 0x126bf1)
     
        embed.set_author(name = " | Ban", icon_url = self.bot.user.avatar_url)
     
        embed.set_footer(text = f" | Banned by {ctx.author}.", icon_url = ctx.author.avatar_url)

        await ctx.send(embed = embed)

        await sleep(seconds)
            
        return await user.unban(reason = "Ban has ended.")

# Link to bot
def setup(bot):
    bot.add_cog(Temporaryban(bot))
