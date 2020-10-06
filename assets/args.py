# Modules
from sys import argv

# Functions
def has_arg(name):

    args = argv[1:]

    return True if name in args else False
