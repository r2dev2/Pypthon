from typing import *

literal_chars = {'"': '"', "'": "'", '(': ')', '[': ']', '{': '}'}
operator_chars = {'*', '**', '^', '&', '*', '<', '<=', '==',
                  '>', '>=', '!=', '+', '-', '/', '<<', '>>'}

def parse_command(command: str) -> str:
    """
    Turns a command into valid python.
    """
    segments = get_piped_segments(command)
    value = segments[0]
    for segment in segments[1:]:
        value = __combine_two_piped(value, segment)
    return value


def get_piped_segments(command: str) -> List[str]:
    """
    Gets the python code of each command in between pipes.
    """
    commands = []
    last_idx = 0
    is_creating_literal = []

    for i, c in enumerate(command + '|'):
        if is_creating_literal and c == literal_chars.get(is_creating_literal[-1]):
            is_creating_literal.pop()
        elif c in literal_chars:
            is_creating_literal.append(c)
        elif c == '|' and not is_creating_literal:
            commands.append(pypthon_cmd_to_python(command[last_idx:i]))
            last_idx = i + 1

    return commands


def pypthon_cmd_to_python(command: str) -> str:
    command = command.strip()

    if __is_literal(command):
        return command

    name, args = __get_function_name_and_args(command)

    return f"{name}({', '.join(args)})"


def __is_literal(code: str) -> bool:
    code = code.strip()
    return literal_chars.get(code[:1]) == code[-1:]


def __get_function_name_and_args(command: str) -> Tuple[str, List[str]]:
    command = command.strip()
    try:
        sidx = command.index(' ')
        return command[:sidx], __spaces_separated_to_args(command[sidx:])
    except ValueError:
        return command, []


def __spaces_separated_to_args(space_arg: str) -> List[str]:
    args = []
    last_idx = 0
    is_creating_literal = []

    for i, c in enumerate(space_arg + ' '):
        if is_creating_literal and c == literal_chars.get(is_creating_literal[-1]):
            is_creating_literal.pop()
        elif c in literal_chars:
            is_creating_literal.append(c)
        elif c == ' ' and not is_creating_literal:
            arg = space_arg[last_idx:i].strip()
            if arg:
                args.append(arg)
                last_idx = i + 1

    args_after_operators = []

    while args:
        arg = args.pop()
        is_colon = arg[-1:] == ':'
        if arg[-1:] in operator_chars or arg[-2:] in operator_chars or is_colon:
            prev = args_after_operators[-1]
            if is_colon:
                args_after_operators[-1] = f"lambda {arg} {prev}"
            else:
                other_value = args.pop()
                args_after_operators[-1] = f"{other_value} {arg} {prev}"
        else:
            args_after_operators.append(arg)

    return args_after_operators[::-1]


def __combine_two_piped(first: str, second: str) -> str:
    if second[-2:-1] != '(':
        return f"{second[:-1]}, {first}{second[-1:]}"
    return f"{second[:-1]}{first}{second[-1:]}"
