# Modules
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Stop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Stops playing music in your voice channel."
        self.usage = "stop"

    @commands.command()
    async def stop(self, ctx):

        if not ctx.author.voice:

            return await ctx.send(embed = Tools.error("You aren't in a voice channel."))

        voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)

        if not voice:

            return await ctx.send(embed = Tools.error("Prism isn't in a voice channel."))

        elif not voice.is_playing():

            return await ctx.send(embed = Tools.error("No music is currently playing."))

        try:

            voice.stop()

        except:

            return await ctx.send(embed = Tools.error("Something went wrong while stopping."))

        return await ctx.send(embed = discord.Embed(description = f":x: **Playback stopped.**", color = 0x126bf1))

# Link to bot
def setup(bot):
    bot.add_cog(Stop(bot))
