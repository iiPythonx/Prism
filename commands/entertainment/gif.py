# Modules
import discord
from os import getenv

from requests import get
from random import choice

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Gif(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Searches giphy for a specified query"
        self.usage = "gif [query]"

        self.api_key = getenv("GIPHY_KEY")
        self.api_url = "https://api.giphy.com/v1/gifs/search"

    @commands.command(aliases = ["gifsearch"])
    async def gif(self, ctx, *, query: str = None):

        if not query:
            return await ctx.send(embed = Tools.error("No query specified."))

        elif not ctx.channel.nsfw:
            return await ctx.send(embed = Tools.error("Due to no limitations, this channel has to be NSFW."))

        data = get(self.api_url, {"api_key": self.api_key, "q": query, "lang": "en"}).json()["data"]

        if not data:
            return await ctx.send(embed = Tools.error("No results found."))

        embed = discord.Embed(color = 0x126bf1)
        embed.set_image(url = choice(data)["images"]["downsized_large"]["url"])
        embed.set_author(name = " | GIF", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Gif(bot))
