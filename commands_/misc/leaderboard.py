# Modules
import discord
from json import loads

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Leaderboard(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Check the public leaderboard"
    self.usage = "leaderboard"

  def ToWord(self, number):

    if number == 1:

      return "first"

    elif number == 2:

      return "second"
    
    else:

      return "third"

  @commands.command(aliases = ["lb", "champions"])
  async def leaderboard(self, ctx, page_number: int = 1):

    db = loads(open("db/users", "r").read())

    pages = {
      "1": {
        "count": 0,
        "members": {}
      }
    }

    current_page = 1

    for user in ctx.guild.members:

      if str(user.id) in db:

        page = pages[str(current_page)]

        if not page["count"] == 5:

          page["count"] += 1

          page["members"][str(user.id)] = db[str(user.id)]["data"]["levels"]["level"]

        else:

          current_page += 1

          pages[str(current_page)] = {
            "count": 1,
            "members": {
              str(user.id): db[str(user.id)]["data"]["levels"]["level"]
            }
          }

    if not str(page_number) in pages:

      return await ctx.send(embed = Tools.error("That page doesn't exist."))

    _sorted = sorted(pages[str(page_number)]["members"].items(), key = lambda x: x[1], reverse = True)

    users, c = "", 1

    for i in _sorted:

      user = self.bot.get_user(int(i[0]))

      bal = db[str(user.id)]["balance"]

      if len(str(bal)) > 10:

        bal = "∞"

      line = f"{user.name} - Level {i[1]} ({bal} coins)"

      medal = ""

      if c < 4 and page_number == 1:

        medal = f":{self.ToWord(c)}_place: "

      users += f"{medal}{line}\n"

      c += 1

    embed = discord.Embed(description = f"This is page {page_number} / {len(pages)}.\n\n{users}", color = 0x126bf1)

    embed.set_author(name = " | Leaderboard", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Leaderboard(bot))
