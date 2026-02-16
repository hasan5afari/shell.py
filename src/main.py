import sys

from command import Command
from builtin_commands import BuiltinCommands


def generate_command(input: str) -> Command:
    builtin_commands = BuiltinCommands.get_builtin_commands()

    tokens = input.split(" ")
    num_tokens = len(tokens)

    command_name = tokens[0] if num_tokens > 0 else ""
    command_arguments = tokens[1:] if num_tokens > 1 else []
    command_procedure = (
        builtin_commands[command_name] if command_name in builtin_commands else None
    )

    return Command(command_name, [], {}, command_arguments, command_procedure)


def main():
    while True:
        sys.stdout.write("$ ")

        command = generate_command(input())
        command.run()


if __name__ == "__main__":
    main()
