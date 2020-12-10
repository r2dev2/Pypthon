import sys

# TODO Figure out why I need different imports for pip and for testing
try:
    from .environment import *
    from . import parser
except ImportError:
    from environment import *
    import parser


def main():
    python = parser.parse_command(" ".join(sys.argv[1:]))
    eval(python)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
