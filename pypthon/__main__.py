import argparse
import sys

# TODO Figure out why I need different imports for pip and for testing
try:
    from .parser import parse_command
    from .environment import *
except ImportError:
    from parser import parse_command
    from environment import *


def main():
    parser = argparse.ArgumentParser(description="Python with pipes")
    parser.add_argument("command", help="the pypthon command")
    parser.add_argument("-s", "--show-python", help="show python code generated", action="store_true")
    args = parser.parse_args()
    python = parse_command(args.command)
    if args.show_python:
        print(python)
    eval(python)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
