from __future__ import annotations

"""Entry point for the text prototype."""

import sys
from pathlib import Path

# Using an absolute import allows this module to be executed either
# as part of the package (``python -m voidbound.main``) or directly
# via ``python voidbound/main.py`` without triggering a relative
# import error.
if __package__ is None:
    # When executed directly ``python voidbound/main.py`` the parent
    # directory needs to be on ``sys.path`` for absolute imports.
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from voidbound.player import Player


class Game:
    """A very small text-based game loop."""

    def __init__(self) -> None:
        self.player = Player(name="Wanderer")
        self.running = True

    def handle_command(self, command: str) -> None:
        """React to a player command."""

        command = command.lower().strip()
        if command in {"quit", "exit"}:
            print("Farewell.")
            self.running = False
        elif command == "look":
            print("Nothing surrounds you but the endless dark.")
        else:
            print("Unknown command.")

    def run(self) -> None:
        """Run the main input loop."""

        print("Welcome to Voidbound. Type 'quit' to exit.")
        while self.running and self.player.is_alive():
            command = input(" > ")
            self.handle_command(command)


def main() -> None:
    """Entry point for Voidbound."""

    Game().run()


if __name__ == "__main__":
    main()

