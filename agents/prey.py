"""
Prey agent class.
"""

from typing import Optional
from agents.agent import PredatorPreyAgent
from agents.network import AgentNetwork


class Prey(PredatorPreyAgent):
    """
    Prey agent - flees from predators.
    """

    def __init__(self, model, network: Optional[AgentNetwork] = None):
        """Initialize the prey."""
        pass

    def act(self):
        """Prey behavior - flee from nearest predator."""
        pass

    def _distance_to(self, pos) -> float:
        """Calculate distance to position (toroidal)."""
        raise NotImplementedError
