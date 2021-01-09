# Modules
import discord
from random import choice

from discord.ext import commands

# Main Command Class
class Sun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Gets you a random picture of the sun"
        self.usage = "sun"

        self.images = [
            "https://www.universetoday.com/wp-content/uploads/2014/09/sun1.jpg",
            "https://apod.nasa.gov/apod/image/1907/SpotlessSunIss_Colacurcio_2048.jpg",
            "https://resize.hswstatic.com/u_0/w_480/gif/sun-update-1.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/220px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg",
            "https://cdn.arstechnica.net/wp-content/uploads/2020/03/nasa_386_SunEmitsSolsticeFlare1200w-800x480.jpg",
            "https://geographical.co.uk/media/k2/items/cache/8e4e30c8fc08507de1b0b5afc7d32a85_XL.jpg",
            "https://astronomy.com/-/media/Images/News%20and%20Observing/News/2018/11/thesun.jpg?mw=600",
            "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/sweap-thumb-1575482781.png",
            "https://riversideparknyc.org/wp-content/uploads/2016/04/sun.jpg",
            "https://cdn.mos.cms.futurecdn.net/YhZo9RHnU6uvcFbwWsp62e-320-80.jpg",
            "https://epsilon.aeon.co/images/5c35ee6d-c055-4208-8681-499b50acc7a0/idea_sized-sun-gettyimages-1036397974.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR6VZjIymNQoOkv3F0Uz9v9c0RFL0o76UGeep4XzGlfYMmPQs4H",
            "https://www.extremetech.com/wp-content/uploads/2019/05/SolarPlasmaInteractions.jpg"
        ]

    @commands.command()
    async def sun(self, ctx):

        embed = discord.Embed(color = 0x126bf1)
        embed.set_image(url = choice(self.images))
        embed.set_author(name = " | Sun", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Sun(bot))
