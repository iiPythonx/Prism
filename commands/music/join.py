# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Join(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Connects to your voice channel."
        self.usage = "join"

    @commands.command(aliases = ["connect"])
    async def join(self, ctx):

        if not ctx.author.voice:

            return await ctx.send(embed = Tools.error("You aren't in a voice channel."))

        voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)

        if voice:

            await voice.move_to(ctx.author.voice.channel)

            return await ctx.send(embed = discord.Embed(description = f":wave: **Moved to #{ctx.author.voice.channel.name}.**", color = 0x126bf1))

        else:

            await ctx.author.voice.channel.connect()

        return await ctx.send(embed = discord.Embed(description = f":wave: **Connected to #{ctx.author.voice.channel.name}.**", color = 0x126bf1))

# Link to bot
def setup(bot):
    bot.add_cog(Join(bot))
