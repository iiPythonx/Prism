# Modules
from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Say(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Makes the bot say something"
        self.usage = "say [text]"

    @commands.command()
    async def say(self, ctx, *, sentence: str = None):

        if not ctx.message.attachments:

            if not sentence:
            
                return await ctx.send(embed = Tools.error("No text specified to say."))

            return await ctx.send(sentence)

        else:

            if sentence:

                await ctx.send(sentence)

            return await ctx.send(ctx.message.attachments[0].url)

# Link to bot
def setup(bot):
    bot.add_cog(Say(bot))
