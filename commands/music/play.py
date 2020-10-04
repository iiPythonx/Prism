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

            voice = await ctx.author.voice.channel.connect()

        elif voice.is_playing():

            voice.stop()

        with youtube_dl.YoutubeDL({}) as ytdl:

            info = ytdl.extract_info(url, download = False)

        voice.play(discord.FFmpegPCMAudio(info["formats"][0]["url"]))

        voice.source = discord.PCMVolumeTransformer(voice.source)

        voice.source.volume = 1

        embed = discord.Embed(description = f":musical_note: **Now playing: {info['title']}**", color = 0x126bf1)

        embed.set_footer(text = " | Please note: music is experimental, freezing may occur.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Play(bot))
