# Modules
import discord
from random import choice

from discord.ext import commands

# Main Command Class
class Ketchup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Some nice, slurpy, tasty ketchup"
        self.usage = "ketchup"
        
        self.images = [
            "https://images-na.ssl-images-amazon.com/images/I/71i0PnRw6EL._SL1500_.jpg",
            "https://cdn.shopify.com/s/files/1/2364/6329/products/2019_PK_Ketchup_Shopify_600x.jpg?v=1571608882",
            "https://images-na.ssl-images-amazon.com/images/I/8199Xb1cVdL._SL1500_.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR3Tg_70GvbraVTinYoWxYACbvlA5ULiK5D7urt6hSNVlwo-plA",
            "https://cdnimg.webstaurantstore.com/images/products/large/166705/271501.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSb4nPCyZoz6qIIju4Mjh4R__hs9RCLuf2ztdpahgfpf2WFRgO-",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRjyJ3-s_hkx1ddeMcH-G8nqe5b02a979VyFEXfNo7VkQwBTQ7B",
            "https://cdn.shopify.com/s/files/1/1376/4649/products/no-added-sugar-organic-ketchup_1024x1024.jpg?v=1525969786",
            "https://i2.wp.com/www.thepetitecook.com/wp-content/uploads/2015/08/ketchup-the-petite-cook.jpg?fit=700%2C467&ssl=1",
            "https://images.freshop.com/00013000001243/e86a3a30c651ad96390af06a26cfd6d8_large.png",
            "https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/06/768x384/landscape-1486400207-index-ketchup.jpg?resize=480:*",
            "https://thumbs-prod.si-cdn.com/utxQux55RAFtzULHh44boHRZY2g=/fit-in/1600x0/https://public-media.si-cdn.com/filer/3e/36/3e365ebe-49a1-48d6-a32a-09822b5da2b1/file-20180722-142438-k7576v.jpg",
            "https://www.rd.com/wp-content/uploads/2017/08/01-Heres-The-Difference-Between-Fancy-Ketchup-and-Regular-Ketchup_643992628-Africa-Studio-1024x683.jpg"
        ]

    @commands.command(aliases = ["katsup", "catsup"])
    async def ketchup(self, ctx):

        embed = discord.Embed(color = 0x126bf1)
        
        embed.set_image(url = choice(self.images))
        
        embed.set_author(name = " | Ketchup", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Ketchup(bot))
