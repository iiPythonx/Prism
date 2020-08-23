# Modules
import discord
from discord.ext import commands

# Main Command Class
class Credits(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Check out everybody that helped make Prism"
        self.usage = "credits"

    @commands.command()
    async def credits(self, ctx):
 
        embed = discord.Embed(description = "Some of the coolest people on Earth.", color = 0x126bf1)

        embed.add_field(name = "Developers", value = "<@633185043774177280>", inline = False)

        embed.add_field(name = "Testers", value = "<@666839157502378014>\n<@403375652755079170>", inline = False)

        embed.add_field(name = "Bug Finders", value = "<@461629094661062656>\n<@667042599659634701>\n<@398826428608544772>", inline = False)

        embed.add_field(name = "Other Cool Bots", value = "<@526154953082011658>", inline = False)

        embed.set_author(name = " | Credits", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Credits(bot))
