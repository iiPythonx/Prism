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

        # Locate our bot latency
        bot = round(self.bot.latency * 1000)

        # Identify our API ping
        first = datetime.now()
        msg = await ctx.send("This is a message used to calculate ping time.")
        api = round((datetime.now() - first).total_seconds() * 1000)

        # Edit message
        embed = discord.Embed(title = "Pong!", description = f"API Ping: {api}ms\nBot Ping: {bot}ms\nRoundtrip: {api + bot}ms", color = 0x126bf1)
        embed.set_author(name = " | Ping", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await msg.edit(content = None, embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Ping(bot))
