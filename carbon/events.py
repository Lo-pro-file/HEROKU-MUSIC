import inspect
import logging
import sys
import re

from pathlib import Path
from telethon import events

def register(**args):
    """ Registers a new message. """
    pattern = args.get("pattern")

    r_pattern = r"^[/!.]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = f"(?i){pattern}"

    args["pattern"] = pattern.replace("^/", r_pattern, 1)
