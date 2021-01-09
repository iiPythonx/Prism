# Modules
import discord
from datetime import date

from discord import Embed
from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Settings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Changes server settings for Prism"
        self.usage = "settings [key] [value]"
        
    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def settings(self, ctx, key: str = None, value = None):

        db = loads(open("db/guilds", "r").read())

        _db = db[str(ctx.guild.id)]

        if not key:

            prefix = _db["prefix"]
            nsfw = True if "nsfw-enabled" in _db["tags"] else False
            levels = True if "levels-enabled" in _db["tags"] else False

            joinleave = self.bot.get_channel(_db["data"]["joinleave_channel"]).name if _db["data"]["joinleave_channel"] else "Not setup"

            if _db["data"]["autorole"]:

                autorole = discord.utils.get(ctx.guild.roles, id = _db["data"]["autorole"])

                if not autorole:

                    autorole = "Not setup"

                    _db["data"]["autorole"] = None

                    open("db/guilds", "w").write(dumps(db, indent = 4))

                else:

                    autorole = "@" + autorole.name

            else:

                autorole = "Not setup"

            embed = Embed(title = "Server Settings", description = f"Last updated: {_db['data']['last_updated']}", color = 0x126bf1)
        
            embed.add_field(name = "Settings­", value = f"Prefix: {prefix}\nNSFW Enabled: {nsfw}\nLevels Enabled: {levels}\nJoin/Leave Channel: #{joinleave}\nAutorole: {autorole}", inline = False)

            embed.add_field(name = "How to change these", value = f"To change a setting, use ``{prefix}settings [setting] [value]``.\nFor example: ``{prefix}settings nsfw off``.", inline = False)

            embed.set_author(name = " | Settings", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
            
            return await ctx.send(embed = embed)

        elif key and not value:
            
            return await ctx.send(embed = Tools.error("No value specified."))

        key = key.lower()

        if not key in ["prefix", "nsfw", "levels", "joinleave", "autorole"]:

            return await ctx.send(embed = Tools.error("That isn't a valid setting."))

        elif not isinstance(value, str) and not isinstance(value, bool):

            return await ctx.send(embed = Tools.error("That isn't a valid value."))

        elif value.lower() in ["on", "enable", "true", "yes"]:

            value = True

        elif value.lower() in ["off", "disable", "false", "no"]:

            value = False

        else:

            if key != "prefix" and not isinstance(value, str) and not isinstance(value, bool):

                return await ctx.send(embed = Tools.error("That isn't a valid value."))

        if key == "prefix":

            for char in ["`", "\\"]:

                if char in value:

                    return await ctx.send(embed = Tools.error("Prefix contains unsupported characters."))

            if len(value) > 10:

                return await ctx.send(embed = Tools.error("Prefixes cannot be longer than 10 characters."))

            _db["prefix"] = value

            text = f"The prefix in this server has been set to ``{value}``."

        elif key == "nsfw":

            if value:

                if not "nsfw-enabled" in _db["tags"]:

                    _db["tags"].append("nsfw-enabled")

            else:

                if "nsfw-enabled" in _db["tags"]:

                    _db["tags"].remove("nsfw-enabled")
  
            text = f"NSFW has been set to ``{value}``."

        elif key == "levels":

            if value:

                if not "levels-enabled" in _db["tags"]:

                    _db["tags"].append("levels-enabled")

            else:

                if "levels-enabled" in _db["tags"]:

                    _db["tags"].remove("levels-enabled")
  
            text = f"Leveling has been set to ``{value}``."

        elif key == "joinleave":

            if not isinstance(value, str):

                return await ctx.send(embed = Tools.error("That isn't a valid value."))

            try:

                id = int(value)

            except:

                try:

                    id = int(value.split("<#")[1].split(">")[0])

                except:

                    return await ctx.send(embed = Tools.error("That isn't a valid value."))

            channel = self.bot.get_channel(id)

            if not channel:

                return await ctx.send(embed = Tools.error("That isn't a valid channel ID."))

            _db["data"]["joinleave_channel"] = channel.id

            text = f"The join/leave channel has been set to #{channel.name}"

        elif key == "autorole":

            if value.lower() in ["remove", "reset"]:

                _db["data"]["autorole"] = None

                text = "The autorole for this server has been reset."

            else:

                if value.startswith("<@&") and value.endswith(">"):

                    value = value.replace("<", "").replace(">", "").replace("@", "").replace("&", "")

                else:

                    if value.startswith("@"):

                        value = value[1:]

                    role = discord.utils.get(ctx.guild.roles, name = value)

                    if not role:

                        return await ctx.send(embed = Tools.error("Couldn't find that role; check your capitalization. You can't use IDs here."))

                    value = role.id

                role = discord.utils.get(ctx.guild.roles, id = int(value))

                _db["data"]["autorole"] = role.id

                text = "This server's autorole has been set to @" + role.name

        _db["data"]["last_updated"] = str(date.today())

        open("db/guilds", "w").write(dumps(db, indent = 4))

        embed = Embed(title = text, color = 0x126bf1)
    
        embed.set_author(name = " | Settings", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Set by {ctx.author}.", icon_url = ctx.author.avatar_url)
        
        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Settings(bot))
