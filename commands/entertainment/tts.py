# Modules
from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class TTS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Make the bot speak"
        self.usage = "tts [text]"

    @commands.command(aliases = ["text2speech", "texttospeech", "speak", "speech"])
    async def tts(self, ctx, *, sentence: str = None):

        if not sentence:
            
            return await ctx.send(embed = Tools.error("No text specified."))

        try:
    
            return await ctx.send(sentence, tts = True)
        
        except:
            
            return await ctx.send(embed = Tools.error("Missing permissions to send TTS messages."))

# Link to bot
def setup(bot):
    bot.add_cog(TTS(bot))
