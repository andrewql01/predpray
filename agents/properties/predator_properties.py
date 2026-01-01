from dataclasses import dataclass
from agents.properties.agent_properties import AgentProperties


@dataclass
class PredatorProperties(AgentProperties):
    """
    Predator-specific properties.
    """

    # Predator-specific properties can be added here
    # For example: hunting_success_rate, kill_count, etc.
    pass
