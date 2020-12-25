# Modules
import base64
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Decrypt(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Decrypt some text using the base64 format."
        self.usage = "decrypt [text]"

    @commands.command()
    async def decrypt(self, ctx, *, text: str = None):
 
        if not text:
            
            return await ctx.send(embed = Tools.error("No text specified to decrypt."))
 
        try:
            encrypted = base64.b64decode(text.encode("ascii")).decode("ascii")

        except ValueError:
            return await ctx.send(embed = Tools.error("Sorry, your text couldn't be decrypted."))

        # Embed construction
        embed = discord.Embed(title = "Decryption Results", description = f"```\n{encrypted}\n```", color = 0x126bf1)
        embed.set_author(name = " | Decrypt", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        # Handle sending
        try:
            return await ctx.send(embed = embed)

        except Exception:
            return await ctx.send(embed = Tools.error("Failed to send the embed, check your text."))

# Link to bot
def setup(bot):
    bot.add_cog(Decrypt(bot))
