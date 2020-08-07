# Prism Rewrite - Basic Command

# Modules
import random

from discord.ext import commands

# Main Command Class
class Weirdtext(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Messes with a sentence's capitalization"
        self.usage = "weirdtext [text]"
        self.tags = []

    @commands.command()
    async def weirdtext(self, ctx, *, sentence = None):

        if not sentence:
            
            return await ctx.send("Please specify something to transform.")

        message = ""
        
        for char in sentence:
            
            if random.randint(1, 2) == 1:
                
                message = f"{message}{char.upper()}"
                
            else:
                
                message = f"{message}{char.lower()}"

        return await ctx.send(message)

# Link to bot
def setup(bot):
    bot.add_cog(Weirdtext(bot))
