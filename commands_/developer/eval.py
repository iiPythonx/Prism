# Modules
import ast
import discord

from datetime import datetime
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

  def _eval_(self, ctx, output, start):

    if not output:

      output = "[no output]"

    # fetch the time taken
    time = round((datetime.now() - start).total_seconds() * 1000)
    timeframe = "ms"

    if time > 1000:

      timeframe = " seconds"
      time = round(time / 1000, 1)

      if time > 60:

        timeframe = " minutes"
        time = round(time / 60, 1)

    embed = discord.Embed(title = f"Evaluated in {time}{timeframe}.", description = f"```py\n{output}\n```", color = 0x126bf1)

    embed.set_author(name = " | Evaluation", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    return embed

  @commands.command(name = "eval")
  @commands.is_owner()
  async def _eval(self, ctx, *, cmd: str = None):
    
    if not cmd:
      
      return await ctx.send(embed = Tools.error("No code provided."))

    if cmd[3:].startswith("py") or cmd[3:].startswith("python"):

      cmd = cmd[5:]

      if cmd.startswith("thon"):

        cmd = cmd[4:]

    env = {
      "bot": ctx.bot,
      "discord": discord,
      "commands": commands,
      "ctx": ctx,
      "Tools": Tools,
    }

    fn_name = "_eval_expr"

    cmd = cmd.strip("` ")

    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    body = f"async def {fn_name}():\n{cmd}"

    start = datetime.now()

    try:

      parsed = ast.parse(body)
      
      body = parsed.body[0].body

      self.insert_returns(body)

      exec(compile(parsed, filename = "<ast>", mode = "exec"), env)
      
      result = (await eval(f"{fn_name}()", env))

      return await ctx.send(embed = self._eval_(ctx, result, start))

    except Exception as e:

      return await ctx.send(embed = self._eval_(ctx, e, start))

# Link to bot
def setup(bot):
    bot.add_cog(Eval(bot))
