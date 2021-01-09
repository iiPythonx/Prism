# Modules
import discord
from json import loads

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Displays someones Prism profile"
        self.usage = "profile [user]"

    @commands.command(aliases = ["account"])
    async def profile(self, ctx, user = None):

        db = loads(open("db/users", "r").read())
        user = await Tools.getClosestUser(ctx, user if user else ctx.author)

        if not str(user.id) in db:
            return await ctx.send(embed = Tools.error(f"{user.name} does not have a profile."))

        # Collect our data
        data = db[str(user.id)]

        favorite_command = sorted(data["data"]["commands"]["used"].items(), key = lambda x: x[1], reverse = True)[0]
        favorite_command = f"{Tools.uppercase(favorite_command[0])} ({favorite_command[1]} times)"

        # Embed construction
        embed = discord.Embed(title = str(user), color = 0x126bf1)

        # Balance
        balance = data["balance"]
        balance = f"{balance:,}"

        if data["balance"] > 1000000000:
            balance = "1,000,000,000+"

        embed.add_field(name = ":coin: Balance", value = balance)
        embed.add_field(name = ":octagonal_sign: Blacklisted", value = str("blacklisted" in data["data"]["tags"]))

        if data["data"]["bio"] is not None:
            embed.add_field(name = ":pencil: Biography", value = data["data"]["bio"], inline = False)

        embed.set_author(name = " | Profile", icon_url = user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Profile(bot))
