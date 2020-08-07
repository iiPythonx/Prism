# Prism Rewrite - Basic Command

# Modules
import discord
from random import randint

from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Use(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Consume / use an item in your inventory"
        self.usage = "use [item]"

    @commands.command(aliases = ["consume"])
    async def use(self, ctx, item: str = None):

        if not item:

            return await ctx.send(embed = Tools.error("No item specified to use."))

        return await ctx.send("wip")

        user = Tools.getClosestUser(ctx, user)

        if not user:

            return await ctx.send(embed = Tools.error("Yea I don't think that's an actual person."))

        db = loads(open("db/users", "r").read())

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

            embed = discord.Embed(title = "Woops! Your hotdog missed! oh no :(", color = 0x126bf1)

        embed.set_author(name = " | Hotdog", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Use(bot))
