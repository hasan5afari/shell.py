from typing import Callable


class Command:
    def __init__(
        self,
        name: str,
        flags: list[str],
        options: dict[str, str | float],
        arguments: list[str | int],
        procedure: (
            Callable[[list[str], dict[str, str | float], list[str | int]], int] | None
        ),
    ) -> None:
        self._name = name
        self._flags = flags
        self._options = options
        self._arguments = arguments
        self._procedure = procedure

    def run(
        self,
    ) -> int:
        if self._procedure:
            return self._procedure(
                self._flags,
                self._options,
                self._arguments,
            )
        else:
            print(f"{self._name}: not found")

            return -1
