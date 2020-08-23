# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from discord.ext import commands
from random import choice, randint

from assets.prism import Cooldowns, Tools

# Main Command Class
class Beg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Beg some people on the street for money"
        self.usage = "bet [user]"
        
        self.people = [
            "Elon Musk", "PewDiePie", "DanTDM", "Peppa Pig", "Rythm", "Benjamin", "yourself", "Dank Memer",
            "the Doge King", "a Python", "Dani", "Blicky", "Bill Gates", "Steve Jobs", "Jackscepticeye",
            "Lazarbeam", "DanTDM's Child"
        ]

    @commands.command()
    async def beg(self, ctx, member: str = None):

        user = choice(self.people)

        if randint(1, 10) == 1:

            user = "Commuter"

        if member:
            
            member = await Tools.getClosestUser(ctx, member)

            user = member.name

        elif Cooldowns.on_cooldown(ctx, "beg"):
            
            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "beg"))

        amount = randint(10, 75)

        db = loads(open("db/users", "r").read())
            
        db[str(ctx.author.id)]["balance"] += amount
        
        embed = discord.Embed(title = f"You begged {user} for coins and gained {amount} coins.", color = 0x126bf1)
        
        embed.set_author(name = " | Beg", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        await ctx.send(embed = embed)
        
        open("db/users", "w").write(dumps(db, indent = 4))

        return await Cooldowns.set_cooldown(ctx, "beg", 60)

# Link to bot
def setup(bot):
    bot.add_cog(Beg(bot))
