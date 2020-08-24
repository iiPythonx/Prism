# Modules
import discord
from random import choice

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Eightball(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Ask the magic eightball a question"
        self.usage = "eightball [question]"

    @commands.command(aliases = ["8ball"])
    async def eightball(self, ctx, *, question = None):

        if not question:
            
            return await ctx.send(embed = Tools.error("No question specified."))

        for member in ctx.message.mentions:

            question = question.replace(f"<@!{member.id}>", member.name)

        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        
        if not question.endswith("?"):
            
            question = f"{question}?"
            
        question = Tools.uppercase(question)

        question = question.replace(" i ", " I ")

        embed = discord.Embed(title = question, description = choice(responses), color = 0x126bf1)
        
        embed.set_author(name = " | Eightball", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Eightball(bot))
