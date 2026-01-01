"""
Predator agent class.
"""

from typing import Optional
from agents.agent import PredatorPreyAgent
from agents.network import AgentNetwork
from world.config import config
from agents.properties.predator_properties import PredatorProperties


class Predator(PredatorPreyAgent):
    """
    Predator agent - hunts prey.
    """

    def __init__(self, model, network: Optional[AgentNetwork] = None):
        """Initialize the predator."""
        properties = PredatorProperties(
            energy=config.predator_max_energy,
            max_energy=config.predator_max_energy,
            speed=config.predator_speed,
        )
        super().__init__(model, network, properties)

    def act(self):
        """Predator behavior - hunt nearest prey."""
        pass

    def _distance_to(self, pos) -> float:
        """Calculate distance to position (toroidal)."""
        raise NotImplementedError
