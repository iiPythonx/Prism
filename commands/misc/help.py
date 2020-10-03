# Modules
import discord
import inspect

import importlib
from os import listdir

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "The help command, listing commands and providing details."
    self.usage = "help [category/command]"

  def get_commands(self, category):

    commands = ""

    for command in listdir(f"commands/{category}"):

      if command != "__pycache__":

        commands = f"{commands}, {command[:-3]}"

    return f"``{commands[2:]}``"

  @commands.command(aliases = ["info", "commands", "cmds"])
  async def help(self, ctx, *, category = None):

    if not category:

      embed = discord.Embed(title = "The Prism Discord Bot", description = "The only discord bot you actually need.", url = "https://top.gg/bot/685550504276787200", color = 0x126bf1)

      embed.add_field(name = ":person_golfing:  Entertainment Commands  :person_golfing:", value = f"See commands with ``{ctx.prefix}help fun``", inline = False)

      embed.add_field(name = ":cat:  Pet Commands  :dog:", value = f"See commands with ``{ctx.prefix}help pets``", inline = False)

      embed.add_field(name = ":musical_note: Music Commands (beta) :musical_note:", value = f"See commands with ``{ctx.prefix}help music``", inline = False)

      embed.add_field(name = ":moneybag: Currency Commands :moneybag:", value = f"See commands with ``{ctx.prefix}help currency``", inline = False)

      embed.add_field(name = ":tools:  Moderation Commands  :tools:", value = f"See commands with ``{ctx.prefix}help mod``", inline = False)

      embed.add_field(name = ":newspaper:  Miscellaneous  Commands  :newspaper:", value = f"See commands with ``{ctx.prefix}help misc``", inline = False)

    elif category.lower() in ["fun", "entertain", "entertainment"]:
        
      embed = discord.Embed(title = ":person_golfing:  Entertainment Commands  :person_golfing:", description = "The most interesting and unique commands out there.", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands("entertainment"), inline = False)
    
    elif category.lower() == "misc":
        
      embed = discord.Embed(title = ":newspaper:  Miscellaneous  Commands  :newspaper:", description = "The commands that cannot be described.", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands("misc"), inline = False)
      
    elif category.lower() == "pets":
        
      embed = discord.Embed(title = ":cat:  Pet Commands  :dog:", description = "Time to go walk the dog, (digitally of course lmao).", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands("pets"), inline = False)

    elif category.lower() == "music":
        
      embed = discord.Embed(title = ":musical_note:  Music Commands  :musical_note:", description = "Is it just me, or did low quality audio arrive?", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands("music"), inline = False)

    elif category.lower() in ["currency", "economy"]:
        
      embed = discord.Embed(title = ":moneybag: Currency Commands :moneybag:", description = "Go get a job you little lazy man.", color = 0x126bf1)
    
      embed.add_field(name = "Commands", value = self.get_commands("currency"), inline = False)
    
    elif category.lower() in ["mod", "moderation"]:
        
      embed = discord.Embed(title = ":tools:  Moderation Commands  :tools:", description = "Somebody causing problems? Don't worry about it mate.", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands("moderation"), inline = False)
    
    else:

      command_path = None

      for folder in listdir("commands"):

        for file in listdir(f"commands/{folder}"):

          if file.endswith(".py") and file[:-3].lower() == category.lower():

            command_path = f"commands.{folder}.{file[:-3]}"

      if not command_path:

        return await ctx.send(embed = Tools.error("That command/category could not be found."))

      command = importlib.import_module(command_path)

      for class_ in inspect.getmembers(command, inspect.isclass):

        if class_[0].lower() == category.lower():

          called = class_[1](self.bot)

          embed = discord.Embed(title = class_[0] + " Command", description = f"{called.desc}\nUsage: {called.usage}", color = 0x126bf1)

    embed.set_author(name = " | Help", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)
          
# Link to bot
def setup(bot):
  bot.add_cog(Help(bot))
