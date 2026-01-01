"""
Population manager for creating and managing agent populations.
"""

import random
from typing import Type, List
from mesa.space import ContinuousSpace
from agents.agent import PredatorPreyAgent


class PopulationManager:
    """
    Manages agent population creation and placement in the continuous space.
    """

    def __init__(
        self,
        space: ContinuousSpace,
        world_width: float,
        world_height: float,
    ):
        """
        Initialize the population manager.
        """
        self.space = space
        self.world_width = world_width
        self.world_height = world_height

    def create_agent_at_random_position(
        self, entity_class: Type[PredatorPreyAgent], model
    ) -> PredatorPreyAgent:
        """
        Create a single agent at a random position.
        """
        pos = (
            random.uniform(0, self.world_width),
            random.uniform(0, self.world_height),
        )
        entity = entity_class(model)
        self.space.place_agent(entity, pos)
        return entity

    def create_population(
        self, population_size: int, entity_class: Type[PredatorPreyAgent], model
    ) -> List[PredatorPreyAgent]:
        """
        Create a population of agents.
        """
        return [
            self.create_agent_at_random_position(entity_class, model)
            for _ in range(population_size)
        ]

    def create_agent_at_position(
        self, entity_class: Type[PredatorPreyAgent], model, x: float, y: float
    ) -> PredatorPreyAgent:
        """
        Create an agent at a specific position.
        """
        pos = (x, y)
        entity = entity_class(model)
        self.space.place_agent(entity, pos)
        return entity
