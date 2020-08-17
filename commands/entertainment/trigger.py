# Prism Rewrite - Basic Command

# Modules
import discord
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Trigger(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Text triggers for your server"
        self.usage = "trigger [option] [trigger]"

    @commands.command(aliases = ["triggers"])
    async def trigger(self, ctx, option: str = None, *, trigger: str = None):

        db = loads(open("db/guilds", "r").read())

        _db = db[str(ctx.guild.id)]

        if not option and not trigger:

            triggers = ""

            for trigger in _db["data"]["triggers"]:

                triggers += f"`{trigger}`: {_db['data']['triggers'][trigger]}\n"

            if not triggers:

                triggers = "No triggers on this server."

            embed = discord.Embed(title = "Server Triggers", description = triggers, color = 0x126bf1)

            embed.set_author(name = " | Triggers", icon_url = self.bot.user.avatar_url)

            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

            return await ctx.send(embed = embed)

        elif not trigger:

            return await ctx.send(embed = Tools.error("No option specified; valid options are `add`, and `delete`."))

        elif option.lower() == "add":

            if not "|" in trigger:

                return await ctx.send(embed = Tools.error("Invalid trigger; `example: haha|no laughing!`."))

            data = trigger.split("|")

            trigger = data[0]

            response = data[1]

            if not response:

                return await ctx.send(embed = Tools.error("Invalid trigger; `example: haha|no laughing!`."))

            _db["data"]["triggers"][trigger] = response

            embed = discord.Embed(title = f"Trigger #{len(_db['data']['triggers'])} saved.", color = 0x126bf1)

        elif option.lower() == "delete":

            if not trigger in _db["data"]["triggers"]:

                return await ctx.send(embed = Tools.error("No such trigger exists."))

            _db["data"]["triggers"].pop(trigger)

            embed = discord.Embed(title = f"Trigger deleted.", color = 0x126bf1)

        else:

            embed = discord.Embed(title = "Invalid option.", description = "Valid options are `add`, and `delete`.", color = 0x126bf1)

        embed.set_author(name = " | Triggers", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        open("db/guilds", "w").write(dumps(db, indent = 4))

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Trigger(bot))
