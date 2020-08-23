# Modules
import random
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Randomkick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Kicks a random user from the server"
        self.usage = "rankick [reason]"
        
    @commands.command(aliases = ["randomkick", "kickran", "kickrandom"])
    @commands.has_permissions(kick_members = True)
    async def rankick(self, ctx, reason: str = None):

        if reason and len(reason) > 512:
    
            return await ctx.send(embed = Tools.error("That reason is too long (max is 512 characters)."))

        c = 0
        
        while True:

            user = random.choice(ctx.guild.members)

            try:
                
                if user == ctx.author:
                    
                    pass
                
                else:
                
                    await user.kick(reason = reason)
                    
                    break
                
            except:
                
                if c >= 15:
                    
                    return await ctx.send(embed = Tools.error("Nobody here is able to be kicked."))
                
            c += 1

        embed = discord.Embed(title = f"{user} has been kicked from the server.", color = 0x126bf1)
        
        embed.set_author(name = " | Random kick", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Kicked by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Randomkick(bot))
