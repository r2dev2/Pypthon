import parser
import sys

from environment import *


def main():
    python = parser.parse_command(" ".join(sys.argv[1:]))
    print(python)
    eval(python)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
