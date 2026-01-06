"""
Predator agent class.
"""

from typing import Optional, TYPE_CHECKING, cast
from agents.agent import BaseAgent
from agents.network import AgentNetwork
from world.config import config
from agents.properties.predator_properties import PredatorProperties

if TYPE_CHECKING:
    from world.environment import Environment


class Predator(BaseAgent):
    """
    Predator agent - hunts prey.
    """

    def __init__(self, model: "Environment", network: Optional[AgentNetwork] = None):
        """Initialize the predator."""
        properties = PredatorProperties(
            energy=config.predator_max_energy,
            max_energy=config.predator_max_energy,
            speed=config.predator_speed,
        )
        super().__init__(model, properties=properties, network=network)
        self.min_energy_to_hunt = 0.2  # Minimum 20% energy to hunt

    def _find_nearest_prey(self):
        """Find nearest prey within view range."""
        # self.model is always Environment in runtime
        model = cast("Environment", self.model)
        return self._find_nearest_agent(model.prey)

    def act(self):
        """Predator behavior - hunt nearest prey or wander randomly."""
        if self.properties is None or not self.is_alive():
            return

        # Check if has enough energy to hunt
        energy_ratio = self.properties.energy_ratio()
        has_energy = energy_ratio >= self.min_energy_to_hunt

        if has_energy:
            # Try to find and hunt nearest prey
            nearest_prey = self._find_nearest_prey()
            if nearest_prey is not None:
                # Hunt the prey
                self.move_towards(nearest_prey.pos)
                # Cost for hunting
                self.properties.energy -= config.hunting_energy_cost
                # Attack/kill logic when close enough
                if self._distance_to(nearest_prey.pos) < config.attack_range:
                    nearest_prey.properties.energy -= config.kill_energy_cost
                    self.properties.energy += config.kill_energy_reward
                    # Increase fitness for successful kill
                    self.properties.fitness += 10.0
                return

        # If no prey in range or not enough energy, wander randomly
        self._random_move()
