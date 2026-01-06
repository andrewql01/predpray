"""
Prey agent class.
"""

from typing import Optional, TYPE_CHECKING, cast, Tuple
from agents.agent import BaseAgent
from agents.network import AgentNetwork
from agents.properties.prey_properties import PreyProperties
from agents.grass import Grass
from world.config import config

if TYPE_CHECKING:
    from world.environment import Environment


class Prey(BaseAgent):
    """
    Prey agent - flees from predators.
    """

    def __init__(self, model: "Environment", network: Optional[AgentNetwork] = None):
        """Initialize the prey."""
        properties = PreyProperties(
            energy=config.prey_max_energy,
            max_energy=config.prey_max_energy,
            speed=config.prey_speed,
        )
        super().__init__(model, properties=properties, network=network)

    def _find_nearest_predator(self):
        """Find nearest predator within view range."""
        # self.model is always Environment in runtime
        model = cast("Environment", self.model)
        return self._find_nearest_agent(model.predators)

    def _find_nearest_grass(self) -> Optional[Grass]:
        """Find nearest available grass within view range."""
        if self.pos is None:
            return None

        model = cast("Environment", self.model)
        nearest_grass = None
        min_distance = config.view_range

        for grass in model.grass:
            if not grass.is_available() or grass.pos is None:
                continue

            distance = self._distance_to(grass.pos)
            if distance < min_distance:
                min_distance = distance
                nearest_grass = grass

        return nearest_grass

    def act(self):
        """Prey behavior - flee from predators, eat grass, or wander randomly."""
        if self.properties is None or not self.is_alive():
            return

        # Priority 1: Flee from predators
        nearest_predator = self._find_nearest_predator()
        if nearest_predator is not None:
            # Flee from the predator
            self.move_away_from(nearest_predator.pos)
            # Cost for fleeing (less than hunting)
            self.properties.energy -= config.fleeing_energy_cost
            return

        # Priority 2: Find and eat grass
        nearest_grass = self._find_nearest_grass()
        if nearest_grass is not None and nearest_grass.pos is not None:
            # Type narrowing: pos is tuple when not None
            grass_pos = cast(Tuple[float, float], nearest_grass.pos)

            # Move towards grass
            self.move_towards(grass_pos)

            # Eat grass if close enough
            if self._distance_to(grass_pos) < 5.0:  # Eating range
                energy_gained = nearest_grass.eat()
                if self.properties is not None:
                    self.properties.energy = min(
                        self.properties.energy + energy_gained,
                        self.properties.max_energy,
                    )
            return

        # Priority 3: If no predator or grass, wander randomly
        self._random_move()
