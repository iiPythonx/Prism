# Modules
import discord
from random import randint

from json import loads, dumps
from discord.ext import commands

from assets.prism import Cooldowns, Tools

# Main Command Class
class Lottery(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Scratch's a lottery ticket"
        self.usage = "lottery"

    @commands.command(aliases = ["lotto"])
    async def lottery(self, ctx):
        
        db = loads(open("db/users", "r").read())
        
        if Cooldowns.on_cooldown(ctx, "lottery"):
            
            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "lottery"))
        
        elif db[str(ctx.author.id)]["balance"] < 250:
            
            return await ctx.send(embed = Tools.error("You need at least 250 coins to buy a lottery ticket."))
        
        db[str(ctx.author.id)]["balance"] -= 250
        
        if randint(1, 7) == 1:
        
            amount = randint(3700, 10000)
        
            db[str(ctx.author.id)]["balance"] += amount
            
            open("db/users", "w").write(dumps(db, indent = 4))
            
            embed = discord.Embed(title = f"Wow! You just won the lottery and gained {amount} coins.", color = 0x126bf1)
            
            embed.set_author(name = " | Lottery", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
            
            await ctx.send(embed = embed)
            
            return await Cooldowns.set_cooldown(ctx, "lottery", 600)
        
        open("db/users", "w").write(dumps(db, indent = 4))
        
        embed = discord.Embed(title = "Nope, your ticket wasn't a winner. Sorry mate.", color = 0x126bf1)
        
        embed.set_author(name = " | Lottery", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        await ctx.send(embed = embed)

        return await Cooldowns.set_cooldown(ctx, "lottery", 600)

# Link to bot
def setup(bot):
    bot.add_cog(Lottery(bot))
