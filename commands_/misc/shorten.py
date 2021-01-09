# Modules
import discord
from json import loads

from requests import post

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Shorten(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Shortens an URL"
        self.usage = "shorten [url]"

        self.url = "https://jaus.tk/api/v1/create"

    @commands.command()
    async def shorten(self, ctx, *, url: str = None):

        if not url:

            return await ctx.send(embed = Tools.error("No URL specified to shorten."))

        resp = post(self.url, data = {"url": url, "trackIP": False})

        shorturl = loads(resp.text)["shorturl"]

        embed = discord.Embed(title = "Click here to visit your website.", description = "Shortened URL: " + shorturl, url = shorturl, color = 0x126bf1)

        embed.add_field(name = "Please note:", value = "This link **will** expire in ~24 hours.", inline = False)

        embed.set_author(name = " | URL Shortened", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Shorten(bot))
