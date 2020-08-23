# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Bank(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Setup your bank account"
        self.usage = "bank [bank id]"

        self.banks = [

            {
                "name": "Simple Banking",
                "limit": "75,000",
                "security": 3,
                "level": 5
            },
            {
                "name": "Penny Pocket Banking",
                "limit": "50,100",
                "security": 6,
                "level": 10
            },
            {
                "name": "Sheri Banking",
                "limit": "100,000",
                "security": 5,
                "level": 15
            },
            {
                "name": "Ormonde Banking",
                "limit": "500,000",
                "security": 8,
                "level": 20
            },
            {
                "name": "Clifton International Banking",
                "limit": "∞",
                "security": 9,
                "level": 100
            }
        ]

    @commands.command()
    async def bank(self, ctx, bank: int = None):

        db = loads(open("db/users", "r").read())

        user = db[str(ctx.author.id)]

        if not bank:

            c = 1

            embed = discord.Embed(title = "The National List of Banks", description = f"Change your bank with the `bank BANKID` command.\nCurrent provider: {user['bank']['data']['name']}." if user["bank"]["data"] else "Set your bank with the `bank BANKID` command.", color = 0x126bf1)

            for bank in self.banks:

                premium = "(premium only)" if bank["level"] == 100 else ""

                _bank = f"\n\tLimit: {bank['limit']}\n\tID: {c}\t\nSecurity: {bank['security']}/10\n\tRequired level: {c * 5}\n\t{premium}\n"

                embed.add_field(name = bank["name"], value = _bank)

                c += 1

            embed.set_author(name = " | Banks", icon_url = self.bot.user.avatar_url)

            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

            return await ctx.send(embed = embed)

        allowed = []

        c = 1

        for _ in self.banks:

            allowed.append(c)

            c += 1

        try:

            bank = int(bank)

        except:

            return await ctx.send(embed = Tools.error("That isn't a valid bank ID!"))

        if not bank in allowed:

            return await ctx.send(embed = Tools.error("That isn't a valid bank ID!"))

        bank = self.banks[bank - 1]

        if bank["level"] == 100 and not "premium" in user["data"]["tags"]:

            return await ctx.send(embed = Tools.error("That bank requires premium to use."))

        elif not user["data"]["levels"]["level"] >= bank["level"]:

            return await ctx.send(embed = Tools.error("You aren't a high enough level for that bank yet!"))

        elif user["bank"]["data"] and user["bank"]["data"]["name"] == bank["name"]:

            return await ctx.send(embed = Tools.error(f"You already use {bank['name']}."))

        embed = discord.Embed(title = f"You switched to {bank['name']}." if user["bank"]["data"] else f"You now use {bank['name']}.", color = 0x126bf1)

        user["bank"]["data"] = bank

        open("db/users", "w").write(dumps(db, indent = 4))

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Bank(bot))
