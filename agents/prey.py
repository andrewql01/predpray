"""
Prey agent class.
"""

from typing import Optional
from agents.agent import PredatorPreyAgent
from agents.network import AgentNetwork
from agents.properties.prey_properties import PreyProperties
from world.config import config


class Prey(PredatorPreyAgent):
    """
    Prey agent - flees from predators.
    """

    def __init__(self, model, network: Optional[AgentNetwork] = None):
        """Initialize the prey."""
        properties = PreyProperties(
            energy=config.prey_max_energy,
            max_energy=config.prey_max_energy,
            speed=config.prey_speed,
        )
        super().__init__(model, network, properties)

    def act(self):
        """Prey behavior - flee from nearest predator."""
        pass

    def _distance_to(self, pos) -> float:
        """Calculate distance to position (toroidal)."""
        raise NotImplementedError
