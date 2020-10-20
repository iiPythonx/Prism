# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Automod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Setup auto-moderation on your server"
        self.usage = "automod [option] [value]"
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def automod(self, ctx, option = None, value = None):
    
        db = loads(open("db/guilds", "r").read())
        data = db[str(ctx.guild.id)]["data"]["automod"]

        if not option:

            # gather configuration
            config = ""

            for key in data:

                config += f"`{key}`: `{data[key]}`\n"

            embed = discord.Embed(title = "Prism Automoderation", description = "Configure automod to give your server that nice clean shine.", color = 0x126bf1)

            embed.add_field(name = "Current Configuration", value = config, inline = False)

        elif not value:

            return await ctx.send(embed = Tools.error("No value specified to set."))

        else:

            return

        embed.set_author(name = " | Automod", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Automod(bot))
