# Modules
import discord
from random import randint

from json import loads, dumps
from discord.ext import commands

from assets.prism import Tools, Constants, Cooldowns

# Main Command Class
class Work(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Work for some coins"
        self.usage = "work"

    @commands.command()
    async def work(self, ctx):
        
        if Cooldowns.on_cooldown(ctx, "work"):
            
            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "work"))
        
        n1 = randint(1, 20)

        n2 = randint(1, 20)

        answer = n1 + n2

        bot_msg = await ctx.send(f"You are now working; solve the equation: `{n1} + {n2}`.")
        
        db = loads(open("db/users", "r").read())
        
        def check(m):

            return m.author == ctx.author and m.channel == ctx.channel

        try:

            message = await self.bot.wait_for("message", check = check, timeout = 5)
        
        except:

            earnings = randint(20, 100)

            db[str(ctx.author.id)]["balance"] += earnings
            
            open("db/users", "w").write(dumps(db, indent = 4))

            return await ctx.send(embed = Tools.error(f"You didn't respond fast enough; but you still earned {earnings} coins."))
        
        try:
            
            await bot_msg.delete()
            
        except:
            
            pass
        
        if not message.content.lower() == str(answer):
            
            earnings = randint(20, 100)

            db[str(ctx.author.id)]["balance"] += earnings
            
            open("db/users", "w").write(dumps(db, indent = 4))

            await ctx.send(embed = Tools.error(f"You messed up at work; but you still earned {earnings} coins."))
            
            return await Cooldowns.set_cooldown(ctx, "work", 600)
        
        reward = randint(200, 450)
            
        db[str(ctx.author.id)]["balance"] += reward
            
        open("db/users", "w").write(dumps(db, indent = 4))
            
        embed = discord.Embed(title = f"Good job, you went to work and earned {reward} coins.", color = 0x126bf1)
        
        embed.set_author(name = " | Work", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
            
        await ctx.send(embed = embed)            
        
        return await Cooldowns.set_cooldown(ctx, "work", 600)
        
# Link to bot
def setup(bot):
    bot.add_cog(Work(bot))
