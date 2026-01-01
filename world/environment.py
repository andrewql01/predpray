from mesa import Model
from world.config import config
from mesa.space import ContinuousSpace
from agents.predator import Predator
from agents.prey import Prey
from world.population_manager import PopulationManager


class Environment(Model):
    """
    Environment managing the 2D toroidal world and all agents using Mesa.
    """

    def __init__(self):
        """Initialize the environment."""
        super().__init__()
        self.width = config.world_width
        self.height = config.world_height

        self.space = ContinuousSpace(self.width, self.height, torus=True)

        # Population manager
        self.population_manager = PopulationManager(
            space=self.space, world_width=self.width, world_height=self.height
        )

        self.predators = []
        self.prey = []
        self._create_agents()

    def _create_agents(self):
        """Creates initial population of predators and prey."""
        predators = self.population_manager.create_population(
            config.predator_count, Predator, self
        )
        prey = self.population_manager.create_population(config.prey_count, Prey, self)
        self.predators = predators
        self.prey = prey

    def step(self) -> None:
        """Advance the model by one step."""
        pass
