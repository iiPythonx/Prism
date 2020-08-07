# Prism Rewrite - Basic Command

# Modules
import discord
from random import choice

from discord.ext import commands

# Main Command Class
class NHiE(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Generate a random 'never have I ever' question"
        self.usage = "neverhaveiever"

    @commands.command(aliases = ["nhie"])
    async def neverhaveiever(self, ctx):

        options = [
            "walked a dog",
            "went to a bar",
            "made friends with Benjamin",
            "made some ascii text",
            "peed in a pool",
            "had diarrhea and vomited simultaneously",
            "worn crocs",
            "walked a tight-rope",
            "been chased by a dog",
            "farted in an elevator",
            "used the bathroom in darkness",
            "pretended to be a burglar",
            "pranked my parents",
            "kissed a stranger",
            "dyed my hair the wrong color",
            "tried watching television upside down",
            "killed a pet by accident",
            "been trapped in an elevator",
            "driven a car naked",
            "woken someone up by snoring",
            "given someone a black eye"
        ]

        embed = discord.Embed(title = f"Never have I ever {choice(options)}.", color = 0x126bf1)
        
        embed.set_author(name = " | Never Have I Ever", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(NHiE(bot))
