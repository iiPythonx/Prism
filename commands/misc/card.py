# Modules
import discord
from json import loads

from io import BytesIO
from requests import get

from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps

# Main Command Class
class Card(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "[EXPERIMENTAL] Generates a image based on your information"
        self.usage = "card"

    @commands.command()
    async def card(self, ctx):

        # Load user
        user = loads(open("db/users", "r").read())[str(ctx.author.id)]

        # Setup image
        image = Image.new("RGB", (3325, 1024), color = (18, 107, 241))

        def font(size, font = "Thin"):

            return ImageFont.truetype(font = f"assets/fonts/Roboto/{font}.ttf", size = size)

        # Profile image
        pfp = Image.open(BytesIO(get(ctx.author.avatar_url).content))
        pfp = pfp.resize((400, 400), Image.ANTIALIAS)

        try:

            image.paste(pfp, (10, 10), pfp)

        except ValueError:

            image.paste(pfp, (10, 10))

        # Drawing
        draw = ImageDraw.Draw(image)

        draw.text((450, 10), f"{ctx.author.name}#{ctx.author.discriminator}", font = font(200, "Regular"), fill = (255, 255, 255))

        draw.line((10, 425) + (3000, 425), fill = (255, 255, 255), width = 10)

        draw.text((450, 225), f"Level {user['data']['levels']['level']}", font = font(150), fill = (225, 225, 225))

        draw.text((10, 450), f"\"{user['data']['bio']}\"", font = font(125), fill = (255, 255, 255))

        # Package the image
        imgByteArr = BytesIO()

        image.save(imgByteArr, format = "PNG")

        imgByteArr.seek(0)
            
        # Send the image
        return await ctx.send(file = discord.File(imgByteArr, "card.png"))

# Link to bot
def setup(bot):
    bot.add_cog(Card(bot))
