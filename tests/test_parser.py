from .context import pypthon

parser = pypthon.parser


def test_parse_command() -> None:
    test_cases = [
        ['"hello" | print', 'print("hello")'],
        [
            "[1, 2, 3, 4] | map x: x + 1 | list | print",
            "print(list(map(lambda x: x + 1, [1, 2, 3, 4])))",
        ]
        # ["map x: x + 1 | list | print", "print(list(map(lambda x: x + 1, stdin)))"],
    ]
    for case in test_cases:
        assert parser.parse_command(*case[:-1]) == case[-1]


def test_get_piped_segments() -> None:
    test_cases = [
        ['"hello" | print', ['"hello"', "print()"]],
        [
            "[1, 2, 3, 4] | map x: x + 1 | list | print",
            ["[1, 2, 3, 4]", "map(lambda x: x + 1)", "list()", "print()"],
        ],
        [
            '"Hello with a | in between" | print',
            ['"Hello with a | in between"', "print()"],
        ],
    ]

    for case in test_cases:
        assert parser.get_piped_segments(*case[:-1]) == case[-1]


def test_pypthon_cmd_to_python() -> None:
    test_cases = [
        ["print", "print()"],
        ["print 'hello' 'world'", "print('hello', 'world')"],
        ["print 1 + 2", "print(1 + 2)"],
        ["map x: x + 1", "map(lambda x: x + 1)"],
        ["map x: x[1: 2]", "map(lambda x: x[1: 2])"],
        ["filter x: x[: 2] != 'oi'", "filter(lambda x: x[: 2] != 'oi')"],
    ]

    for case in test_cases:
        assert parser.pypthon_cmd_to_python(*case[:-1], False) == case[-1]
