# Copyright 2020-20xx; Benjamin O'Brien (iiPython)
# setup.py

# Modules
from os.path import exists
from json import loads, dumps
from os import mkdir, system, name

# Initialization
print("Checking if this release is ready to go...")

if not exists("db"):

    mkdir("db")

    print("\tcreated database folder")

# Setup folders
if not exists("db/users"):

    open("db/users", "w+").write(dumps({}))

    print("\tcreated users database")

if not exists("db/guilds"):

    open("db/guilds", "w+").write(dumps({}))

    print("\tcreated guilds database")

# Setup .env file
print()

token = input("Bot token: ")
dbltoken = input("DBL token (leave empty if none): ")
wolfram = input("Wolframalpha key: ")

if not dbltoken:

    open("assets/cogs/top.py", "w").write("def setup(bot):\n  pass")

open(".env", "w+").write(f"TOKEN = \"{token}\"\nDBL_TOKEN = \"{dbltoken}\"\n\nWOLFRAMALPHA_KEY = \"{wolfram}\"")

# Install dependencies
x = input("Would you like to install dependencies (Y/n)? ")

if x.lower() in ["y", "n", "yes", "no"]:

    if x.lower() in ["yes", "y"]:

        python = "python"

        if name != "nt":

            python += "3"

        system(f"{python} -m pip install -r requirements.txt")

# Finish up
print()

print("Prism should be ready to launch.")
