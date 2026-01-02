import random
from mesa import Model
from world.config import config
from mesa.space import ContinuousSpace
from agents.predator import Predator
from agents.prey import Prey
from agents.grass import Grass
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
        self.grass = []
        self._create_agents()
        self._create_grass()

    def _create_agents(self):
        """Creates initial population of predators and prey."""
        predators = self.population_manager.create_population(
            config.predator_count, Predator, self
        )
        prey = self.population_manager.create_population(config.prey_count, Prey, self)
        self.predators = predators
        self.prey = prey

    def _create_grass(self):
        """Creates grass clusters in the environment."""
        self.grass = []
        for _ in range(config.grass_cluster_count):
            # Random cluster center
            cluster_x = random.uniform(0, self.width)
            cluster_y = random.uniform(0, self.height)

            # Create grass patches in cluster
            for _ in range(config.grass_per_cluster):
                # Random position within cluster radius
                distance = random.uniform(0, config.grass_cluster_radius)
                x = cluster_x + distance * random.uniform(-1, 1)
                y = cluster_y + distance * random.uniform(-1, 1)

                # Wrap around toroidal world
                x = x % self.width
                y = y % self.height

                # Create grass patch
                grass = Grass(self, config.grass_energy_value)
                self.space.place_agent(grass, (x, y))
                self.grass.append(grass)

    def step(self) -> None:
        """Advance the model by one step."""
        # Update all agents (let them act)
        for predator in self.predators:
            if predator.is_alive():
                predator.act()
                # Passive energy drain
                if predator.properties is not None:
                    predator.properties.energy -= config.passive_energy_drain
                    predator.properties.age += 1

        for prey in self.prey:
            if prey.is_alive():
                prey.act()
                # Passive energy drain
                if prey.properties is not None:
                    prey.properties.energy -= config.passive_energy_drain
                    prey.properties.age += 1

        # Remove dead agents
        self._remove_dead_agents()

        # Respawn grass
        self._respawn_grass()

    def _remove_dead_agents(self) -> None:
        """Remove dead agents from the simulation."""
        # Remove dead predators
        dead_predators = [p for p in self.predators if not p.is_alive()]
        for predator in dead_predators:
            self.predators.remove(predator)
            self.space.remove_agent(predator)

        # Remove dead prey
        dead_prey = [p for p in self.prey if not p.is_alive()]
        for prey in dead_prey:
            self.prey.remove(prey)
            self.space.remove_agent(prey)

        # Remove eaten grass
        eaten_grass = [g for g in self.grass if g.eaten]
        for grass in eaten_grass:
            self.grass.remove(grass)
            self.space.remove_agent(grass)

    def _respawn_grass(self) -> None:
        """Respawn some grass patches randomly."""
        # Respawn in existing clusters
        for _ in range(config.grass_cluster_count):
            if random.random() < config.grass_respawn_rate:
                # Find a random position near existing grass or random
                if self.grass:
                    # Respawn near existing grass
                    existing_grass = random.choice(self.grass)
                    if existing_grass.pos is not None:
                        base_x, base_y = existing_grass.pos
                    else:
                        base_x = random.uniform(0, self.width)
                        base_y = random.uniform(0, self.height)
                else:
                    # Random position if no grass exists
                    base_x = random.uniform(0, self.width)
                    base_y = random.uniform(0, self.height)

                # Random position within small radius
                distance = random.uniform(0, config.grass_cluster_radius * 0.5)
                x = base_x + distance * random.uniform(-1, 1)
                y = base_y + distance * random.uniform(-1, 1)

                # Wrap around toroidal world
                x = x % self.width
                y = y % self.height

                # Create new grass patch
                grass = Grass(self, config.grass_energy_value)
                self.space.place_agent(grass, (x, y))
                self.grass.append(grass)
