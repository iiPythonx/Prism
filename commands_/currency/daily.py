# Modules
import discord
from json import loads, dumps

from discord.ext import commands
from assets.prism import Cooldowns

# Main Command Class
class Daily(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Redeems your daily amount of coins"
        self.usage = "daily"

    @commands.command(aliases = ["redeem"])
    async def daily(self, ctx):
        
        if Cooldowns.on_cooldown(ctx, "daily"):
            
            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "daily"))
 
        db = loads(open("db/users", "r").read())
 
        try:

          redeem = round(db[str(ctx.author.id)]["balance"] / 4)
        
        except:

          db[str(ctx.author.id)]["balance"] += 1000000000

          open("db/users", "w").write(dumps(db, indent = 4))
  
          embed = discord.Embed(title = f"You have redeemed ∞ daily coins.\n( Because your too rich for division ;) )", color = 0x126bf1)
          
          embed.set_author(name = " | Daily", icon_url = self.bot.user.avatar_url)
          
          embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

          await ctx.send(embed = embed)
          
          return await Cooldowns.set_cooldown(ctx, "daily", 86400)

        if len(str(db[str(ctx.author.id)]["balance"])) > 50:

          db[str(ctx.author.id)]["balance"] += 1000000000

          open("db/users", "w").write(dumps(db, indent = 4))
  
          embed = discord.Embed(title = f"You have redeemed ∞ daily coins.\n( Because you're too rich for division ;) )", color = 0x126bf1)
          
          embed.set_author(name = " | Daily", icon_url = self.bot.user.avatar_url)
          
          embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

          await ctx.send(embed = embed)
          
          return await Cooldowns.set_cooldown(ctx, "daily", 86400)

        db[str(ctx.author.id)]["balance"] += redeem
        
        if redeem == 0:
            
            redeem = 15
 
        open("db/users", "w").write(dumps(db, indent = 4))
 
        embed = discord.Embed(title = f"You have redeemed {redeem} daily coins.", color = 0x126bf1)
        
        embed.set_author(name = " | Daily", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        await ctx.send(embed = embed)
        
        return await Cooldowns.set_cooldown(ctx, "daily", 86400)

# Link to bot
def setup(bot):
    bot.add_cog(Daily(bot))
