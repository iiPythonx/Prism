# Modules
import json
from .events import Events

from .core import Internals
from dotenv import load_dotenv

from discord.ext import commands
from ..utils.logging import Logging

# Prism class
class Prism(commands.Bot):

    """The Prism class, which wraps commands.Bot"""
    def __init__(self):
        super().__init__(
            command_prefix = self.locate_prefix,
            case_insensitive = True
        )

        self.remove_command("help")  # Remove default help command

        self.core = Internals()
        self.events = Events(self)

        self.logger = Logging()

        self.database = self.core.database
        self.__postinit__()

    def __postinit__(self):

        # Load our .env file on windows
        load_dotenv()

        # Load our config.json file
        with open("config.json", "r") as file:
            config = json.loads(file.read())

        self.release = config["release"]
        self.owner_ids = config["owner_ids"]

    def locate_prefix(self):
        return "p2!"  # Temporary solution

    def get_prism_guild(self, guild_id):

        # Try to get guild
        guild = self.database.get_row_by_key("guilds", "id", guild_id)
        if guild is None:
            return None

        # Return our guild
        return self.get_guild(guild[0])