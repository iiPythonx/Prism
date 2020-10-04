# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Leave(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Makes Prism leave your voice channel."
        self.usage = "leave"

    @commands.command(aliases = ["disconnect", "dsc", "fuckoff"])
    async def leave(self, ctx):

        if not ctx.author.voice:

            return await ctx.send(embed = Tools.error("You aren't in a voice channel."))

        voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)

        if not voice:

            return await ctx.send(embed = Tools.error("Prism isn't in a voice channel."))

        elif voice.is_playing():

            try:

                voice.stop()

            except:

                pass

        await voice.disconnect()

        return await ctx.send(embed = discord.Embed(description = f":wave: **Left the voice channel.**", color = 0x126bf1))

# Link to bot
def setup(bot):
    bot.add_cog(Leave(bot))
