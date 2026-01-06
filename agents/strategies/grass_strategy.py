"""
Grass-specific action strategy.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agents.agent import BaseAgent


class GrassStrategy:
    """
    Strategy implementation for grass agents.
    """

    def act(self, agent: "BaseAgent") -> None:
        """Execute grass-specific action."""
        # Grass is passive - it doesn't do anything on its own
        # It just waits to be eaten by prey
        # Future: could add growth logic here
        pass
