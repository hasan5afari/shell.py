import os

from typing import Callable


def exit_procedure(
    flags: list[str],
    options: dict[str, str | float],
    arguments: list[str | int],
) -> int:
    exit()

    return 0


def is_executable(path: str) -> bool:
    if not os.path.isfile(path):
        return False

    return os.access(path, os.X_OK)


def find_executable(command: str) -> str:
    PATH_ENV = os.getenv("PATH")
    directories = PATH_ENV.split(os.pathsep)

    for directory in directories:
        items = os.listdir(directory) if os.path.exists(directory) else []
        for item in items:
            full_path = os.path.join(directory, item)
            if os.path.splitext(item)[0] == command and is_executable(full_path):
                return full_path

    return ""


def type_procedure(
    flags: list[str],
    options: dict[str, str | float],
    arguments: list[str | int],
) -> int:
    if not arguments:
        return -1

    argument = arguments[0]
    builtin_commands = BuiltinCommands.get_builtin_commands()

    if argument in builtin_commands:
        print(f"{argument} is a shell builtin")
        return 0

    executable_path = find_executable(argument)

    if executable_path:
        print(f"{argument} is {executable_path}")
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
