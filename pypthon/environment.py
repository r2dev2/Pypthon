import itertools as it
import os
import re
import shlex
import shutil
import subprocess
import sys
from functools import reduce
from pathlib import Path
from pprint import pprint
from sys import stdin


def uprint(kwargs, iterable):
    """
    Allows unpacking into print.

    Usage:

    >>> ["hello", "world"] | uprint {"sep": ":"}
    hello:world
    """
    return print(*iterable, **kwargs)


def ufunc(func, iterable):
    """
    Allows unpacking iterable into functions.

    Usage:

    >>> ["hello", "world"] | ufunc print
    hello world
    """
    return func(*iterable)


def sh(command, iterable):
    """
    Opens a shell function.

    This streams input but not the response.
    """
    pipe = subprocess.PIPE
    process = subprocess.Popen(shlex.split(command), universal_newlines=True, stdin=pipe, stdout=pipe, stderr=pipe)
    for line in iterable:
        process.stdin.write(line + '\n')
        process.stdin.flush()
    process.stdin.close()
    return process.stdout
