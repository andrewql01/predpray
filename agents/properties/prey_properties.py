from dataclasses import dataclass
from agents.properties.agent_properties import AgentProperties


@dataclass
class PreyProperties(AgentProperties):
    """
    Prey-specific properties.
    """

    # Prey-specific properties can be added here
    # For example: escape_success_rate, food_found, etc.
    pass
