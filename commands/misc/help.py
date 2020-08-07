# Prism Rewrite - Basic Command

# Modules
import os
import json

import discord
import inspect

import importlib
from assets.prism import Tools

from discord.ext import commands

# Variables
nsfw_commands = [
  "dictionary", "gay", "lesbian", "pp", "slap"
]

# Main Command Class
class Help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Prism's help command, making life easy"
    self.usage = "help [category]"

  def get_commands(self, ctx, category):

    db = json.loads(open("db/guilds", "r").read())

    commands = ""

    for command in os.listdir(f"commands/{category}"):

      if command != "__pycache__":

        if not "nsfw-enabled" in db[str(ctx.guild.id)]["tags"]:

          if command[:-3] in nsfw_commands:

            pass

          else:

            commands = f"{commands}, {command[:-3]}"

        else:
                
          commands = f"{commands}, {command[:-3]}"

    return f"``{commands[2:]}``"

  async def embed(self, ctx, cat, prefix, commandClass = None):

    embed = None

    if cat == "default":

      embed = discord.Embed(title = "The Prism Discord Bot", description = "The only discord bot you actually need.", url = "https://top.gg/bot/685550504276787200", color = 0x126bf1)

      embed.add_field(name = ":person_golfing:  Entertainment Commands  :person_golfing:", value = f"See commands with ``{prefix}help entertain``", inline = False)

      embed.add_field(name = ":cat:  Pet Commands  :dog:", value = f"See commands with ``{prefix}help pets``", inline = False)

      embed.add_field(name = ":moneybag: Currency Commands :moneybag:", value = f"See commands with ``{prefix}help currency``", inline = False)

      embed.add_field(name = ":tools:  Moderation Commands  :tools:", value = f"See commands with ``{prefix}help mod``", inline = False)

      embed.add_field(name = ":newspaper:  Miscellaneous  Commands  :newspaper:", value = f"See commands with ``{prefix}help misc``", inline = False)

    elif cat == "entertainment":

      embed = discord.Embed(title = ":person_golfing:  Entertainment Commands  :person_golfing:", description = "The most interesting and unique commands out there.", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands(ctx, cat), inline = False)

    elif cat == "misc":

      embed = discord.Embed(title = ":newspaper:  Miscellaneous  Commands  :newspaper:", description = "The commands that cannot be described.", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands(ctx, cat), inline = False)

    elif cat == "pets":

      embed = discord.Embed(title = ":cat:  Pet Commands  :dog:", description = "Time to go walk the dog, (digitally of course lmao).", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands(ctx, cat), inline = False)

    elif cat == "currency":

      embed = discord.Embed(title = ":moneybag: Currency Commands :moneybag:", description = "Go get a job you little lazy man.", color = 0x126bf1)
    
      embed.add_field(name = "Commands", value = self.get_commands(ctx, cat), inline = False)

    elif cat == "moderation":

      embed = discord.Embed(title = ":tools:  Moderation Commands  :tools:", description = "Somebody causing problems? Don't worry about it mate.", color = 0x126bf1)

      embed.add_field(name = "Commands", value = self.get_commands(ctx, cat), inline = False)

    else:

      embed = discord.Embed(title = f"{cat} Command", description = f"{commandClass.desc}; usage: {commandClass.usage}", color = 0x126bf1)

      embed.set_author(name = " | Help", icon_url = self.bot.user.avatar_url)

      embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)
      
    return embed

  @commands.command(aliases = ["info", "commands", "cmds"])
  async def help(self, ctx, *, category = None):
        
    db = json.loads(open("db/guilds", "r").read())

    prefix = db[str(ctx.guild.id)]["prefix"]

    if not category:

      return await ctx.send(embed = await self.embed(ctx, "default", prefix))

    elif category.lower() in ["fun", "entertain", "entertainment"]:
        
      return await ctx.send(embed = await self.embed(ctx, "entertainment", prefix))
    
    elif category.lower() == "misc":
        
      return await ctx.send(embed = await self.embed(ctx, "misc", prefix))
      
    elif category.lower() == "pets":
        
      return await ctx.send(embed = await self.embed(ctx, "pets", prefix))
    
    elif category.lower() in ["currency", "economy"]:
        
      return await ctx.send(embed = await self.embed(ctx, "currency", prefix))
    
    elif category.lower() in ["mod", "moderation"]:
        
      return await ctx.send(embed = await self.embed(ctx, "moderation", prefix))
    
    else:

      for command_folder in os.listdir("commands"):

        for command in os.listdir(f"commands/{command_folder}"):
            
          if f"{category.lower()}.py" == command:
            
            command_module = importlib.import_module(f"commands.{command_folder}.{command[:-3]}")

            for name, obj in inspect.getmembers(command_module):
                    
              if inspect.isclass(obj):
                        
                try:

                  commandClass = obj(self.bot)
      
                except:

                  return await ctx.send(embed = Tools.error("Yea, that command randomly doesn't want to work today. (we are investigating it)"))

                return await ctx.send(embed = await self.embed(ctx, Tools.uppercase(category), prefix, commandClass))

      return await ctx.send(embed = await self.embed(ctx, "default", prefix))
          
# Link to bot
def setup(bot):
    bot.add_cog(Help(bot))
