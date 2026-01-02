"""
agent class using Mesa.
"""

import math
import random
from typing import Optional, Tuple, List, TYPE_CHECKING, cast
from mesa import Agent
from agents.properties.agent_properties import AgentProperties
from agents.network import AgentNetwork
from world.config import config

if TYPE_CHECKING:
    from world.environment import Environment


class PredatorPreyAgent(Agent):
    """
    Base agent class for predator-prey simulation.
    Inherits from mesa.Agent.
    """

    def __init__(
        self,
        model: "Environment",
        properties: Optional[AgentProperties] = None,
        network: Optional[AgentNetwork] = None,
    ):
        """Initialize the agent."""
        super().__init__(model)
        self.pos: Optional[Tuple[float, float]] = None
        self.network = network
        self.properties = properties

    def _create_default_properties(self) -> AgentProperties:
        """Creates default properties - to be overridden in subclasses."""
        raise NotImplementedError

    @property
    def energy(self) -> float:
        """Energy property for easy access."""
        if self.properties is None:
            return 0.0
        return self.properties.energy

    @energy.setter
    def energy(self, value: float):
        """Energy setter."""
        if self.properties is not None:
            self.properties.energy = value

    @property
    def max_energy(self) -> float:
        """Max energy property."""
        if self.properties is None:
            return 0.0
        return self.properties.max_energy

    @property
    def fitness(self) -> float:
        """Fitness property."""
        if self.properties is None:
            return 0.0
        return self.properties.fitness

    @fitness.setter
    def fitness(self, value: float):
        """Fitness setter."""
        if self.properties is not None:
            self.properties.fitness = value

    def is_alive(self) -> bool:
        """Check if agent is alive."""
        if self.properties is None:
            return False
        return self.properties.is_alive()

    def step(self):
        """Mesa step method - called by scheduler."""
        pass

    def act(self):
        """Agent action - to be implemented in subclasses."""
        raise NotImplementedError

    def _distance_to(self, pos: Tuple[float, float]) -> float:
        """Calculate toroidal distance to position."""
        if self.pos is None:
            return float("inf")

        x1, y1 = self.pos
        x2, y2 = pos

        # Toroidal distance calculation
        model = cast("Environment", self.model)
        dx = min(abs(x2 - x1), model.width - abs(x2 - x1))
        dy = min(abs(y2 - y1), model.height - abs(y2 - y1))

        return math.sqrt(dx * dx + dy * dy)

    def _find_nearest_agent(self, agent_list: List["PredatorPreyAgent"]):
        """Find nearest agent from list within view range."""
        if self.pos is None or not agent_list:
            return None

        nearest_agent: Optional["PredatorPreyAgent"] = None
        min_distance = config.view_range

        for agent in agent_list:
            if not agent.is_alive():
                continue

            if agent.pos is None:
                continue

            distance = self._distance_to(agent.pos)
            if distance < min_distance:
                min_distance = distance
                nearest_agent = agent

        return nearest_agent

    def move_towards(self, target_pos: Tuple[float, float]) -> None:
        """Move one step towards target position."""
        if self.pos is None or self.properties is None:
            return

        x1, y1 = self.pos
        x2, y2 = target_pos

        # Calculate direction (toroidal)
        dx = x2 - x1
        dy = y2 - y1

        # Handle toroidal wrapping
        model = cast("Environment", self.model)
        if abs(dx) > model.width / 2:
            dx = dx - model.width if dx > 0 else dx + model.width
        if abs(dy) > model.height / 2:
            dy = dy - model.height if dy > 0 else dy + model.height

        # Normalize direction
        distance = math.sqrt(dx * dx + dy * dy)
        if distance > 0:
            dx /= distance
            dy /= distance

        # Move with speed
        speed = self.properties.speed
        new_x = x1 + dx * speed
        new_y = y1 + dy * speed

        # Wrap around toroidal world
        new_x = new_x % model.width
        new_y = new_y % model.height

        # Update position using Mesa space
        model.space.move_agent(self, (new_x, new_y))

    def move_away_from(self, target_pos: Tuple[float, float]) -> None:
        """Move one step away from target position."""
        if self.pos is None or self.properties is None:
            return

        x1, y1 = self.pos
        x2, y2 = target_pos

        # Calculate direction (toroidal)
        dx = x2 - x1
        dy = y2 - y1

        # Handle toroidal wrapping
        model = cast("Environment", self.model)
        if abs(dx) > model.width / 2:
            dx = dx - model.width if dx > 0 else dx + model.width
        if abs(dy) > model.height / 2:
            dy = dy - model.height if dy > 0 else dy + model.height

        # Normalize direction
        distance = math.sqrt(dx * dx + dy * dy)
        if distance > 0:
            dx /= distance
            dy /= distance

        # Move AWAY (opposite direction)
        speed = self.properties.speed
        new_x = x1 - dx * speed
        new_y = y1 - dy * speed

        # Wrap around toroidal world
        new_x = new_x % model.width
        new_y = new_y % model.height

        # Update position using Mesa space
        model.space.move_agent(self, (new_x, new_y))

    def _random_move(self) -> None:
        """Move in a random direction."""
        if self.pos is None or self.properties is None:
            return

        # Random direction
        angle = random.uniform(0, 2 * math.pi)
        speed = self.properties.speed

        x, y = self.pos
        new_x = x + math.cos(angle) * speed
        new_y = y + math.sin(angle) * speed

        # Wrap around toroidal world
        model = cast("Environment", self.model)
        new_x = new_x % model.width
        new_y = new_y % model.height

        # Update position using Mesa space
        model.space.move_agent(self, (new_x, new_y))
