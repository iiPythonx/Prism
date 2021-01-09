# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Premium(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Maybe this is where you get premium"
        self.usage = "premium"

    @commands.command(aliases = ["upgrade"])
    async def premium(self, ctx):

        db = loads(open("db/users", "r").read())

        if not Tools.has_flag(db, ctx.author, "premium"):

            if ctx.author in self.bot.get_guild(729513002302177311).members:

                db[str(ctx.author.id)]["balance"] += 10000

                db[str(ctx.author.id)]["data"]["tags"].append("premium")

                open("db/users", "w").write(dumps(db, indent = 4))

                embed = discord.Embed(title = "You have redeemed Prism Premium!", description = "You have gained 10k coins and have a premium badge on your profile.", color = 0x0ee323)

                return await ctx.send(embed = embed)

        has_premium = True if Tools.has_flag(db, ctx.author, "premium") else False

        embed = discord.Embed(title = "Prism Premium :medal:", description = f"Bragging rights for everbody :)\nPremium status: {has_premium}", color = 0x126bf1)

        embed.add_field(name = "Benefits", value = ":medal: Exclusive badge on your profile\n:moneybag: Payout of 10k daily coins\n:man_scientist: Access to expirimental commands\n:name_badge: Access to premium-only commands\n:man_artist: Future access to the character customizer", inline = False)

        embed.add_field(name = "How to get premium", value = "Prism will never be a paid-for bot; which means premium is\ncompletely free.\n\nTo get premium follow these steps:\n1. Join `discord.gg/KhvXWTr`.\n2. Reuse the `premium` command.\n3. Tada, Prism should let you redeem premium. :D", inline = False)

        embed.set_author(name = " | Premium", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Premium(bot))
