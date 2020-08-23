# Modules
import time
import discord

import datetime
from discord.ext import commands

# Main Command Class
class Uptime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Tells you how long Prism has been online"
        self.usage = "uptime"
        
        self.start = time.time()
        
    @commands.command()
    async def uptime(self, ctx):
            
        embed = discord.Embed(description = str(datetime.timedelta(seconds = int(round(time.time() - self.start)))), color = 0x126bf1)

        embed.set_author(name = " | Uptime", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f"Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Uptime(bot))
