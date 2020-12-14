import argparse
import sys

# TODO Figure out why I need different imports for pip and for testing
try:
    from .parser import parse_command
    from .environment import *
except ImportError:
    from parser import parse_command
    from environment import *


def main() -> None:
    parser = argparse.ArgumentParser(description="Python with pipes")
    parser.add_argument("command", help="the pypthon command")
    parser.add_argument("-s", "--show-python", help="show python code generated", action="store_true")
    parser.add_argument("-i", "--import", help="module to import eg: -i 'requests' -i 'numpy'", default=[], action="append")
    parser.add_argument("-d", "--dry-run", help="don't run python code", action="store_true")
    parser.add_argument("-e", "--environment", help="show variables excluding -i imports in environment", action="store_true")
    args = parser.parse_args()
    python = parse_command(args.command)
    if args.show_python or args.dry_run:
        print(python)
    code = '\n'.join([
        get_user_custom_setup(),
        python
    ])
    for module in getattr(args, "import"):
        import_string = f"import {module}"
        if not args.dry_run:
            exec(import_string, globals())
    if args.dry_run or args.environment:
        pprint(sorted(v for v in globals() if v[:1] != "_"))
    if not args.dry_run:
        exec(code)


def get_user_custom_setup() -> str:
    pyprc = Path.home() / ".pypthonrc.py"
    pyprc.touch()
    with open(pyprc, 'r') as fin:
        return fin.read()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
