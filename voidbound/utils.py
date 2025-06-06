"""Helper functions and common utilities."""

# TODO: Add text formatting helpers, dice rolls, and other utility functions.


def roll_die(sides: int) -> int:
    """Return a random number between 1 and the number of sides."""
    import random

    return random.randint(1, sides)
