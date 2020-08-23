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
  async def stats(self, ctx, *, etc: str = None):

    orig_time = time.time()

    command_count = 0

    for folder in os.listdir("commands"):

      for file in os.listdir(f"commands/{folder}"):

        if file != "__pycache__":

          command_count += 1

    bot = f"""
      Server Count: {len(self.bot.guilds)}
      User Count: {len(self.bot.users)}
      Command Count: {command_count}
      Bot Latency: {str(time.time() - orig_time).split(".")[1][:2]}ms
      Staff Member(s):
        - <@633185043774177280> (Developer)
        - <@666839157502378014> (Management)
    """

    other = f"""
      Python Version: {str(sys.version).split(" ")[0]}
      Discord.py Version: {discord.__version__}
      API Latency: {round(self.bot.latency * 1000)}ms

      Last updated: {str(datetime.now()).split(" ")[0]}
    """

    embed = discord.Embed(color = 0x126bf1)

    embed.add_field(name = "Bot Information", value = bot, inline = False)

    if etc and etc.lower() == "all":

      percore_usage = ""

      for i, percentage in enumerate(psutil.cpu_percent(percpu = True, interval = 1)):

        percore_usage = f"{percore_usage}Core {i + 1}: {percentage}%\n"

      svmem = psutil.virtual_memory()

      cpufreq = psutil.cpu_freq()

      boot_time_timestamp = psutil.boot_time()

      bt = datetime.fromtimestamp(boot_time_timestamp)

      uname = platform.uname()

      system = f"""
        System: {uname.system}
        Node Name: {uname.node}
        Release: {uname.release}
        Version: {uname.version}
        Machine: {uname.machine}
        Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}
      """

      processor = f"""
        Physical Cores: {psutil.cpu_count(logical = False)}
        Total Cores: {psutil.cpu_count(logical = True)}
        Current Frequency: {cpufreq.current:.2f}Mhz

        CPU Usage (per core):
        {percore_usage}
        Total CPU Usage: {psutil.cpu_percent()}%
      """

      memory = f"""
        Total: {self.scale_size(svmem.total)}
        Available: {self.scale_size(svmem.available)}
        Used: {self.scale_size(svmem.used)}
        Percentage: {svmem.percent}%
      """

      embed.add_field(name = "System Information", value = system, inline = False)

      embed.add_field(name = "Processor Information", value = processor, inline = False)

      embed.add_field(name = "Memory Information", value = memory, inline = False)

    embed.add_field(name = "Other Information", value = other, inline = False)

    embed.set_author(name = " | Statistics", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
  bot.add_cog(Stats(bot))
