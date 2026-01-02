from utils.singleton import Singleton


class SimulationConfig(metaclass=Singleton):
    """
    Simple simulation configuration class with basic parameters.
    Singleton pattern - only one instance exists.
    """

    def __init__(self):
        # World dimensions
        self.world_width: int = 800
        self.world_height: int = 600

        # Initial population sizes
        self.predator_count: int = 20
        self.prey_count: int = 50

        # Agent speeds
        self.predator_speed: float = 2.0
        self.prey_speed: float = 1.5

        # Agent energy
        self.predator_max_energy: float = 100.0
        self.prey_max_energy: float = 50.0

        # Network architecture
        self.network_input_size: int = 8
        self.network_hidden_size: int = 16
        self.network_output_size: int = 3

        # Visibility
        self.view_range: float = 100.0

        # Combat/Interaction settings
        self.attack_range: float = 15.0  # Distance to attack/kill
        self.hunting_energy_cost: float = 0.5  # Energy cost per step when hunting
        self.fleeing_energy_cost: float = 0.3  # Energy cost per step when fleeing
        self.kill_energy_cost: float = 50.0  # Energy removed from prey when killed
        self.kill_energy_reward: float = 30.0  # Energy gained by predator when killing
        self.passive_energy_drain: float = 0.1  # Energy lost per step just for existing

        # Simulation settings
        self.fps: int = 60

        # Grass settings
        self.grass_cluster_count: int = 15  # Number of grass clusters
        self.grass_per_cluster: int = 20  # Number of grass patches per cluster
        self.grass_cluster_radius: float = 50.0  # Radius of grass cluster
        self.grass_energy_value: float = 5.0  # Energy gained by prey when eating grass
        self.grass_respawn_rate: float = (
            0.01  # Probability of grass respawning per step
        )

        # Agent visual appearance configuration
        self.predator_portrayal: dict = {"color": "red", "shape": "circle", "size": 10}
        self.prey_portrayal: dict = {"color": "blue", "shape": "circle", "size": 6}
        self.grass_portrayal: dict = {"color": "green", "shape": "circle", "size": 3}
        self.default_portrayal: dict = {"color": "gray", "shape": "circle", "size": 4}

        self._initialized = True


config = SimulationConfig()
