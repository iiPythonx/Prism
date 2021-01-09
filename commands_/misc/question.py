# Modules
import discord
import wolframalpha

from os import getenv
from json import loads

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Question(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Make a request to wolframalpha"
        self.usage = "question [question]"

        self.key = getenv("WOLFRAMALPHA_KEY")
        self.client = None

        if self.key is not None:
            self.client = wolframalpha.Client(self.key)

    @commands.command(aliases = ["q", "ask", "wolfram", "wf"])
    async def question(self, ctx, *, question: str = None):

        if question is None:
            return await ctx.send(embed = Tools.error("No question provided."))

        elif self.client is None:
            return await ctx.send(embed = Tools.error("API key is missing so this command is disabled."))

        # Format mentions
        for user in ctx.message.mentions:
            question = question.replace(f"<@!{user.id}>", user.name)

        # Send alert
        msg = await ctx.send(embed = discord.Embed(title = "Searching...", description = "This process can take up to 45 seconds.", color = 0x126bf1))

        # Create query
        res = self.client.query(question)

        try:
            value = next(res.results).text

        except AttributeError:
            return await ctx.send(embed = Tools.error("No results were found."))

        # Construct embed
        embed = discord.Embed(description = value, color = 0x126bf1)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await msg.edit(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Question(bot))
