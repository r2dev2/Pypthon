import functools
import itertools as it
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
import typing as tp
from functools import reduce
from pathlib import Path
from pprint import pprint
from sys import stdin


def iterable_first(fn):
    """
    Decorator used to make the piped value the first argument.
    """
    def inner(*args):
        *regular_args, piped = args
        return fn(piped, *regular_args)
    return inner


@iterable_first
def uprint(iterable, kwargs={}):
    """
    Allows unpacking into print.

    Usage:

    >>> ["hello", "world"] | uprint {"sep": ":"}
    hello:world
    >>> ["hello", "world"] | uprint
    hello world
    """
    return print(*iterable, **kwargs)
    

@iterable_first
def ufunc(iterable, func, kwargs={}):
    """
    Allows unpacking iterable into functions.

    Usage:

    >>> ["hello", "world"] | ufunc print {"sep": ":"}
    hello:world
    >>> ["hello", "world"] | ufunc print
    hello world
    """
    return func(*iterable, **kwargs)


def sh(command, iterable):
    """
    Opens a shell function.

    This streams input but not the response.
    """
    pipe = subprocess.PIPE
    process = subprocess.Popen(
        shlex.split(command),
        universal_newlines=True,
        stdin=pipe,
        stdout=pipe,
        stderr=pipe,
    )
    for line in iterable:
        process.stdin.write(line + "\n")
        process.stdin.flush()
    process.stdin.close()
    return process.stdout
