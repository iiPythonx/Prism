# Modules
import discord
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class UserInformation(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Fetches a user's discord information"
    self.usage = "user"
      
  @commands.command(aliases = ["ui", "userinformation"])
  async def user(self, ctx, user = None):

    user = await Tools.getClosestUser(ctx, user if user else ctx.author, True)

    def getStatus(status):

      status = status.value

      if status == "online":

        return ":green_circle: Online"

      elif status == "idle":

        return ":yellow_circle: Idle"

      elif status == "dnd":

        return ":red_circle: DnD"

    embed = discord.Embed(title = "User Information", color = 0x126bf1)

    embed.add_field(name = "Full Name", value = user)

    if user.nick:

      embed.add_field(name = "Nickname", value = user.nick)

    if user.premium_since:

      embed.add_field(name = "Nitro", value = user.premium_since)

    if user.is_on_mobile():

      embed.add_field(name = "On Mobile", value = "Yes")

    if user.activity:

      embed.add_field(name = "Status", value = user.activity.name)

    embed.add_field(name = "Animated Avatar", value = user.is_avatar_animated())

    embed.add_field(name = "Mention", value = user.mention)

    embed.add_field(name = "Joined Discord", value = user.created_at.strftime('%b %d, %Y'))

    embed.add_field(name = "Joined Server", value = user.joined_at.strftime('%b %d, %Y'))

    embed.add_field(name = "Highest Role", value = f"{user.top_role.mention}\nHex: {user.color}")

    embed.add_field(name = "Online Status", value = getStatus(user.status))

    embed.add_field(name = "ID", value = user.id)

    embed.add_field(name = "Bot", value = user.bot)

    embed.set_image(url = user.avatar_url)

    embed.set_author(name = " | User", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(UserInformation(bot))
