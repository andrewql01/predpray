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

        # Simulation settings
        self.fps: int = 60

        # Agent visual appearance configuration
        self.predator_portrayal: dict = {"color": "red", "shape": "circle", "size": 10}
        self.prey_portrayal: dict = {"color": "blue", "shape": "circle", "size": 6}
        self.default_portrayal: dict = {"color": "gray", "shape": "circle", "size": 4}

        self._initialized = True


config = SimulationConfig()
