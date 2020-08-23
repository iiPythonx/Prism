# Modules
import discord
from asyncio import sleep

from random import randint

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Hack(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Hack anybody you want (105% legit)"
        self.usage = "hack [anything here]"

    def random_ip(self):

        return f"{randint(10, 99)}.{randint(10, 99)}.{randint(100, 999)}.{randint(10, 99)}"

    @commands.command()
    async def hack(self, ctx, *, somebody: str = None):

        if not somebody:
            
            return await ctx.send(embed = Tools.error("You forgot to specify who to hack. >_>"))

        message = await ctx.send(f"Now hacking {somebody}... :O")
    
        await sleep(2)

        await message.edit(content = "[▝] Targeting remote host (127.0.0.1)")

        await sleep(2)

        await message.edit(content = "[▗] Cracking Facebook password")

        await sleep(2)

        await message.edit(content = "[▖] Checking memes")

        await sleep(2)

        await message.edit(content = f"[▘] Hacking into bank ({self.random_ip()})")
        
        await sleep(2)
        
        await message.edit(content = "[▝] Calculating circumference")
        
        await sleep(2)
        
        await message.edit(content = "[▗] Doing some math")
        
        await sleep(2)
        
        await message.edit(content = f"[▖] Shutting off cameras @ {self.random_ip()}")
        
        await sleep(2)

        try:
        
            return await ctx.send(f"{ctx.author.mention}, {somebody} has been hacked.")

        except:

            return await ctx.send(embed = Tools.error("What the actual heck are you typing???"))

# Link to bot
def setup(bot):
    bot.add_cog(Hack(bot))
