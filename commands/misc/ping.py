# Modules
import discord
from datetime import datetime

from discord.ext import commands

# Main Command Class
class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Checks the bot and API ping"
        self.usage = "ping"

    @commands.command()
    async def ping(self, ctx):
            
        api = round(self.bot.latency * 1000)
        
        first = datetime.now()

        msg = await ctx.send("This is a message used to calculate ping time.")

        bot = str(datetime.now() - first).split(".")[1][:2]

        try:

            await msg.delete()

        except:

            pass
        
        embed = discord.Embed(title = "Pong!", description = f"API Ping: {api}ms.\nBot Ping: {bot}ms.", color = 0x126bf1)
        
        embed.set_author(name = " | Ping", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Ping(bot))
