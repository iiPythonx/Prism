# Copyright 2020-20xx; Benjamin O'Brien
# Licensed under the MIT license.

# Modules
from termcolor import colored

# Main class
class Logging(object):

    """

    Represents the Prism logging system.
    This allows you to output errors in a more user-friendly format.

    """

    def __init__(self):

        self.warnings = 0
        self.errors = 0

    def error(self, e):

        """

        Prints an error message to the console.
        By default, in a red message wrapped in "[ERROR]".

        """

        self.errors += 1

        if "exception" in e:

            return print(colored(f"[ERROR]: {e.split('exception: ')[1]}", "red"))

        return print(colored(f"[ERROR]: {e}", "red"))

    def crash(self, e):

        """

        Prints a crash message to the console.
        By default, in a red message wrapped in "[ERROR]".

        WARNING: THIS WILL TERMINATE THE APPLICATION!

        """

        if "exception" in e:

            print(colored(f"[ERROR]: {e.split('exception: ')[1]}", "red"))

        print(colored(f"[ERROR]: {e}", "red"))

        exit()

    def warn(self, e):

        """

        Prints an warning message to the console.
        By default, in a yellow/orange message wrapped in "[WARN]".

        """

        self.warnings += 1

        return print(colored(f"[WARN]: {e}", "yellow"))

    def inform(self, e):

        """

        Prints an informative message to the console.
        By default, in a green message wrapped in "[INFO]"

        """

        return print(colored(f"[INFO]: {e}", "green"))
