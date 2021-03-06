"""
Start Passwolt storage server (only works if installed.)
"""

import os

from passwolt_server.util import display, SERVER_CONFIG_PATH


def _is_installed():
    """
    Detect whether already installed or not.
    """
    return os.path.exists(SERVER_CONFIG_PATH)


def start():
    display("""
    ************************************************************************
    ########################################################################

              / __ \____ ____________      ______  / / /_
             / /_/ / __ `/ ___/ ___/ | /| / / __ \/ / __/
            / ____/ /_/ (__  |__  )| |/ |/ / /_/ / / /_
           /_/    \__,_/____/____/ |__/|__/\____/_/\__/  runner

    ########################################################################
    ************************************************************************
    """, style=["blue"])
    display(
        "Passwolt server is a self hosted and managed server to store "
        "encrypted passwords."
    )
    display("Starting-up the server...")
    if not _is_installed():
        display(
            "Hold on buddy! Looks like you haven't installed passwolt-server.\n"
            "This makes me sad :(\n"
            "You need to run the installation (only once, I promise!), by executing "
            "the following:\n"
            "  $ passwolt-server install\n\n"
            "Once that is done, please come back here to start the server :D",
            style=["bold", "red"]
        )

    # Start the server in background
