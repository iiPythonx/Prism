# Modules
import discord
from json import loads

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Shop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Check all the latest swag"
        self.usage = "shop"

    @commands.command(aliases = ["market"])
    async def shop(self, ctx):
        
        db = loads(open("db/guilds", "r").read())

        user = loads(open("db/users", "r").read())[str(ctx.author.id)]
        
        items = loads(open("assets/res/items.json", "r").read())

        categories = {}

        for item in items:

            if not items[item]["cat"] in categories:

                categories[items[item]["cat"]] = {}

            categories[items[item]["cat"]][item] = items[item]

        prefix = db[str(ctx.guild.id)]["prefix"]
        
        embed = discord.Embed(description = f"Some of the world's most useful items.\nUse ``{prefix}buy [item id]`` to purchase an item.\nFor example, ``{prefix}buy 1`` would buy a Pizza Slice.", color = 0x126bf1)

        for category in categories:

            text = ""

            for item in categories[category]:

                _item = categories[category][item]

                if not "premium" in _item["tags"] or "premium" in _item["tags"] and "premium" in user["data"]["tags"]:

                    text += f"[{item}] {_item['name']} ({_item['price']} coins) \n"

            embed.add_field(name = Tools.uppercase(category), value = text, inline = False)

        embed.set_author(name = " | Item Shop", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)
        
# Link to bot
def setup(bot):
    bot.add_cog(Shop(bot))
