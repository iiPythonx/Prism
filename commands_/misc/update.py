# Modules
import discord
import requests

from json import loads
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Update(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Grabs the latest commit to Prism"
        self.usage = "update"

        self.url = "https://api.github.com/repos/ii-Python/Prism/commits"
        self.config = loads(open("config.json", "r").read())

    @commands.command()
    async def update(self, ctx, branch: str = ""):

        await ctx.send(embed = discord.Embed(title = "Fetching commits...", color = 0x126bf1), delete_after = 0)

        # Branch identifier
        if branch != "":
            branch = "/" + branch

        # Make request
        try:
            r = requests.get(self.url + branch, timeout = 2)

            # Check if branch was not found
            if r.status_code == 404:
                return await ctx.send(embed = Tools.error("Specified branch does not exist."))

            # Convert to JSON
            r = r.json()

        except requests.exceptions.ConnectionError:
            return await ctx.send(embed = Tools.error("Sorry, something went wrong while fetching updates."))

        # Load data
        try:
            commit = r[0]

        except KeyError:
            commit = r  # Branches with only one commit

        _commit = commit["commit"]
        verification = ":white_check_mark:" if _commit["verification"]["verified"] else ":x:"

        # Embed construction
        embed = discord.Embed(
            title = f"Running Prism {self.config['release']}",
            description = f"Latest github push: {_commit['message']}\nClick [here](https://github.com/ii-Python/Prism/commits) to view previous updates.",
            url = "https://github.com/ii-Python/Prism/commit/" + _commit["url"].split("/")[-1],
            color = 0x126bf1
        )

        embed.add_field(name = "Pushed by", value = commit["author"]["login"])
        embed.add_field(name = "Push verified", value = verification)
        embed.add_field(name = "Pushed on", value = _commit["committer"]["date"].split("T")[0])
        embed.add_field(name = "Push signature", value = commit["sha"][:-(len(commit["sha"]) - 7)])
        embed.add_field(name = "Branch", value = branch[1:] if branch else "stable")

        embed.set_author(name = " | Update", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Update(bot))
