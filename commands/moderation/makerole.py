# Modules
import random
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Makerole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Creates a new role with a random color"
        self.usage = "makerole [role name]"
        
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def makerole(self, ctx, *, role_name: str = None):
    
        if not role_name:

            return await ctx.send(embed = Tools.error("No role name was specified."))

        elif len(role_name) > 100:

            return await ctx.send(embed = Tools.error("That name is too long to be a role."))

        elif len(ctx.guild.roles) == 250:

            return await ctx.send(embed = Tools.error("This server has the maximum number of roles allowed."))

        elif role_name.startswith("<@!"):

            role_name = self.bot.get_user(int(role_name.split("<@!")[1].split(">")[0])).name

        color = discord.Colour(random.randint(0, 0xFFFFFF))
            
        await ctx.guild.create_role(name = role_name, colour = color)
        
        embed = discord.Embed(description = "New server role created.", color = color)

        embed.add_field(name = "Role: ", value = role_name, inline = False)

        embed.add_field(name = "Color: ", value = color, inline = False)

        embed.set_author(name = " | New Role", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Makerole(bot))
    