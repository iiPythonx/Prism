# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Dump(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sends your pet back to the shelter"
        self.usage = "shelter"

    @commands.command(aliases = ["dump"])
    async def shelter(self, ctx):

        def check(m):

            return m.author == ctx.author and m.channel == ctx.channel

        db = loads(open("db/users", "r").read())

        if not db[str(ctx.author.id)]["pet"]["level"]:

            return await ctx.send(embed = Tools.error("Sorry, but you don't own a pet."))

        embed = discord.Embed(title = f"Are you sure you want to send {db[str(ctx.author.id)]['pet']['name']} back to the shelter?", color = 0x126bf1)

        m = await ctx.send(embed = embed)

        message = await self.bot.wait_for("message", check = check)

        try:

            await m.delete()

        except:

            pass

        if not message.content.lower() in ["yes", "yea", "yup", "ye"]:

            embed = discord.Embed(title = "You decided to look away from the shelter.", color = 0x126bf1)

            return await ctx.send(embed = embed)

        name = db[str(ctx.author.id)]["pet"]["name"]

        db[str(ctx.author.id)]["pet"]["name"] = None

        db[str(ctx.author.id)]["pet"]["level"] = None

        db[str(ctx.author.id)]["pet"]["type"] = None

        db[str(ctx.author.id)]["pet"]["holding"] = None

        open("db/users", "w").write(dumps(db, indent = 4))

        embed = discord.Embed(title = f"You sent {name} back to the adoption shelter.", color = 0x126bf1)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Dump(bot))
