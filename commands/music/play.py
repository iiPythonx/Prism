# Modules
import discord
import lavalink

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Play(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Streams YouTube music to discord"
        self.usage = "play [url]"

        self.bot.music = lavalink.Client(685550504276787200)  # temporarily hardcoded
        self.bot.music.add_node("localhost", 7000, "prism", "us", "music-node")
        self.bot.add_listener(self.bot.music.voice_update_handler, "on_socket_response")
        self.bot.music.add_event_hook(self.track_hook)

    async def track_hook(self, event):

        if isinstance(event, lavalink.events.QueueEndEvent):

            guild_id = int(event.player.guild_id)
            
            await self.connect_to(guild_id, None)
        
    async def connect_to(self, guild_id: int, channel_id: str):

        ws = self.bot._connection._get_websocket(guild_id)
        
        await ws.voice_state(str(guild_id), channel_id)

    @commands.command()
    async def play(self, ctx, query: str = None):

        if not query:

            return await ctx.send(embed = Tools.error("No query specified to play."))

        elif not ctx.author.voice:

            return await ctx.send(embed = Tools.error("You aren't in a voice channel."))

        voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)

        if not voice:

            voice = await ctx.author.voice.channel.connect()

        elif voice.is_playing():

            voice.stop()

        #with youtube_dl.YoutubeDL({}) as ytdl:

        #    info = ytdl.extract_info(url, download = False)

        #voice.play(discord.FFmpegPCMAudio(info["formats"][0]["url"]))

        #voice.source = discord.PCMVolumeTransformer(voice.source)

        #voice.source.volume = 1

        #embed = discord.Embed(description = f":musical_note: **Now playing: {info['title']}**", color = 0x126bf1)

        #embed.set_footer(text = " | Please note: music is experimental, freezing may occur.", icon_url = ctx.author.avatar_url)

        #return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Play(bot))
