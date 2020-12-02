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
    @commands.has_permissions(manage_messages = True)
    async def trigger(self, ctx, option: str = None, *, trigger: str = None):

        db = loads(open("db/guilds", "r").read())
        triggers = db[str(ctx.guild.id)]["data"]["triggers"]

        if not option:
            triggerlist, index = "", 1

            for trigger in triggers:
                triggerlist += f"(#{index}) `{trigger}`: {triggers[trigger]} \n"
                index += 1

            if not triggerlist:
                triggerlist = "No triggers to display."

            embed = discord.Embed(title = "Server Triggers", description = triggerlist, color = 0x126bf1)

        elif not trigger: return await ctx.send(embed = Tools.error("No trigger data specified."))
        elif "`" in trigger: return await ctx.send(embed = Tools.error("Triggers cannot contain the ` character."))
        else:

            if option in ["add", "create", "make"]:
                if not "|" in trigger or trigger.count("|") > 1:
                    return await ctx.send(embed = Tools.error("Invalid trigger specified, example: `hello|world`."))
                elif len(trigger) > 90:
                    return await ctx.send(embed = Tools.error("Triggers have a maximum length of 90 characters."))
                elif len(triggers) == 20:
                    return await ctx.send(embed = Tools.error("You can have a maximum of 20 triggers."))

                raw = trigger.split("|")

                name = raw[0]
                data = raw[1]

                if name in triggers: return await ctx.send(embed = Tools.error("That trigger already exists."))

                elif name.startswith(" ") or name.endswith(" "): return await ctx.send(embed = Tools.error("Trigger names cannot start or end with a space."))

                triggers[name] = data
                embed = discord.Embed(title = f"Trigger #{len(triggers)} created.", color = 0x126bf1)

            elif option in ["remove", "delete"]:

                if trigger not in triggers:
                    return await ctx.send(embed = Tools.error("No such trigger exists."))

                triggers.pop(trigger)
                embed = discord.Embed(title = "Trigged deleted.", color = 0x126bf1)

            else:
                return await ctx.send(embed = Tools.error("Invalid (or unknown) option specified."))

        open("db/guilds", "w").write(dumps(db, indent = 4))

        embed.set_author(name = " | Triggers", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Trigger(bot))
