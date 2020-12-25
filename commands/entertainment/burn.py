# Modules
import discord
from PIL import Image

from assets.prism import Tools
from discord.ext import commands

from assets.images import imagefromURL, compile

# Main Command Class
class Burn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Spongebob would like to burn you now please"
        self.usage = "burn [user]"

    @commands.command()
    async def burn(self, ctx, user: discord.User = None):

        user = await Tools.getClosestUser(ctx, user if user else ctx.author)

        # Image initialization
        data = imagefromURL(user.avatar_url).resize((224, 259))
        im = Image.open("assets/images/spongebob_burn.png")
        cnv = Image.new(mode = "RGB", color = (0, 0, 0), size = im.size)

        # Rendering
        cnv.paste(data, (29, 58))
        cnv.paste(im, (0, 0), im)

        # Send the image
        return await ctx.send(file = discord.File(compile(cnv), "burn.png"))

# Link to bot
def setup(bot):
    bot.add_cog(Burn(bot))
