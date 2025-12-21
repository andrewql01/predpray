from dataclasses import dataclass
from typing import Tuple

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
        return self.energy / self.max_energy if self.max_energy > 0 else 0.0
    
    def can_reproduce(self, min_energy_ratio: float = 0.7, min_age: int = 50) -> bool:
        """Check if agent can reproduce"""
        return (
            self.energy_ratio() > min_energy_ratio and
            self.age > min_age and
            self.reproduction_cooldown == 0
        )
    
    def is_alive(self) -> bool:
        """Check if agent is alive (has energy)."""
        return self.energy > 0