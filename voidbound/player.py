
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Player:
    """A minimal player representation."""

    name: str
    hp: int = 10

    def is_alive(self) -> bool:
        """Return True if the player is alive."""

        return self.hp > 0
