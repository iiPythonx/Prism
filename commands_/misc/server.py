# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Server(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Gets a bunch of information on the server"
        self.usage = "server"
        
    @commands.command(aliases = ["serverinfo", "serverinformation", "si", "guild", "guildinfo", "guildinformation", "gi"])
    async def server(self, ctx):

        information = f"""
            Name: {ctx.guild.name}
            Server owner: {ctx.guild.owner.name}
            Member count: {ctx.guild.member_count}
            Region: {ctx.guild.region}
            Verification level: {Tools.uppercase(str(ctx.guild.verification_level))}
            Created on: {ctx.guild.created_at.__format__('%A, %d. %B %Y, at %H:%M:%S')}
            Role count: {len(ctx.guild.roles) - 1}
            Emoji count: {len(ctx.guild.emojis)}
        """

        embed = discord.Embed(title = Tools.uppercase(ctx.guild.name), color = 0x126bf1)
       
        embed.add_field(name = "Information", value = information, inline = False)
      
        embed.set_image(url = ctx.guild.icon_url)
     
        embed.set_author(name = " | Server Information", icon_url = self.bot.user.avatar_url)
     
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Server(bot))
