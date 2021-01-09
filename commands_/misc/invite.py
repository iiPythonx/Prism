# Modules
import discord
from discord.ext import commands

# Main Command Class
class Invite(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Invite Prism to your own server"
        self.usage = "invite"
        
    @commands.command()
    async def invite(self, ctx):
            
        embed = discord.Embed(title = "Click here to invite Prism to your server.", url = f"https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot", color = 0x126bf1)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
            
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Invite(bot))
