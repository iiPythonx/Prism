# Prism Rewrite - Basic Command

# Modules
import discord
from random import randint

from json import loads, dumps

from discord.ext import commands
from assets.prism import Tools, Cooldowns

# Main Command Class
class Sue(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sue somebody"
        self.usage = "sue [user] [reason]"

    @commands.command()
    async def sue(self, ctx, user: discord.User = None, *, reason: str = None):

        if Cooldowns.on_cooldown(ctx, "sue"):
            
            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "sue"))

        db = loads(open("db/users", "r").read())

        if not user:
            
            return await ctx.send(embed = Tools.error("Bruh, who are you trying to sue?"))

        elif not str(user.id) in db:

            return await ctx.send(embed = Tools.error(f"{user.name} doesn't have a Prism bank account."))

        elif user == ctx.author:

            return await ctx.send(embed = Tools.error("You cannot sue yourself."))

        default = f"{ctx.author.name} is suing {user.name}"

        if not reason:

            text = default + "."

            reason = ""

        else:

            text = default + " for:"

        embed = discord.Embed(title = text, description = reason, color = 0x126bf1)

        await ctx.send(embed = embed)

        if randint(1, 3) == 1:

            fee = round(db[str(ctx.author.id)]["balance"] / randint(5, 8))

            if fee == 0:

                embed = discord.Embed(title = "You're so poor that the opposing side dropped the charges.", color = 0x126bf1)

                embed.set_author(name = " | Lawsuit Dropped", icon_url = self.bot.user.avatar_url)

                return await ctx.send(embed = embed)

            db[str(ctx.author.id)]["balance"] -= fee

            db[str(user.id)]["balance"] += fee

            open("db/users", "w").write(dumps(db, indent = 4))

            embed = discord.Embed(title = f"You lost the lawsuit and payed {fee} coins.", description = f"I bet {user.name} is laughing so hard right now.", color = 0x126bf1)

            return await ctx.send(embed = embed)

        else:

            success = randint(1300, 8275)

            db[str(user.id)]["balance"] -= success

            db[str(ctx.author.id)]["balance"] += success

            open("db/users", "w").write(dumps(db, indent = 4))

            embed = discord.Embed(title = f"You won the lawsuit and gained {success} coins.", description = "Well played.", color = 0x126bf1)

            embed.set_author(name = " | Lawsuit", icon_url = self.bot.user.avatar_url)

            await ctx.send(embed = embed)

            return await Cooldowns.set_cooldown(ctx, "sue", 3600)

# Link to bot
def setup(bot):
    bot.add_cog(Sue(bot))
