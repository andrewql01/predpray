"""
Predator-specific action strategy.
"""

from typing import TYPE_CHECKING
from world.config import config

if TYPE_CHECKING:
    from agents.agent import BaseAgent


class PredatorStrategy:
    """
    Strategy implementation for predator agents.
    """

    def act(self, agent: "BaseAgent") -> None:
        """Execute predator-specific action."""
        if agent.properties is None or not agent.is_alive():
            return

        # Check if has enough energy to hunt
        energy_ratio = agent.properties.energy_ratio()
        min_energy_to_hunt = getattr(agent, "min_energy_to_hunt", 0.2)
        has_energy = energy_ratio >= min_energy_to_hunt

        if has_energy:
            # Try to find and hunt nearest prey
            nearest_prey = agent._find_nearest_prey()  # type: ignore[attr-defined]
            if nearest_prey is not None and nearest_prey.pos is not None:
                # Hunt the prey
                agent.move_towards(nearest_prey.pos)
                # Cost for hunting
                agent.properties.energy -= config.hunting_energy_cost
                # Attack/kill logic when close enough
                if agent._distance_to(nearest_prey.pos) < config.attack_range:
                    if nearest_prey.properties is not None:
                        nearest_prey.properties.energy -= config.kill_energy_cost
                        # Big penalty for being eaten - encourages prey to avoid predators
                        if nearest_prey.properties.energy <= 0:
                            nearest_prey.properties.fitness += (
                                config.death_fitness_penalty
                            )
                    agent.properties.energy += config.kill_energy_reward
                    # Increase fitness for successful kill
                    agent.properties.fitness += 10.0
                return

        # If no prey in range or not enough energy, wander randomly
        agent._random_move()
