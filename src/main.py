import sys


def process_input(input: str) -> tuple[str, list[str]]:
    tokens = input.split(" ")
    num_tokens = len(tokens)

    command = tokens[0] if num_tokens > 0 else ""
    extra_stuff = tokens[1:] if num_tokens > 1 else []

    return command, extra_stuff


def main():
    while True:
        sys.stdout.write("$ ")

        command, extra = process_input(input())

        if command == "exit":
            exit()
        elif command == "echo":
            if extra:
                print(" ".join(extra))
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
