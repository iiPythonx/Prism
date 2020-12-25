# Modules
import os
import sys

import time
import psutil

import discord
import platform

from datetime import datetime
from discord.ext import commands

# Main Command Class
class Stats(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Check out Prism's statistics"
    self.usage = "stats"

    self.uptime_start = datetime.now()

  def scale_size(self, bytes, suffix = "B"):

    factor = 1024

    for unit in ["", "K", "M", "G", "T", "P"]:
      if bytes < factor:
        return f"{bytes:.2f}{unit}{suffix}"

      bytes /= factor

  @commands.command(aliases = ["statistics", "bot"])
  async def stats(self, ctx):

    # Locate our usage per core
    percore_usage = ""
    for i, percentage in enumerate(psutil.cpu_percent(percpu = True, interval = 1)):
      percore_usage += f"{percentage}% "

    # Load lots of information
    bt = datetime.fromtimestamp(psutil.boot_time()).strftime("%D %I:%M %p")
    uname = platform.uname()
    svmem = psutil.virtual_memory()

    cpu = psutil.cpu_freq()

    # Create embed
    embed = discord.Embed(title = "Prism Statistics", color = 0x126bf1)

    embed.add_field(
      name = "Bot Information",
      value = f"""```
        Guild Count: {len(self.bot.guilds)}
        Command Count: {len(self.bot.commands)}

        Bot latency: {round(self.bot.latency * 1000)}ms```
      """.replace("  ", ""),
      inline = False
    )

    embed.add_field(
      name = "System Information",
      value = f"""```
        Running {uname.system} v{uname.version} ({uname.machine})
        Lastest Boot: {bt}```
      """.replace("  ", ""),
      inline = False
    )

    embed.add_field(
      name = "Processor Information",
      value = f"""```
        Physical cores: {psutil.cpu_count(logical = False)} | Total cores: {psutil.cpu_count(logical = True)}
        Maximum frequency: {round(cpu.max / 1000, 1)}GHz
        Current frequency: {round(cpu.current / 1000, 1)}GHz

        Core Usage:
        {percore_usage}

        CPU Usage: {psutil.cpu_percent()}%```
      """.replace("  ", ""),
      inline = False
    )

    embed.add_field(
      name = "RAM Information",
      value = f"""```
        Total: {self.scale_size(svmem.total)} | Free: {self.scale_size(svmem.available)}
        Used: {self.scale_size(svmem.used)} | Percentage: {svmem.percent}%```
      """.replace("  ", ""),
      inline = False
    )

    embed.add_field(
      name = "Other Information",
      value = f"""```
        Python version: {platform.python_version()}
        Library version: {discord.__version__}

        Time requested: {datetime.now().strftime("%D %I:%M:%S %p")} CST```
      """.replace("  ", ""),
      inline = False
    )

    embed.set_author(name = " | Statistics", icon_url = self.bot.user.avatar_url)
    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Stats(bot))
