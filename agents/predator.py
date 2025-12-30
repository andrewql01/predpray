"""
Predator agent class.
"""

from typing import Optional
from agents.agent import PredatorPreyAgent
from agents.network import AgentNetwork


class Predator(PredatorPreyAgent):
    """
    Predator agent - hunts prey.
    """

    def __init__(self, model, network: Optional[AgentNetwork] = None):
        """Initialize the predator."""
        pass

    def act(self):
        """Predator behavior - hunt nearest prey."""
        pass

    def _distance_to(self, pos) -> float:
        """Calculate distance to position (toroidal)."""
        raise NotImplementedError
