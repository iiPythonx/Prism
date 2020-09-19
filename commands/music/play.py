# Modules
import discord
import youtube_dl

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Streams YouTube music to discord"
        self.usage = "play [url]"

    @commands.command()
    async def play(self, ctx, url: str = None):

        if not url:

            return await ctx.send(embed = Tools.error("No URL specified to play."))

        elif not ctx.author.voice:

            return await ctx.send(embed = Tools.error("You aren't in a voice channel."))

        voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)

        if not voice:

            try:

                voice = await ctx.author.voice.channel.connect()

            except:

                return await ctx.send(embed = Tools.error("Missing permission(s) to join your voice channel."))

        with youtube_dl.YoutubeDL({}) as ytdl:

            info = ytdl.extract_info(url, download = False)

        await ctx.send(info["title"])

        voice.play(discord.FFmpegPCMAudio(info["formats"][0]["url"]))

        voice.source = discord.PCMVolumeTransformer(voice.source)

        voice.source.volume = 1

# Link to bot
def setup(bot):
    bot.add_cog(Play(bot))
