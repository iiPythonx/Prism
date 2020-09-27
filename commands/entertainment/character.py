# Modules
import discord
from assets.prism import Tools
from discord.ext import commands

# Command class
class Character(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.desc = "Are there in germany, there are fast cars. IN GERMANY, THERE ARE PARTY PEOPLE. AT HALF PAST FOUR. THERE ARE GERMAN TRUCKS: SCANIA, IVECO, VOLVO, MAN, DAF. AT HALF PAST FOUR! THERE ARE HOSEPOWER- 300, 700, 900. 4 AM. BRATWURST WITH A LARGE BEER, AT HALF PAST FOUR. AVAILABLE IN GERMANY."
        self.usage = "character"
        
    def create_connection(self):

        """Connects to the SQLite database"""

        conn = sqlite3.connect("db/characters.db")

        cursor = conn.cursor()

        self.db_conn = conn  # make it so save works

        return cursor

    def save(self):

        """Save the database"""

        if not self.db_conn:

            raise ValueError("PrismErrDatabase391-There is no database connected.")

        self.db_conn.commit()

        self.db_conn.close()

    def fetch_character(self, id):

        """Create a link to the character database and fetch their information"""

        c = self.create_connection()

        self.save()

        return None  # very very temporary

    @commands.command(aliases = ["char"])
    async def character(self, ctx):

        # bruh moment
        character = self.fetch_character(ctx.author.id)

        if not character:

            return await ctx.send(embed = Tools.error("hi"))

        return await ctx.send(character)

# Link to bot
def setup(bot):

    bot.add_cog(Character(bot))
