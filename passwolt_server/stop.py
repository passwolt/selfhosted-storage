"""
Stop the Passwolt server
"""

import os
import psutil
import signal

from passwolt_server.util import display, PID_FILE_PATH
from time import sleep


def stop():
    # Send a SIGTERM signal.
    display("Stopping the passwolt server...", style=["cyan"])
    with open(PID_FILE_PATH, 'r') as f:
        pid = int(f.read())
        os.kill(pid, signal.SIGTERM)
    timeout = 10
    delay = 0.5
    while psutil.pid_exists(pid) and timeout:
        # wait until the process exists or wait timeout
        sleep(delay)
        timeout -= delay
    display("Stopped!", style=["green"])
