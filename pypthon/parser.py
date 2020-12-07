from typing import *

string_chars = {'"', "'"}

def parse_command(command: str) -> str:
    """
    Turns a command into valid python.
    """


def get_piped_segments(command: str) -> List[str]:
    """
    Gets the python code of each command in between pipes.
    """
    commands = []
    last_idx = 0
    is_creating_string = ""

    for i, c in enumerate(command + '|'):
        if c in string_chars and is_creating_string:
            if c == is_creating_string:
                is_creating_string = ""
        elif c in string_chars and not is_creating_string:
            is_creating_string = c
        elif c == '|' and not is_creating_string:
            commands.append(pypthon_to_python(command[last_idx:i]))
            last_idx = i + 1

    return commands


def pypthon_to_python(command: str) -> str:
    return command.strip()
