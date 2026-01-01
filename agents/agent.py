"""
agent class using Mesa.
"""

from typing import Optional
from mesa import Agent
from agents.properties.agent_properties import AgentProperties
from agents.network import AgentNetwork


class PredatorPreyAgent(Agent):
    """
    Base agent class for predator-prey simulation.
    Inherits from mesa.Agent.
    """

    def __init__(
        self,
        model,
        network: Optional[AgentNetwork] = None,
        properties: Optional[AgentProperties] = None,
    ):
        """Initialize the agent."""
        super().__init__(model)
        self.pos = None
        self.network = network
        self.properties = properties

    def _create_default_properties(self) -> AgentProperties:
        """Creates default properties - to be overridden in subclasses."""
        raise NotImplementedError

    @property
    def energy(self) -> float:
        """Energy property for easy access."""
        raise NotImplementedError

    @energy.setter
    def energy(self, value: float):
        """Energy setter."""
        pass

    @property
    def max_energy(self) -> float:
        """Max energy property."""
        raise NotImplementedError

    @property
    def fitness(self) -> float:
        """Fitness property."""
        raise NotImplementedError

    @fitness.setter
    def fitness(self, value: float):
        """Fitness setter."""
        pass

    def is_alive(self) -> bool:
        """Check if agent is alive."""
        raise NotImplementedError

    def step(self):
        """Mesa step method - called by scheduler."""
        pass

    def act(self):
        """Agent action - to be implemented in subclasses."""
        raise NotImplementedError

    def move_towards(self, target_pos):
        """Move one step towards target position."""
        pass
