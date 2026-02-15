import sys


def main() -> None:
    sys.stdout.write("$ ")

    user_command = input()
    print(f"{user_command}: command not found")


if __name__ == "__main__":
    main()
