# Modules
import discord
from json import loads

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Pet(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Check out your pet"
        self.usage = "pet [user]"

    @commands.command()
    async def pet(self, ctx, user = None):

        db = loads(open("db/users", "r").read())

        user = await Tools.getClosestUser(ctx, user if user else ctx.author)

        if not str(user.id) in db:

            return await ctx.send(embed = Tools.error(f"{user.name} doesn't have an account."))

        elif not db[str(user.id)]["pet"]["level"]:

            if user.id == ctx.author.id:

                return await ctx.send(embed = Tools.error("You don't have a pet."))

            else:

                return await ctx.send(embed = Tools.error(f"{user.name} doesn't have a pet."))

        pet = db[str(user.id)]["pet"]

        level = pet["level"]

        if len(str(level)) > 50:

            level = "∞"

        embed = discord.Embed(title = pet["name"], color = 0x126bf1)

        embed.add_field(name = "Information", value = f"Name: {pet['name']}\nLevel: {level}\nType: {Tools.uppercase(pet['type'])}\nCurrently holding: {pet['holding']}\nAdopted on: {pet['adopted_on']}")

        embed.set_author(name = " | Pet", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f"Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Pet(bot))
