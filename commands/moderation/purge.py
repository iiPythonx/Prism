# Modules
import discord
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
            
            return await ctx.send(embed = Tools.error("You cannot delete more than 100 messages at a time."))

        try:

            await ctx.channel.purge(limit = amount + 1)

        except:

            return await ctx.send(embed = Tools.error("Something went wrong while deleting those."))

        embed = discord.Embed(title = f"{amount} messages have been deleted from #{ctx.channel.name}.", color = 0x126bf1)
        
        embed.set_author(name = " | Purge", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        message = await ctx.send(embed = embed, delete_after = 3)

# Link to bot
def setup(bot):
    bot.add_cog(Purge(bot))
