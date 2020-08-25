# Copyright 2020-20xx; Benjamin O'Brien
# Licensed under the MIT license.

# Modules
from termcolor import colored

# Main class
class Logging:

  """

    Represents the Prism logging system.
    This allows you to output errors in a more user-friendly format.

  """

  def error(_, e):

    """

      Prints an error message to the console.
      By default, in a red message wrapped in "[ERROR]".

    """

    return print(colored(f"[ERROR]: {e.split('exception: ')[1]}", "red"))

  def warn(_, e):

    """

      Prints an warning message to the console.
      By default, in a yellow/orange message wrapped in "[WARN]".

    """

    return print(colored(f"[WARN]: {e}", "yellow"))

  def inform(_, e):

    """

      Prints an informative message to the console.
      By default, in a green message wrapped in "[INFO]"

    """

    return print(colored(f"[INFO]: {e}", "green"))
