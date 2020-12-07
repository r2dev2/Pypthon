import os
import shutil as sh
import sys
from pathlib import Path
from pprint import pprint
from sys import stdin

def uprint(kwargs, iterable):
    """
    Allows unpacking into print

    Usage:

    >>> ["hello", "world"] | uprint {"sep": ":"}
    hello:world
    """
    print(*iterable, **kwargs)
