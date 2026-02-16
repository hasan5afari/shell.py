from typing import Callable

from command import Command


def exit_procedure(
    flags: list[str],
    options: dict[str, str | float],
    arguments: list[str | int],
) -> int:
    exit()

    return 0


def type_procedure(
    flags: list[str],
    options: dict[str, str | float],
    arguments: list[str | int],
) -> int:
    builtin_commands = BuiltinCommands.get_builtin_commands()

    argument = arguments[0]
    if len(arguments) > 0 and argument in builtin_commands:
        print(f"{argument} is a shell builtin")
    else:
        print(f"{argument}: not found")

    return 0


def echo_procedure(
    flags: list[str],
    options: dict[str, str | float],
    arguments: list[str | int],
) -> int:
    if len(arguments) > 0:
        print(" ".join(arguments))

    return 0


class BuiltinCommands:
    exit = exit_procedure
    type = type_procedure
    echo = echo_procedure

    @staticmethod
    def get_builtin_commands() -> (
        dict[str, Callable[[list[str], dict[str, str | float], list[str | int]], int]]
    ):
        return {
            name: value
            for name, value in BuiltinCommands.__dict__.items()
            if not name.startswith("__")
        }
