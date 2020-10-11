# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Unbans a member on the server"
        self.usage = "unban [user]"

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, user: str = None):
    
        if not user:
            
            return await ctx.send(embed = Tools.error("Please specify a user to unban."))

        user = await Tools.getBannedUser(ctx, user)

        try:

            await ctx.guild.unban(user)

        except Exception as e:

            print(e)  # temporary

            return await ctx.send(embed = Tools.error(f"Failed to unban {user.name} from the server."))

        return await ctx.send(embed = discord.Embed(title = f"{user.name} has been unbanned.", color = 0x126bf1))

# Link to bot
def setup(bot):
    bot.add_cog(Unban(bot))
