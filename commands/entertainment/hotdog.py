# Modules
import discord
from random import randint

from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Hotdog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Throws a hotdog at a user"
        self.usage = "hotdog [user]"

    @commands.command()
    async def hotdog(self, ctx, user = None):

        if not user:

            return await ctx.send(embed = Tools.error("Mcbruh, who you tryna hit?"))

        user = await Tools.getClosestUser(ctx, user)

        db = loads(open("db/users", "r").read())

        await ctx.send(str(user))

        if not Tools.has_flag(db, ctx.author, "premium"):

            return await ctx.send(embed = Tools.error("You need premium to use this command."))

        elif not str(user.id) in db:

            return await ctx.send(embed = Tools.error(f"{user.name} does not have a Prism account."))

        _user = db[str(ctx.author.id)]

        __user = db[str(user.id)]
        
        inventory = _user["data"]["inventory"]

        if not "Hotdog" in inventory:

            return await ctx.send(embed = Tools.error("You don't have any hotdogs! Buy some with the ``shop`` command."))

        inventory["Hotdog"]["count"] -= 1

        if inventory["Hotdog"]["count"] == 0:

            inventory.pop("Hotdog")

        if randint(1, 2) == 1:

            amt = randint(100, 1000)

            _user["balance"] += amt

            __user["balance"] -= amt

        else:

            amt = None

        open("db/users", "w").write(dumps(db, indent = 4))

        if amt:

            embed = discord.Embed(title = f"You just threw your hotdog at {user.name}!", description = f"They dropped {amt} coins!", color = 0x126bf1)

        else:

            embed = discord.Embed(title = "Oh no, you threw the hotdog but missed! loser", color = 0x126bf1)

        embed.set_author(name = " | Hotdog", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Hotdog(bot))
