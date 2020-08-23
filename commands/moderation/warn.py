# Modules
import discord
from json import loads, dumps

from discord.ext import commands
from assets.prism import Tools, Constants

# Main Command Class
class Warn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Warns a member on the server"
        self.usage = "warn [user] [reason]"
        
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def warn(self, ctx, user: discord.Member = None, *, reason: str = None):
    
        if not user:
            
            return await ctx.send(embed = Tools.error("No user specified to warn."))

        elif user.id == ctx.author.id:
            
            return await ctx.send(embed = Tools.error("You cannot warn yourself."))
        
        elif user.id == self.bot.user.id:
            
            return await ctx.send(embed = Tools.error("You cannot warn me; I'm a bot."))

            
            if reason and len(reason) > 200:
                
                return await ctx.send(embed = Tools.error("Your reason is too long."))
            
            else:
                
                if not reason:
                
                    reason = ""

        db = loads(open("db/users", "r").read())

        if not str(user.id) in db:

            db[str(user.id)] = Constants.user_preset

        if not str(ctx.guild.id) in db[str(user.id)]["data"]["warnings"]:
            
            db[str(user.id)]["data"]["warnings"][str(ctx.guild.id)] = [f"{ctx.author.mention}: {reason}"]
        
        else:
            
            db[str(user.id)]["data"]["warnings"][str(ctx.guild.id)].append(f"{ctx.author.mention}: {reason}")

        open("db/users", "w").write(dumps(db, indent = 4))

        try:

            embed = discord.Embed(title = f"You have been warned on {ctx.guild.name}.", description = reason, color = 0x126bf1)
         
            embed.set_author(name = " | Warning", icon_url = self.bot.user.avatar_url)
         
            embed.set_footer(text = f" | Warned by {ctx.author}.", icon_url = ctx.author.avatar_url)

            await user.send(embed = embed)
                
        except:
            
            reason = f"{reason}\nThis is just a server warning due to privacy settings."

        embed = discord.Embed(title = f"{ctx.author.name} just warned {user.name}.", description = reason, color = 0x126bf1)
     
        embed.set_author(name = " | Warn", icon_url = self.bot.user.avatar_url)
     
        embed.set_footer(text = f" | Warned by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Warn(bot))
