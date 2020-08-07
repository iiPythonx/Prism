# Prism Rewrite - Basic Command

# Modules
from discord.ext import commands

# Main Command Class
class TTS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Make the bot speak"
        self.usage = "tts [text]"
        self.tags = []

    @commands.command(aliases = ["text2speech", "texttospeech", "speak", "speech"])
    async def tts(self, ctx, *, sentence: str = None):

        if not sentence:
            
            return await ctx.send("I can't speak if you don't give me anything to say. >:C")

        try:
    
            return await ctx.send(sentence, tts = True)
        
        except:
            
            return await ctx.send("I don't have permission to send TTS messages.")

# Link to bot
def setup(bot):
    bot.add_cog(TTS(bot))
