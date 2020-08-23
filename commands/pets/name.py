# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Name(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Rename your pet to something fancy"
        self.usage = "name [text]"

    @commands.command(aliases = ["collar", "pname", "petname", "namepet"])
    async def name(self, ctx, *, name: str = None):

        if not name:

            return await ctx.send(embed = Tools.error("You need to specify a new pet name."))

        elif len(name) > 250 or "\n" in name:

            return await ctx.send(embed = Tools.error("Your name is too long."))

        elif "<@" in name:

          name = self.bot.get_user(int(name.split("<@!")[1].split(">")[0])).name

        db = loads(open("db/users", "r").read())

        if not db[str(ctx.author.id)]["pet"]["level"]:

            return await ctx.send(embed = Tools.error("You don't own a pet."))
          
        db[str(ctx.author.id)]["pet"]["name"] = name

        open("db/users", "w").write(dumps(db, indent = 4))

        embed = discord.Embed(title = f"Your pet has been renamed to {name}.", color = 0x126bf1)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Name(bot))
