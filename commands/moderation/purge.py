# Modules
import discord
from asyncio import sleep

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Purge(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Bulk deletes messages from a channel"
        self.usage = "purge [amount]"
        
    @commands.command(aliases = ["clear"])
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount: int = 5):

        if amount > 100:
            
            return await ctx.send(embed = Tools.error("The API doesn't allow more than 100 messages deleted at a time."))

        await ctx.channel.purge(limit = amount + 1)

        embed = discord.Embed(title = f"I have deleted {amount} messages from #{ctx.channel.name}.", color = 0x126bf1)
        
        embed.set_author(name = " | Purge", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        message = await ctx.send(embed = embed)
        
        await sleep(3)
        
        try:
            
            return await message.delete()

        except:

            pass

# Link to bot
def setup(bot):
    bot.add_cog(Purge(bot))
