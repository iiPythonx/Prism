# MOdules
from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Clap(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Replaces spaces with clap emojis"
        self.usage = "clap [text]"

    @commands.command()
    async def clap(self, ctx, *, sentence: str = None):

        if not sentence:
            return await ctx.send(embed = Tools.error("No text specified to clap"))

        clapped_text = sentence.replace(" ", " :clap: ")

        try:
            return await ctx.send(clapped_text)

        except Exception:
            return await ctx.send(embed = Tools.error("That's too much text to clap."))

# Link to bot
def setup(bot):
    bot.add_cog(Clap(bot))
