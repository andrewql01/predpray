"""
Population manager for creating and managing agent populations.
"""

import random
from typing import Type, List
from mesa.space import ContinuousSpace
from agents.agent import BaseAgent


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
        self, entity_class: Type[BaseAgent], model
    ) -> BaseAgent:
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
        self, population_size: int, entity_class: Type[BaseAgent], model
    ) -> List[BaseAgent]:
        """
        Create a population of agents.
        """
        return [
            self.create_agent_at_random_position(entity_class, model)
            for _ in range(population_size)
        ]

    def create_agent_at_position(
        self, entity_class: Type[BaseAgent], model, x: float, y: float
    ) -> BaseAgent:
        """
        Create an agent at a specific position.
        """
        pos = (x, y)
        entity = entity_class(model)
        self.space.place_agent(entity, pos)
        return entity
