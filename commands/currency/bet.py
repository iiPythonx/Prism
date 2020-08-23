# Modules
import discord
from random import randint

from json import loads, dumps
from discord.ext import commands

from assets.prism import Tools, Cooldowns

# Main Command Class
class Bet(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Flip a coin for some money"
        self.usage = "bet [amount]"

    @commands.command()
    async def bet(self, ctx, amount = None):

        if not amount:
            
            return await ctx.send(embed = Tools.error("No amount specified to bet."))

        db = loads(open("db/users", "r").read())

        try:

            amount = int(amount)

            if amount < 1:

                return await ctx.send(embed = Tools.error("Please enter a valid integer."))

        except:

            if amount.lower() != "all":

                return await ctx.send(embed = Tools.error("That isn't a number."))

            amount = db[str(ctx.author.id)]["balance"]

        if len(str(amount)) > 50 and amount != db[str(ctx.author.id)]["balance"]:

            return await ctx.send(embed = Tools.error("That's way too much money."))

        elif Cooldowns.on_cooldown(ctx, "bet"):
            
            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "bet"))

        elif db[str(ctx.author.id)]["balance"] < amount:
            
            return await ctx.send(embed = Tools.error(f"You don't have {amount} coins in your account."))

        elif randint(1, 2) == 1:
            
            db[str(ctx.author.id)]["balance"] += amount

            if len(str(amount)) > 50:

                amount = "∞"
            
            embed = discord.Embed(title = f"Darn, you win {amount} coins.", color = 0x126bf1)
            
            embed.set_author(name = " | Bet", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
            
            await ctx.send(embed = embed)
            
        else:
            
            db[str(ctx.author.id)]["balance"] -= amount
            
            if len(str(amount)) > 50:

                amount = "∞"

            embed = discord.Embed(title = f"Ha, you lose {amount} coins.", color = 0x126bf1)
            
            embed.set_author(name = " | Bet", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
            
            await ctx.send(embed = embed)
        
        open("db/users", "w").write(dumps(db, indent = 4))

        return await Cooldowns.set_cooldown(ctx, "bet", 60)

# Link to bot
def setup(bot):
    bot.add_cog(Bet(bot))
