# Modules
from ..utils.colors import colored

# Event class
class Events(object):

    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):

        # Logging information
        print(colored("Prism v2 - Logged in as", "blue"), colored(self.bot.user, "yellow"))
        print(colored("=" * 50, "blue"))
        print()
