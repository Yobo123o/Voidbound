"""Enemy definitions and behavior."""

# TODO: Create base Enemy class with common stats and actions.
# TODO: Define specific enemy types (e.g., Undead, Beast) inheriting from Enemy.

class Enemy:
    """Basic enemy prototype."""

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
