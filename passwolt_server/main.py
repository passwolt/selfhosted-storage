#!/usr/bin/env python3

import argparse
from passwolt_server.start import start
from passwolt_server.stop import stop
from passwolt_server.install import install


def main():
    """
    The usual entry point.
    """
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter,
        prog="passwolt-server"
    )
    parser.add_argument(
        "action", choices=("start", "stop", "install"),
        help="Launch the command."
    )
    args = parser.parse_args()
    if args.action == "start":
        start()
    elif args.action == "stop":
        stop()
    elif args.action == "install":
        install()


if __name__ == '__main__':
    main()