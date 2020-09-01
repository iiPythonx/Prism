# Modules
import os
import sys

import time
import psutil

import discord
import platform

from datetime import datetime
from discord.ext import commands

# Constants
uptime_start = datetime.now()

# Main Command Class
class Stats(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Check out Prism's statistics"
    self.usage = "stats"

  def scale_size(self, bytes, suffix = "B"):

    factor = 1024

    for unit in ["", "K", "M", "G", "T", "P"]:

      if bytes < factor:

        return f"{bytes:.2f}{unit}{suffix}"

      bytes /= factor

  @commands.command(aliases = ["statistics", "bot"])
  async def stats(self, ctx):

    percore_usage = ""

    for i, percentage in enumerate(psutil.cpu_percent(percpu = True, interval = 1)):

      percore_usage = f"{percore_usage}\tCore #{i + 1}: {percentage}%\n"

    bt = datetime.fromtimestamp(psutil.boot_time()).strftime("%D %I:%M %p")

    uname = platform.uname()

    svmem = psutil.virtual_memory()

    cpufreq = psutil.cpu_freq()

    embed = discord.Embed(title = "Prism Statistics", color = 0x126bf1)

    embed.add_field(
      name = "Bot Information",
      value = f"""```
        Guild Count: {len(self.bot.guilds)}
        Member Count: {len(self.bot.users)}
        Command Count: {len(self.bot.commands)}

        Latency: {round(self.bot.latency * 1000)}ms

        Staff Member(s):
          - iiPython#0768 (Developer)
          - Commuter#4083 (Management)```
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
        Physical: {psutil.cpu_count(logical = False)} | Total: {psutil.cpu_count(logical = True)}
        Frequency: {cpufreq.current:.2f}Mhz

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
        Python Version: {str(sys.version).split(" ")[0]}
        Discord.py Version: {discord.__version__}

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
