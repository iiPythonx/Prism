# Modules
from .events import Events
from .core import Internals

from dotenv import load_dotenv
from discord.ext import commands

# Prism class
class Prism(commands.Bot):

    """The Prism class, which wraps commands.Bot"""
    def __init__(self):
        super().__init__(
            command_prefix = self.locate_prefix,
            case_insensitive = True,
            owner_ids = [
                633185043774177280,
                666839157502378014
            ]
        )
        self.core = Internals()
        self.events = Events(self)

        self.database = self.core.database
        load_dotenv()

    def locate_prefix(self):
        return "p2!"  # Temporary solution
