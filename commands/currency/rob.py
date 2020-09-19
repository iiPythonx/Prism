# Modules
import discord
from random import randint

from json import loads, dumps
from discord.ext import commands

from assets.prism import Cooldowns, Tools

# Main Command Class
class Rob(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Robs a user of their goodies ;)"
        self.usage = "rob [user]"

    @commands.command(aliases = ["steal"])
    async def rob(self, ctx, user = None):
        
        if Cooldowns.on_cooldown(ctx, "rob"):
            
            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "rob"))
        
        elif not user:
            
            return await ctx.send(embed = Tools.error("Please specify somebody to rob."))
        
        user = await Tools.getClosestUser(ctx, user)

        if user.id == ctx.author.id:
            
            return await ctx.send(embed = Tools.error("Stop trying to rob yourself."))
        
        elif user.id == self.bot.user.id:
            
            return await ctx.send(embed = Tools.error("Stop trying to rob me."))
        
        db = loads(open("db/users", "r").read())

        if not str(user.id) in db:

            return await ctx.send(embed = Tools.error(f"{user.name} doesn't have an account."))

        elif db[str(user.id)]["balance"] < 500:

            return await ctx.send(embed = Tools.error(f"Bruh, {user.name} is poor."))

        elif db[str(ctx.author.id)]["balance"] < 300:

            return await ctx.send(embed = Tools.error("You need at least 300 coins to rob someone."))

        elif randint(0, 1):

            # user wins
            earn = randint(250, round(db[str(user.id)]["balance"] / 2))

            db[str(user.id)]["balance"] -= earn

            db[str(ctx.author.id)]["balance"] += earn

            if (str(earn)) > 15:

                earn = "∞"

            embed = discord.Embed(title = "Nice :ok_hand:", description = f"You just robbed {user.name} and earned `{earn}` coins.", color = 0x126bf1)

        else:

            # caught
            fee = randint(300, round(db[str(ctx.author.id)]["balance"] / 2))

            db[str(ctx.author.id)]["balance"] -= fee

            embed = discord.Embed(title = "L O L", description = f"You failed miserably at robbing {user.name} and got caught!!!111\nYou paid `{fee}` coins as a fee.", color = 0xFF0000)

        embed.set_author(name = " | Rob", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = " | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        open("db/users", "w").write(dumps(db, indent = 4))

        await ctx.send(embed = embed)

        return await Cooldowns.set_cooldown(ctx, "rob", 3600)
        
# Link to bot
def setup(bot):
    bot.add_cog(Rob(bot))
