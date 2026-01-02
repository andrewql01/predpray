"""
Grass agent class - food for prey.
"""

from typing import TYPE_CHECKING
from mesa import Agent

if TYPE_CHECKING:
    from world.environment import Environment


class Grass(Agent):
    """
    Grass agent - food source for prey.
    """

    def __init__(self, model: "Environment", energy_value: float = 10.0):
        """Initialize the grass."""
        super().__init__(model)
        self.energy_value = energy_value  # Energy gained by prey when eating
        self.eaten = False  # Whether this grass has been eaten

    def is_available(self) -> bool:
        """Check if grass is available to be eaten."""
        return not self.eaten

    def eat(self) -> float:
        """
        Eat the grass and return energy value.
        Marks the grass as eaten.
        """
        if self.eaten:
            return 0.0
        self.eaten = True
        return self.energy_value
