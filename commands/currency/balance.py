# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Balance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "See how much money somebody has"
        self.usage = "balance [user]"

    @commands.command(aliases = ["bal"])
    async def balance(self, ctx, user: str = None):

        db = loads(open("db/users", "r").read())

        user = await Tools.getClosestUser(ctx, user if user else ctx.author)

        if not str(user.id) in db:
            
            return await ctx.send(embed = Tools.error(f"{user.name} doesn't have a Prism account."))

        _user = db[str(user.id)]

        _bal = _user["balance"]

        if len(str(_bal)) > 50:

            _bal = "∞"

        balance = f"<:coin:733723405118865479>\t{_bal} coins"

        name = user.name + "'s"

        if user.id == ctx.author.id:

            name = "Your"

        embed = discord.Embed(title = f"{name} Balance", description = balance, color = 0x126bf1)

        embed.set_author(name = " | Balance", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Balance(bot))
