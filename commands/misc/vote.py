# Modules
import discord
import requests

from json import loads
from asyncio import sleep

from discord.ext import commands
from assets.prism import Cooldowns, Tools

# Main Command Class
class Vote(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Gifts you money for upvoting the bot on top.gg"
        self.usage = "vote"
        
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4NTU1MDUwNDI3Njc4NzIwMCIsImJvdCI6dHJ1ZSwiaWF0IjoxNTg1NzkxNjM3fQ.jPyvYRUs46wsk6gya_IqvWiSrFjjwSR5jCkqEt-DH2o"
        
    @commands.command()
    async def vote(self, ctx):
            
        if Cooldowns.on_cooldown(ctx, "vote"):

            return await ctx.send(embed = Cooldowns.cooldown_text(ctx, "vote"))

        bot_data = loads(requests.get("https://top.gg/api/bots/685550504276787200", headers = {"Authorization": self.token}).text)

        base_upvotes = bot_data["points"]

        embed = discord.Embed(title = "Click here to vote for Prism!", description = "When your done, send a message in this channel.", url = "https://top.gg/bot/685550504276787200/vote", color = 0x126bf1)

        await ctx.send(embed = embed)

        def check(m):

            return m.author == ctx.author and m.channel == ctx.channel

        await self.bot.wait_for("message", check = check)
            
        embed = discord.Embed(title = "This might take a few minutes.", description = "Since the top.gg API doesn't update instantly,\nit might take a minute to verify your vote.", color = 0x126bf1)

        embed.set_author(name = " | Waiting for change", icon_url = self.bot.user.avatar_url)

        embed.set_footer(text = f" | Requested by {ctx.author}.", icon_url = ctx.author.avatar_url)

        message = await ctx.send(embed = embed)
        
        failed_attempts = 0
        
        while failed_attempts < 16:
            
            bot_data = loads(requests.get("https://top.gg/api/bots/685550504276787200", headers = {"Authorization": self.token}).text)

            current_upvotes = bot_data["points"]
            
            if current_upvotes > base_upvotes:
            
                db = loads(open("db/users", "r").read())

                db[str(ctx.author.id)]["balance"] = db[str(ctx.author.id)]["balance"] + 2750

                open("db/users", "w").write(json.dumps(db, indent = 4))
                
                embed = discord.Embed(title = "Thanks for voting!", description = "Since you voted, you get a free $2,750.", color = 0x0ee323)

                embed.set_author(name = " | Successful Vote", icon_url = self.bot.user.avatar_url)

                embed.set_footer(text = " | You can vote every 12 hours.", icon_url = ctx.author.avatar_url)

                try:

                    await ctx.author.send(embed = embed)

                except:

                    await ctx.send(embed = embed)

                try:

                    await message.delete()

                except:

                    pass

                if Tools.has_flag(db, ctx.author, "premium"):

                    await Cooldowns.set_cooldown(ctx, "vote", 86400)

                    break

                await Cooldowns.set_cooldown(ctx, "vote", 43200)

                break
                
            await sleep(15)
                
            failed_attempts += 1

# Link to bot
def setup(bot):
    bot.add_cog(Vote(bot))
