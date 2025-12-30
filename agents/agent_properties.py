from dataclasses import dataclass


@dataclass
class AgentProperties:
    """
    Agent properties class
    """

    x: float
    y: float

    energy: float
    max_energy: float

    speed: float

    age: int = 0
    fitness: float = 0.0
    reproduction_cooldown: int = 0

    def energy_ratio(self) -> float:
        """Returns energy ratio (0.0 - 1.0)"""
        raise NotImplementedError

    def can_reproduce(self, min_energy_ratio: float = 0.7, min_age: int = 50) -> bool:
        """Check if agent can reproduce"""
        raise NotImplementedError

    def is_alive(self) -> bool:
        """Check if agent is alive (has energy)."""
        raise NotImplementedError
