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
        self.desc = "Check the Prism knowledgebase for a question"
        self.usage = "question [question]"
        
        self.client = wolframalpha.Client(getenv("WOLFRAMALPHA_KEY"))

    @commands.command(aliases = ["q", "ask"])
    async def question(self, ctx, *, question: str = None):

        if not question:
        
            return await ctx.send(embed = Tools.error("No question provided."))

        for user in ctx.message.mentions:

            question = question.replace(f"<@!{user.id}>", user.name)

        db = loads(open("db/guilds", "r").read())[str(ctx.guild.id)]["tags"]

        if not ctx.channel.nsfw and not "nsfw-enabled" in db:

            return await ctx.send(embed = Tools.error("This command can only be used in NSFW channels."))

        m = await ctx.send(embed = discord.Embed(title = "Searching.. this might take a minute.", color = 0x126bf1))

        res = self.client.query(question)

        try:

            await m.delete()

        except:

            pass

        try:

            embed = discord.Embed(color = 0x126bf1)

            embed.add_field(name = "Results:", value = next(res.results).text, inline = False)

            embed.set_author(name = " | Question", icon_url = self.bot.user.avatar_url)

            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

            return await ctx.send(embed = embed)

        except:

            return await ctx.send(embed = Tools.error("No results found."))      

# Link to bot
def setup(bot):
    bot.add_cog(Question(bot))
