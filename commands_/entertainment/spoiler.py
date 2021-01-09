# Modules
from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Spoiler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Turns text into a massive spoiler"
        self.usage = "spoiler [text]"

    @commands.command()
    async def spoiler(self, ctx, *, sentence = None):

        if not sentence:
            
            return await ctx.send(embed = Tools.error("No text specified."))

        message = ""

        for char in sentence:
            
            message = f"{message}||{char}||"

        try:

            return await ctx.send(message)
        
        except:
            
            return await ctx.send(embed = Tools.error("Your sentence is too long."))

# Link to bot
def setup(bot):
    bot.add_cog(Spoiler(bot))
