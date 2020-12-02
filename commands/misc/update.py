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

        await ctx.send(embed = discord.Embed(title = "Fetching commits...", color = 0x126bf1), delete_after = 0)
        
        try:
            r = get(self.url, timeout = 2).json()

            try: await m.delete()
            except: pass
        
        except:
            return await ctx.send(embed = Tools.error("Sorry, something went wrong while fetching updates."))

        commit = r[0]
        _commit = commit["commit"]
        verification = f":white_check_mark:" if _commit["verification"]["verified"] else ":x:"

        embed = discord.Embed(
            title = "Latest update: " + _commit["message"][0].lower() + _commit["message"][1:],
            description = "Click [here](https://github.com/ii-Python/Prism/commits) to view previous updates.",
            url = "https://github.com/ii-Python/Prism/commit/" + _commit["url"].split("/")[-1],
            color = 0x126bf1
        )
        
        embed.add_field(name = "Pushed by", value = commit["author"]["login"])
        embed.add_field(name = "Push verified", value = verification)
        embed.add_field(name = "Pushed on", value = _commit["committer"]["date"].split("T")[0])
        embed.add_field(name = "Push signature", value = commit["sha"][:-(len(commit["sha"]) - 7)])

        embed.set_author(name = " | Update", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Update(bot))
