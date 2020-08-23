# Modules
from discord.ext import commands
from assets.prism import Constants, Tools

# Main Command Class
class Emojify(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Turns text into emojies"
        self.usage = "emojify [text]"

    @commands.command(aliases = ["emoji"])
    async def emojify(self, ctx, *, text = None):

        if not text:
            
            return await ctx.send(embed = Tools.error("No text specified."))

        message = ""

        for character in text:

            if character.lower() in Constants.alphabet:

                message = f"{message}:regional_indicator_{character.lower()}: "

            else:

                if character == " ":

                    message = f"{message}  "

                elif character == "#":

                    message = f"{message}:hash: "

                elif character == "$":

                    message = f"{message}:heavy_dollar_sign: "

                elif character == "1":

                    message = f"{message}:one: "

                elif character == "2":

                    message = f"{message}:two: "

                elif character == "3":

                    message = f"{message}:three: "

                elif character == "4":

                    message = f"{message}:four: "

                elif character == "5":

                    message = f"{message}:five: "

                elif character == "6":

                    message = f"{message}:six: "

                elif character == "7":

                    message = f"{message}:seven: "

                elif character == "8":

                    message = f"{message}:eight: "

                elif character == "9":

                    message = f"{message}:nine: "

                elif character == "0":

                    message = f"{message}:zero: "

                elif character == "!":

                    message = f"{message}:grey_exclamation: "

                elif character == "?":

                    message = f"{message}:grey_question: "

                elif character == ".":

                    message = f"{message}:white_circle: "

                else:

                    message = f"{message}{character}"

        try:
            
            return await ctx.send(message)
        
        except:
            
            return await ctx.send("Sorry, your text is too long to emojify.")

# Link to bot
def setup(bot):
    bot.add_cog(Emojify(bot))
