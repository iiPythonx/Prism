# Modules
import discord
from requests import get

from json import loads, loads
from assets.prism import Tools

from discord.ext import commands

# Main Command Class
class Dictionary(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Lookup a word in the urban dictionary"
        self.usage = "dictionary [word]"

    @commands.command(aliases = ["dict", "lookup", "ud"])
    async def dictionary(self, ctx, *, word = None):

        #return await ctx.send("Sorry, but this command is temporarily disabled.\nDetails: ``API not responding well``")
      
        db = loads(open("db/guilds", "r").read())

        if not "nsfw-enabled" in db[str(ctx.guild.id)]["tags"]:

          return await ctx.send(embed = Tools.error("NSFW is not enabled in this server."))

        elif not ctx.channel.nsfw:

          return await ctx.send(embed = Tools.error("This channel doesn't allow NSFW."))

        elif not word:
            
            return await ctx.send(embed = Tools.error("No word/phrase specified."))
        
        elif word.startswith("<@!"):
            
            word = Tools.getClosestUser(word).name
     
        elif len(word) > 50:

            return await ctx.send(embed = Tools.error("That word/phrase is too long."))

        elif word.lower() == "commuter":

            embed = discord.Embed(title = word, description = f"[Commuter] is a person that likes to play [beamng.drive]. His catchphrase is [idiot] although he has multiple other [phrases] that he says often. He likes playing around with [Prism] and talking about corn. He plays Roblox games and stuff, he is [super duper insanely] smart when it comes to learning Python.", color = 0x126bf1)

            embed.set_author(name = " | Dictionary", icon_url = self.bot.user.avatar_url)
            
            embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

            return await ctx.send(embed = embed)

        request = get(f"https://api.urbandictionary.com/v0/define?term={word.lower()}", headers = {"content-type": "application/json"}).text
    
        if not request:
        
          return await ctx.send(embed = Tools.error("Couldn't connect to the urban dictionary."))
    
        data = loads(request)

        if len(data["list"]) == 0:

            return await ctx.send(embed = Tools.error(f"No dictionary results found for: ``{word}``."))

        embed = discord.Embed(title = word, description = data["list"][0]["definition"], color = 0x126bf1)

        embed.set_author(name = " | Dictionary", icon_url = self.bot.user.avatar_url)
        
        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        try:

            return await ctx.send(embed = embed)
        
        except:
            
            return await ctx.send(embed = Tools.error("That description is too long to send."))

# Link to bot
def setup(bot):
    bot.add_cog(Dictionary(bot))
