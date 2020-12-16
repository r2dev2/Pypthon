import functools
import itertools as it
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import reduce
from pathlib import Path
from pprint import pprint
from sys import stdin


__executor = ThreadPoolExecutor()


def iterable_first(fn):
    """
    Decorator used to make the piped value the first argument.
    """
    @functools.wraps(fn)
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

    This streams both input and the response.
    """
    process = __open_process(command)
    __executor.submit(__write_to_process, process, iterable)
    return process.stdout


@iterable_first
def cmap(iterable, func, threads=100):
    """
    Concurrent map.

    Usage:

    >>>  range(3) | cmap requests.get("https://google.com") | uprint
    <Response [200]> <Response [200]> <Response [200]>
    """
    executor = ThreadPoolExecutor(max_workers=threads)
    return executor.map(func, iterable)


@iterable_first
def cfilter(iterable, func, threads=100):
    """
    Concurrent filter.

    Usage:

    >>> ['https://google.com', 'https://google.com/pypthon'] | cfilter url: requests.get(url).status_code == 200 | uprint
    https://google.com
    """
    def map_fn(value):
        return func(value), value

    for is_valid, value in cmap(map_fn, threads, iterable):
        if is_valid:
            yield value


def result_fn(func):
    """
    Wrapper to return either the function return or the exception raised.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return e
    return inner


def __open_process(command):
    pipe = subprocess.PIPE
    return subprocess.Popen(
        shlex.split(command),
        universal_newlines=True,
        stdin=pipe,
        stdout=pipe,
        stderr=pipe,
    )


def __write_to_process(process, iterable):
    for line in iterable:
        process.stdin.write(line + "\n")
        process.stdin.flush()
    process.stdin.close()
