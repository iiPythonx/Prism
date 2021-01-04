def guild_preset(guild):

    return (
        # Information
        guild.id,  # Server ID
        "p2!",  # Prefix - this needs changed later

        # Settings
        False,  # Enable NSFW commands
        True,  # Enable leveling messages
        True,  # Enable errors
        False,  # Command-not-found message

        # Setting values
        0,  # Join/leave channel
        "Never"  # Last updated
    )
