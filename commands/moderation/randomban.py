# Modules
import random
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Randomban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "bans a random user from the server"
        self.usage = "ranban [reason]"
        
    @commands.command(aliases = ["randomban", "banran", "banrandom"])
    @commands.has_permissions(ban_members = True)
    async def ranban(self, ctx, reason: str = None):

        if reason and len(reason) > 512:
    
            return await ctx.send(embed = Tools.error("That reason is too long (max is 512 characters)."))

        c = 0
        
        while True:

            user = random.choice(ctx.guild.members)

            try:
                
                if user == ctx.author:
                    
                    pass
                
                else:
                
                    await user.ban(reason = reason)
                    
                    break
                
            except:
                
                if c >= 15:
                    
                    return await ctx.send(embed = Tools.error("Nobody here is able to be banned."))
                
            c += 1

        embed = discord.Embed(title = f"{user} has been banned from the server.", color = 0x126bf1)
        
        embed.set_author(name = " | Random ban", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | banned by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Randomban(bot))
