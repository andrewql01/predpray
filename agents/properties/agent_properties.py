from dataclasses import dataclass
from abc import ABC


@dataclass
class AgentProperties(ABC):
    """
    Base agent properties class with common properties.
    """

    energy: float
    max_energy: float

    speed: float

    age: int = 0
    fitness: float = 0.0
    reproduction_cooldown: int = 0

    @property
    def agent_type(self) -> str:
        """Returns the agent type based on the class name."""
        class_name = self.__class__.__name__
        if "Predator" in class_name:
            return "predator"
        elif "Prey" in class_name:
            return "prey"
        return "unknown"

    def energy_ratio(self) -> float:
        """Returns energy ratio (0.0 - 1.0)"""
        if self.max_energy == 0:
            return 0.0
        return self.energy / self.max_energy

    def can_reproduce(self, min_energy_ratio: float = 0.7, min_age: int = 50) -> bool:
        """Check if agent can reproduce"""
        return (
            self.energy_ratio() >= min_energy_ratio
            and self.age >= min_age
            and self.reproduction_cooldown <= 0
        )

    def is_alive(self) -> bool:
        """Check if agent is alive (has energy)."""
        return self.energy > 0
