# Prism Rewrite - Basic Command

# Modules
from requests import get
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Ascii(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Turns text into ascii art"
    self.usage = "ascii [text]"

  @commands.command()
  async def ascii(self, ctx, *, sentence: str = None):

    if not sentence:
        
      return await ctx.send(embed = Tools.error("No text was specified."))

    elif sentence.startswith("<@!") and sentence.endswith(">"):

      sentence = self.bot.get_user(int(sentence.split("<@!")[1].split(">")[0])).name

    text = f"``{get(f'http://artii.herokuapp.com/make?text={sentence}').text}``"

    if text == "````":

      return await ctx.send(embed = Tools.error("Ruh roh raggy, you broke ascii."))

    try:

      return await ctx.send(text)

    except:

      return await ctx.send(embed = Tools.error("Your text was too long to turn into ascii art."))

# Link to bot
def setup(bot):
  bot.add_cog(Ascii(bot))
