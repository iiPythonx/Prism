# Modules
import discord
from json import loads

from random import randint
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Penis(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Calculates how big someones PP is (based on nuclear physics)"
        self.usage = "pp [user]"

    @commands.command(aliases = ["penis"])
    @commands.is_nsfw()
    async def pp(self, ctx, user: discord.User = None):

        db = loads(open("db/guilds", "r").read())

        if not "nsfw-enabled" in db[str(ctx.guild.id)]["tags"]:
          return await ctx.send(embed = Tools.error("NSFW is not enabled in this server."))

        user = await Tools.getClosestUser(ctx, user if user else ctx.author)

        pp = "8"
        size = randint(4, 10)
        counter = 0
        
        while counter < size:
            
            pp += "="
            counter += 1
            
        pp = f"{pp}D"

        message = f"Here is your PP:\n{pp}"
        
        if user.id != ctx.author.id:
            message = f"Here is {user.name}'s PP:\n{pp}"
            
        embed = discord.Embed(title = message, color = 0x126bf1)
        embed.set_author(name = " | PP", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Penis(bot))
