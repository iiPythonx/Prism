# Modules
import ast
import discord

from assets.prism import Tools
from discord.ext import commands

# Main Command Classs
class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Evaluates math equations"
        self.usage = "math [equation]"

        self.not_allowed = [
            "ctx", "message", "print", "eval",
            "await", "import", "bot"
        ]

    def insert_returns(self, body):

        if isinstance(body[-1], ast.Expr):
            body[-1] = ast.Return(body[-1].value)
            ast.fix_missing_locations(body[-1])

    @commands.command()
    async def math(self, ctx, *, equation = None):

        # Check for equation
        if not equation:
            return await ctx.send(embed = Tools.error("No equation specified."))

        # Special formatting
        equation = equation.replace(" ", "")

        equation = equation.replace("9+10", "21")
        equation = equation.replace("^", "**")
        equation = equation.replace("%", "/100")

        # Check for cheeky hackers
        for expr in self.not_allowed:
            if expr in equation:
                return await ctx.send(embed = Tools.error("The specified expression is invalid."))

        if equation.count("**") > 2:
            return await ctx.send(embed = Tools.error("The specified equation would take too long to evaluate."))

        # Evaluate
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

        except Exception:
            return await ctx.send(embed = Tools.error("Specified expression is invalid."))

        # Embed construction
        embed = discord.Embed(title = str(result), color = 0x126bf1)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        try:
            return await ctx.send(embed = embed)

        except Exception as err:
            print(type(err))
            return await ctx.send(embed = Tools.error("Specified expression is too long."))

# Link to bot
def setup(bot):
    bot.add_cog(Math(bot))
