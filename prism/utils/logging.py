# Modules
import sys
from .colors import colored

# Main class
class Logging(object):

    """
    Represents the Prism logging system.
    This allows you to output errors in a more user-friendly format.
    """

    def error(self, message):
        return print(colored(f"[ERROR]: {message}", "red"))

    def crash(self, message):
        self.error(message)
        return sys.exit(1)

    def warn(self, message):
        return print(colored(f"[WARNING]: {message}", "yellow"))

    def inform(self, message):
        return print(colored(f"[INFO]: {message}", "blue"))
