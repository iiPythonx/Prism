# Prism Discord Bot - Rewrite Edition
# The only bot you will ever need.

# Last revision: January 1st, 2021.
# Copyright 2020-20xx MIT; iiPython, see LICENSE for more details.


# Modules
import sys
from prism import Prism
from os import getenv, listdir

# Initialization
bot = Prism()

# Command loader
for command_folder in listdir("commands"):

    # Loop through command category
    for command in listdir(f"commands/{command_folder}"):

        # Check for a python file
        if command.endswith(".py"):

            # Ensure we can load
            if "--no-commands" in sys.argv:
                continue

            # Load command
            bot.load_extension(f"commands.{command_folder}.{command[:-3]}")

# Special extensions
if "--no-special-ext" not in sys.argv:

    # Loop through our externals
    for external in listdir("prism/externals"):

        # Check its a python file
        if external.endswith(".py"):

            # Load extension
            bot.load_extension(f"prism.externals.{external[:-3]}")

# Bot events
@bot.event
async def on_ready():
    return await bot.events.on_ready()

@bot.event
async def on_command_error(ctx, error):
    return await bot.events.error_handler(ctx, error)

@bot.event
async def on_message(msg):

    result = await bot.events.on_message(msg)

    if result is not True:
        return

    return await bot.process_commands(msg)

@bot.event
async def on_guild_join(guild):
    return await bot.events.guild_add(guild)

@bot.event
async def on_guild_remove(guild):
    return await bot.events.guild_remove(guild)

@bot.event
async def on_member_join(member):
    return await bot.events.member_joined(member)

@bot.event
async def on_member_remove(member):
    return await bot.events.member_left(member)

@bot.event
async def on_message_delete(message):
    return await bot.events.message_delete(message)

# Discord connection
token = getenv("BOT_TOKEN")
if token is None:
    print("No token is inside of the .env file, quitting.")
    exit()

bot.run(token, reconnect = True)
