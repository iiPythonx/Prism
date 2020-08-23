# Modules
import ast
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Math(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.desc = "Does math for you"
    self.usage = "math [equation]"

    self.not_allowed = [
      "ctx",
      "message",
      "print",
      "eval",
      "await",
      "import",
      "bot"
    ]

  def insert_returns(self, body):

    if isinstance(body[-1], ast.Expr):

      body[-1] = ast.Return(body[-1].value)

      ast.fix_missing_locations(body[-1])

  @commands.command()
  async def math(self, ctx, *, equation: str = None):

    if not equation:
      
      return await ctx.send(embed = Tools.error("No equation specified."))

    equation = equation.replace("9 + 10", "21")

    equation = equation.replace("9+10", "21")

    equation = equation.replace("^", "**")

    equation = equation.replace("%", " / 100")

    for expr in self.not_allowed:

      if expr in equation:

        return await ctx.send(embed = Tools.error("Specified expression is invalid."))

    if equation.count("^") > 3 or equation.count("999") > 2:

      return await ctx.send(embed = Tools.error("Specified expression is too long."))

    try:

      fn_name = "_eval_expr"

      equation = equation.strip("`")

      equation = "\n".join(f"    {i}" for i in equation.splitlines())

      body = f"async def {fn_name}():\n{equation}"

      parsed = ast.parse(body)
      
      body = parsed.body[0].body

      self.insert_returns(body)
      
      exec(compile(parsed, filename = "math", mode = "exec"))
      
      result = (await eval(f"{fn_name}()"))

    except:

      return await ctx.send(embed = Tools.error("Specified expression is invalid."))

    embed = discord.Embed(title = str(result), color = 0x126bf1)

    embed.set_author(name = " | Math", icon_url = self.bot.user.avatar_url)

    embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

    try:

      return await ctx.send(embed = embed)

    except:

      return await ctx.send(embed = Tools.error("Specified expression is too long."))

# Link to bot
def setup(bot):
  bot.add_cog(Math(bot))
