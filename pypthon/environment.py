import itertools as it
import os
import re
import shutil as sh
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
