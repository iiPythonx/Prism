# Modules
import base64
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Encrypt(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Encrypts some text using the base64 format."
        self.usage = "encrypt [text]"

    @commands.command()
    async def encrypt(self, ctx, *, text: str = None):
 
        if not text:
            
            return await ctx.send(embed = Tools.error("No text specified to encrypt."))
 
        elif len(text) > 200:
            
            return await ctx.send(embed = Tools.error("Text is too long, it should be 200 at max."))
 
        try:

            encrypted = base64.b64encode(text.encode("ascii")).decode("ascii")

        except:

            return await ctx.send(embed = Tools.error("Sorry, your text couldn't be encrypted."))

        embed = discord.Embed(title = "Encryption Results", description = f"```\n{encrypted}\n```", color = 0x126bf1)

        embed.set_author(name = " | Encrypt", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        try:

            return await ctx.send(embed = embed)

        except:

            return await ctx.send(embed = Tools.error("Failed to send the embed, check your text."))

# Link to bot
def setup(bot):
    bot.add_cog(Encrypt(bot))
