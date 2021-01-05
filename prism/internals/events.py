# Modules
from discord.ext import commands
from ..utils.colors import colored
from ..utils.presets import guild_preset

# Event class
class Events(object):

    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):

        # Logging information
        print(colored("Prism v2 - Logged in as", "blue"), colored(self.bot.user, "yellow"))
        print(colored("=" * 50, "blue"))
        print()

        # Process guilds
        for guild in self.bot.guilds:

            _ = self.bot.get_prism_guild(guild.id)
            if _ is None:

                # Register guild
                self.bot.database.insert_into("guilds", guild_preset(guild))
                print("Registered", guild.name, "into the database.")  # Temporary

    async def on_message(self, message):

        # Check that we are in a server
        if not message.guild:
            return

        # Check our prefix
        print("check prefix here")

        return True

    async def member_joined(self, member):
        pass

    async def member_left(self, member):
        pass

    async def guild_add(self, guild):

        # Register guild
        self.bot.database.insert_into("guilds", guild_preset(guild))
        print("Registered", guild.name, "into the database.")  # Temporary

    async def guild_remove(self, guild):

        # Remove guild
        self.bot.database.remove_from("guilds", "id", guild.id)
        print("Removed", guild.name, "from the database.")  # Temporary

    async def message_delete(self, message):
        pass

    async def error_handler(self, ctx, error):

        # Error types
        if isinstance(error, commands.CommandNotFound):
            return

        # Console logging
        error_type = type(error).__name__
        self.bot.logger.error(f"{error_type}: {error}")
