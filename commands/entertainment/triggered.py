# Modules
import discord
from PIL import Image

from random import randint
from assets.prism import Tools

from discord.ext import commands
from assets.images import imagefromURL, compileGIF

# Main Command Class
class Triggered(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "They be lookin' kinda triggered"
        self.usage = "triggered [user]"

    @commands.command()
    async def triggered(self, ctx, user: discord.User = None):

        user = await Tools.getClosestUser(ctx, user if user else ctx.author)

        # Image initialization
        image = imagefromURL(user.avatar_url).resize((216, 216), Image.ANTIALIAS)

        text = Image.open("assets/images/triggered.jpg")

        # Animating
        canvas = Image.new(mode = "RGB", size = image.size, color = (0, 0, 0))

        images, num = [], 0

        while num < 100:

            canvas.paste(image, (randint(-4, 4), randint(-4, 4)))

            images.append(canvas)

            canvas.paste(text, (randint(-4, 4), (216 - 39) + (randint(-4, 4))))

            canvas = Image.new(mode = "RGB", size = image.size, color = (0, 0, 0))

            num += 5

        # Compiling to GIF
        data = compileGIF(images, 3)

        # Send the image
        return await ctx.send(file = discord.File(data, "triggered.gif"))

# Link to bot
def setup(bot):
    bot.add_cog(Triggered(bot))
