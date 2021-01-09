# Modules
import discord

from asyncio import sleep
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Train(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Trains your pet at the training center"
        self.usage = "train [levels]"

    @commands.command()
    async def train(self, ctx, levels: int = 1):

        db = loads(open("db/users", "r").read())
        
        user = db[str(ctx.author.id)]
        
        if not user["pet"]["level"]:
            
            return await ctx.send(embed = Tools.error("You don't own a pet."))
        
        train_price = (100 * user["pet"]["level"]) + (500 * levels)
        
        if not user["balance"] >= train_price:
            
            return await ctx.send(embed = Tools.error(f"You need an additional ${train_price - user['balance']} to train {user['pet']['name']}."))
        
        embed = discord.Embed(title = f"{user['pet']['name']} is now being trained..", color = 0x126bf1)

        message = await ctx.send(embed = embed)
        
        await sleep(3)
        
        db = loads(open("db/users", "r").read())

        user = db[str(ctx.author.id)]

        user["pet"]["level"] += levels

        user["balance"] -= train_price
        
        try:
            
            await message.delete()
            
        except:
            
            pass
        
        open("db/users", "w").write(dumps(db, indent = 4))
        
        embed = discord.Embed(title = f"{user['pet']['name']} has been trained and is now Level {user['pet']['level']}!", color = 0x126bf1)
        
        try:

          return await ctx.send(embed = embed)

        except:

          embed = discord.Embed(title = f"{user['pet']['name']} has been trained and is now Level ∞!", color = 0x126bf1)

          return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Train(bot))
