#!/usr/bin/env python3
"""
Installation script

Arguments
=========

 - location: where to store the encrypted passwords
 - host: which host to bind to
 - port: which port to run the service on
 - auto-start: should the server automatically run on system boot

"""


from util import display, Question


def main():
    display("""
    ************************************************************************
    ########################################################################

              / __ \____ ____________      ______  / / /_
             / /_/ / __ `/ ___/ ___/ | /| / / __ \/ / __/
            / ____/ /_/ (__  |__  )| |/ |/ / /_/ / / /_
           /_/    \__,_/____/____/ |__/|__/\____/_/\__/  installer

    ########################################################################
    ************************************************************************
    """, style=['blue'])
    display(
        "Passwolt server is a self hosted and managed server to store "
        "encrypted passwords."
    )
    display("""
        Note: This means you would only be able to store and retrieve
          your passwords when the server is accessible by your clients
          (Passwolt browser extension, mobile app, etc.)
          We prefer this, so that your even your encrypted passwords are
          not stored anywhere in the cloud.
          However, if you don't have such a requirement, considering storing
          these on some cloud storage like Google Drive (securely).
        """, style=['bold']
    )
    display("Starting installation...")
    qloc = Question("Where do you want to store the encrypted passwords?")
    location = qloc.prompt()
    qhost = Question("What host to bind to?",
                     choices=['127.0.0.1', '0.0.0.0'],
                     default_choice='127.0.0.1')
    host = qhost.prompt()
    qport = Question("What port to bind to?")
    port = qport.prompt()
    qauto_start = Question("Should the server auto-start from the next boot?",
                           choices=["yes", "no"],
                           default_choice="yes")
    auto_start = qauto_start.prompt()


if __name__ == '__main__':
    main()