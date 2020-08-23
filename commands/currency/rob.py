# Modules
import random
import discord

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
        
        victim = db[str(user.id)]
        
        author = db[str(ctx.author.id)]
        
        if victim["balance"] < 100:
          
          return await ctx.send(embed = Tools.error(f"{user.name} doesn't even have 100 coins."))
        
        elif Tools.has_flag(db, user, "protected"):
          
          return await ctx.send(embed = Tools.error(f"{user.name} has a Bank Lock active."))

        if random.randint(1, 3) == 1:
            
            fine = random.randint(75, 310)
            
            author["balance"] -= fine
            
            open("db/users", "w").write(dumps(db, indent = 4))
            
            await ctx.send(embed = Tools.error(f"You got busted and were fined {fine} coins."))

            return await Cooldowns.set_cooldown(ctx, "rob", 3600)
        
        number = random.randint(1, 5)
        
        if number == 1:
            
            author["balance"] += victim["balance"]
                
            bal = victim["balance"]

            victim["balance"] = 0

            embed = discord.Embed(title = f"You just robbed {user.name} for {bal} coins and made them go broke.", color = 0x126bf1)
            
            embed.set_author(name = " | Rob", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Robbed by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        elif number in range(2, 4):
            
            author["balance"] += round((victim["balance"] / 3) * 2)

            bal = victim["balance"]

            victim["balance"] -= round((victim["balance"] / 3) * 2)
                
            embed = discord.Embed(title = f"You just robbed {user.name} for {round((bal / 3) * 2)} coins.", color = 0x126bf1)
            
            embed.set_author(name = " | Rob", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Robbed by {ctx.author}.", icon_url = ctx.author.avatar_url)

        else:
            
            author["balance"] += round(victim["balance"] / 3)

            bal = victim["balance"]

            victim["balance"] -= round(victim["balance"] / 3)
                
            embed = discord.Embed(title = f"You just robbed {user.name} for {round(bal / 3)} coins.", color = 0x126bf1)
            
            embed.set_author(name = " | Rob", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Robbed by {ctx.author}.", icon_url = ctx.author.avatar_url)

        try:

            await ctx.send(embed = embed)
        
        except:

            if number == 1:

                embed = discord.Embed(title = f"You just robbed {user.name} for their whole wallet.", color = 0x126bf1)
            
            else:

                embed = discord.Embed(title = f"You just robbed {user.name} for ∞ coins.", color = 0x126bf1)
            
            embed.set_author(name = " | Rob", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Robbed by {ctx.author}.", icon_url = ctx.author.avatar_url)

            await ctx.send(embed = embed)

        open("db/users", "w").write(dumps(db, indent = 4))

        return await Cooldowns.set_cooldown(ctx, "rob", 3600)
        
# Link to bot
def setup(bot):
    bot.add_cog(Rob(bot))
