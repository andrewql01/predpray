"""
Prey-specific action strategy.
"""

from typing import TYPE_CHECKING, cast, Tuple
from world.config import config

if TYPE_CHECKING:
    from agents.agent import BaseAgent


class PreyStrategy:
    """
    Strategy implementation for prey agents.
    """

    def act(self, agent: "BaseAgent") -> None:
        """Execute prey-specific action."""
        if agent.properties is None or not agent.is_alive():
            return

        # Priority 1: Flee from predators
        nearest_predator = agent._find_nearest_predator()  # type: ignore[attr-defined]
        if nearest_predator is not None and nearest_predator.pos is not None:
            # Flee from the predator
            agent.move_away_from(nearest_predator.pos)
            # Cost for fleeing (less than hunting)
            agent.properties.energy -= config.fleeing_energy_cost
            return

        # Priority 2: Find and eat grass
        nearest_grass = agent._find_nearest_grass()  # type: ignore[attr-defined]
        if nearest_grass is not None and nearest_grass.pos is not None:
            # Type narrowing: pos is tuple when not None
            grass_pos = cast(Tuple[float, float], nearest_grass.pos)

            # Move towards grass
            agent.move_towards(grass_pos)

            # Eat grass if close enough
            if agent._distance_to(grass_pos) < 5.0:  # Eating range
                energy_gained = nearest_grass.eat()
                if agent.properties is not None:
                    agent.properties.energy = min(
                        agent.properties.energy + energy_gained,
                        agent.properties.max_energy,
                    )
                    # Increase fitness for eating grass
                    agent.properties.fitness += 1.0
            return

        # Priority 3: If no predator or grass, wander randomly
        agent._random_move()
