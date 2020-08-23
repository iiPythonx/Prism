# Modules
import discord
from datetime import date

from json import loads, dumps

from assets.prism import Tools
from discord.ext import commands

# Main Command Class
class Adopt(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Adopt an absolutely adorable pet"
        self.usage = "adopt [pet name / ID]"

        self.pets = {
            "lizard": {
                "price": 200,
                "emoji": ":lizard:"
            },
            "snail": {
                "price": 200,
                "emoji": ":snail:"
            },
            "cat": {
                "price": 750,
                "emoji": ":cat:"
            },
            "dog": {
                "price": 750,
                "emoji": ":dog:"
            },
            "robot": {
                "price": 750,
                "emoji": ":robot:"
            },
            "chicken": {
                "price": 1250,
                "emoji": ":chicken:"
            },
            "wolf": {
                "price": 1250,
                "emoji": ":wolf:"
            },
            "dragon": {
                "price": 9750,
                "emoji": ":dragon_face:"
            },
            "wumpus": {
                "price": 13000,
                "emoji": "<:PrismWumpus:730898074255360011>"
            },
            "prism": {
                "price": 1000000,
                "emoji": "<:PrismPet:729824575323504733>"
            }
        }

    @commands.command()
    async def adopt(self, ctx, *, pet = None):

        if not pet:

            pets, c = "", 1

            for pet in self.pets:

                pets += f"[{c}] {self.pets[pet]['emoji']} {Tools.uppercase(pet)} (${self.pets[pet]['price']})\n"

                c += 1

            embed = discord.Embed(title = "Prism Pet Shop", description = "The cutest pets on planet discord!", color = 0x126bf1)

            embed.add_field(name = "Pets", value = pets, inline = False)

            embed.add_field(name = "How to adopt", value = "To adopt a pet, either use:\n``adopt [pet name]``\nor use\n``adopt [pet id]``")

            embed.set_author(name = " | Petshop", icon_url = self.bot.user.avatar_url)

            return await ctx.send(embed = embed)

        pet = pet.lower()

        try:

            id = int(pet) - 1

            if id < 0:

                return await ctx.send(embed = Tools.error("Invalid pet ID!"))

            pets = []

            for _pet in self.pets:

                pets.append(_pet)

            try:

                pet = pets[id]

            except:

                return await ctx.send(embed = Tools.error("Invalid pet ID!"))

        except:

            if not pet in self.pets:

                return await ctx.send(embed = Tools.error("That isn't a valid pet!"))

        db = loads(open("db/users", "r").read())

        user = db[str(ctx.author.id)]

        if user["pet"]["level"]:

            return await ctx.send(embed = Tools.error("You already have a pet, get rid of it using the ``shelter`` command."))

        elif not user["balance"] >= self.pets[pet]["price"]:

            more = self.pets[pet]["price"] - user["balance"]

            return await ctx.send(embed = Tools.error(f"You need ${more} more to buy a pet {pet}!"))

        user["balance"] -= self.pets[pet]["price"]

        user["pet"]["level"] = 1

        user["pet"]["type"] = pet

        user["pet"]["name"] = "Unnamed " + Tools.uppercase(pet)

        user["pet"]["adopted_on"] = str(date.today())

        open("db/users", "w").write(dumps(db, indent = 4))

        embed = discord.Embed(title = "Adoption Successful!", description = f"Have fun with your new pet {pet}.\n\n(you can name it with the ``name`` command)", color = 0x0ee323)

        embed.set_author(name = " | Adoption", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Adopted by {ctx.author}.", icon_url = ctx.author.avatar_url)

        return await ctx.send(embed = embed)

# Link to bot
def setup(bot):
    bot.add_cog(Adopt(bot))
