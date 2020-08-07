# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads

from random import randint
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Gayness(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Check how gay somebody is (100% legit)"
        self.usage = "gay [user]"

    @commands.command()
    async def gay(self, ctx, user: discord.User = None):

        db = loads(open("db/guilds", "r").read())

        if not "nsfw-enabled" in db[str(ctx.guild.id)]["tags"]:

          return await ctx.send(embed = Tools.error("NSFW is not enabled in this server."))

        elif not ctx.channel.nsfw:

          return await ctx.send(embed = Tools.error("NSFW is not enabled in this channel."))

        elif not user:
            
            user = ctx.author

        rating = randint(0, 100)

        message = f"You are {rating}% gay."
        
        if ctx.author.id != user.id:
            
            message = f"{user.name} is {rating}% gay."
            
        embed = discord.Embed(title = message, color = 0x126bf1)
        
        embed.set_author(name = " | Gay", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Gayness(bot))
