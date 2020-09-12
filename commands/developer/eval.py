# Prism Rewrite - Basic Command

# Modules
import os
import ast

import string
import random

import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Eval(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Evaluates Python code"
    self.usage = "eval [code]"

  def insert_returns(self, body):

    if isinstance(body[-1], ast.Expr):

      body[-1] = ast.Return(body[-1].value)

      ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):

      self.insert_returns(body[-1].body)

      self.insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        
      self.insert_returns(body[-1].body)

  def _eval_(self, output, user, lang = "py"):

    description = f"```{lang}\n{output}\n```"

    embed = discord.Embed(title = f"Evaluated in {round(self.bot.latency * 1000)}ms.", description = description, color = 0x126bf1)

    embed.set_author(name = " | Evaluation", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {user.name}.", icon_url = user.avatar_url)

    return embed

  def _js_exec(self, code):

      open("assets/temp/jscode.js", "w+").write(code)

      os.system("node assets/temp/jscode.js > assets/temp/jsoutput 2>&1")

      output = open("assets/temp/jsoutput", "r").read()

      os.remove("assets/temp/jscode.js")

      os.remove("assets/temp/jsoutput")

      return output

  @commands.command(name = "eval")
  @commands.is_owner()
  async def _eval(self, ctx, *, cmd: str = None):
    
    if not cmd:
      
      return await ctx.send(embed = Tools.error("No code provided."))

    print(f"Eval used by {ctx.author}:")

    print(f"  {cmd}")

    if cmd[3:].startswith("py") or cmd[3:].startswith("python"):

      cmd = cmd[5:]

      if cmd.startswith("thon"):

        cmd = cmd[4:]

    elif cmd[3:].startswith("js") or cmd[3:].startswith("javascript"):

      cmd = cmd[5:]

      cmd = cmd[:-3]

      lines = cmd.split("\n")

      cmd = ""

      for line in lines[1:]:

        cmd = f"{cmd}{line}\n"   

      output = self._js_exec(cmd)

      lines = output.split("\n")

      lines_compiled = ""

      for line in lines:

        lines_compiled = f"{lines_compiled}{line}\n"

      output = lines_compiled.split("    at ")[0]

      return await ctx.send(embed = self._eval_(output, ctx.author, "js"))

    class prism:

      def generateToken(author):

        token = ""

        upper = string.ascii_uppercase

        lower = string.ascii_lowercase

        for char in str(author.id):

          if random.randint(0, 1):

            token += upper[int(char)]

          else:

            token += lower[int(char)]

        c = 1

        while c != random.randint(50, 75):

          if random.randint(0, 1):

            token = token + random.choice(upper)
          
          else:

            token = token + random.choice(lower)

          c += 1

        return token

    env = {
        "bot": ctx.bot,
        "discord": discord,
        "commands": commands,
        "ctx": ctx,
        "__import__": __import__,
        "Tools": Tools,
        "os": os,
        "prism": prism
    }

    fn_name = "_eval_expr"

    cmd = cmd.strip("` ")

    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    body = f"async def {fn_name}():\n{cmd}"

    try:

      parsed = ast.parse(body)
      
      body = parsed.body[0].body

      self.insert_returns(body)

      exec(compile(parsed, filename = "<ast>", mode = "exec"), env)
      
      result = (await eval(f"{fn_name}()", env))

      if isinstance(result, discord.message.Message):

        result = result.content

      return await ctx.send(embed = self._eval_(result, ctx.author))

    except Exception as e:

      return await ctx.send(embed = self._eval_(e, ctx.author))

# Link to bot
def setup(bot):
    bot.add_cog(Eval(bot))
