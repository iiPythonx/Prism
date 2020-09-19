# Modules
import discord
from requests import get

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Update(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Grabs the latest commit to Prism"
        self.usage = "update"

        self.url = "https://api.github.com/repos/ii-Python/Prism/commits"

    @commands.command()
    async def update(self, ctx):

        m = await ctx.send(embed = discord.Embed(title = "Fetching commits..", color = 0x126bf1))
        
        try:

            r = get(self.url).json()

            try:

                await m.delete()

            except:

                pass
        
        except:

            return await ctx.send(embed = Tools.error("Sorry, something went wrong while fetching update."))

        commit = r[0]["commit"]

        date = commit["committer"]["date"].split("T")[0]

        verification = f":white_check_mark:" if commit["verification"]["verified"] else ":x:"

        if commit["verification"]["signature"]:

            verification += f" ({commit['verification']['signature']})"

        embed = discord.Embed(title = commit["message"], url = "https://github.com/ii-Python/Prism/commit/" + commit["url"].split("/")[-1], color = 0x126bf1)
        
        embed.add_field(name = "Pushed by", value = commit["committer"]["name"], inline = False)

        embed.add_field(name = "Push verified", value = verification, inline = False)

        embed.add_field(name = "Pushed on", value = date, inline = False)

        embed.set_author(name = " | Update", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Update(bot))
