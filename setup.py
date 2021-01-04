# Modules
import os
import sqlite3

import subprocess
from shutil import which

from os.path import exists, isdir, isfile

# Initialization
print("Setup is initializing, please wait...")

CS_PYTHONS = ["python", "python3", "python3.7", "python3.8", "python3.9"]
CS_USERDB  = """
CREATE TABLE IF NOT EXISTS users (
    id long,
    balance integer,

    level integer,
    experience integer,
    reputation integer

    biography text,
    blacklisted boolean
)
"""
CS_GUILDDB = """
CREATE TABLE IF NOT EXISTS guilds (
    id long,
    prefix text,

    nsfw boolean,
    levels boolean,
    errors boolean,
    commandnotfound boolean,

    joinleave long,
    lastupdated text
)
"""
CS_PETDB   = """
CREATE TABLE IF NOT EXISTS pets (
    name text,
    type text,

    level integer,
    holding integer,

    adopted text,
    owner integer
)
"""
CS_DOTENV  = """# Tokens
BOT_TOKEN   = "{}"
DBL_TOKEN   = "{}"

# API Keys
WOLFRAM_KEY = "{}"
CATAPI_KEY  = "{}"
GIPHY_KEY   = "{}"
"""

# Clear function
def clear():

    command = "clear"
    if os.name == "nt":
        command = "cls"

    subprocess.run([command], shell = True)

# Locate python command
py = CS_PYTHONS[0]
for python_command in CS_PYTHONS:
    if which(python_command):
        py = python_command

# Clear screen
clear()

# ===== DATABASE INITIALIZATION =====
print("Checking the database is setup...")

# Check for the folder
if not isdir("db"):

    # Remove file-version
    if isfile("db"):
        os.remove("db")

    # Create database folder
    os.mkdir("db")

    # Log
    print(" ", "created database folder")

else:
    print(" ", "folder already exists")

# Check for the databases
def initialize_db(filename, command):

    # Handle connection
    connection = sqlite3.connect("db/" + filename)
    cursor = connection.cursor()

    # Initialization
    cursor.execute(command)

    # Save database
    connection.commit()
    connection.close()

initialize_db("users.db", CS_USERDB)
initialize_db("guilds.db", CS_GUILDDB)
initialize_db("pets.db", CS_PETDB)

print(" ", "databases initialized")

# ===== .ENV INITIALIZATION =====
print()

def setup_dotenv():

    # Introduction
    print("Setting up .env file now.")
    print("=" * 50)

    # Grab values
    bot_token = input("Bot token (discord.com/developers/applications): ")
    dbl_token = input("Top.gg token (optional): ")

    wolf_key  = input("WolframAlpha API key (developer.wolframalpha.com/portal/myapps): ")
    cat_key   = input("CatAPI API key (thecatapi.com/signup): ")
    giphy_key = input("Giphy API key (developers.giphy.com/dashboard): ")

    # Substitute
    with open(".env", "w+") as file:
        file.write(CS_DOTENV.format(
            bot_token,
            dbl_token,
            wolf_key,
            cat_key,
            giphy_key
        ))

    # Log
    print()
    print("Successfully configured .env file.")

# Check if we should setup our .env file
if not exists(".env"):
    setup_dotenv()

else:

    # It already exists, should we overwrite?
    print("Setup has detected an existing .env file.")
    x = input("Should we reconfigure it? (y/N): ")

    if x and x.lower() in ["yes", "y"]:
        print()
        setup_dotenv()

print()

# ===== DEPENDENCIES INITIALIZATION =====
print("Prism uses a requirements.txt file to contain dependencies.")
print("If you want, this setup file can automatically install these.")

# Confirmation
x = input("Install dependencies? (y/N): ")
if x and x.lower() in ["y", "yes"]:

    print()
    print("Installing dependencies from requirements file...")

    # Execute command
    subprocess.run(
        [py, "-m", "pip", "install", "-U", "-r", "requirements.txt"],
        stdout = subprocess.PIPE  # Hide stupid output
    )

# ===== INSTALL COMPLETION =====
print()
print("The setup file has finished setting up Prism.")
print("You can now launch it with", py + " main.py")
