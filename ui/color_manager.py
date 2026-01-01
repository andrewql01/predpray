from typing import Optional
from utils.singleton import Singleton
from agents.properties.agent_properties import AgentProperties
from world.config import config

COLOR_MAP = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "gray": (128, 128, 128),
    "green": (0, 255, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}


class ColorManager(metaclass=Singleton):
    """
    Manages color conversions and color-related operations.
    """

    def color_string_to_rgb(self, color_str: str) -> tuple:
        """Convert color string to RGB tuple."""
        return COLOR_MAP.get(color_str.lower(), (128, 128, 128))

    def get_agent_color(
        self, agent_properties: Optional[AgentProperties] = None
    ) -> tuple:
        """Get the color for an agent based on its properties."""
        if agent_properties is None:
            return self.color_string_to_rgb("gray")

        agent_type = agent_properties.agent_type

        # Map agent type to color from config
        if agent_type == "predator":
            color_name = config.predator_portrayal["color"]
        elif agent_type == "prey":
            color_name = config.prey_portrayal["color"]
        else:
            color_name = config.default_portrayal["color"]

        base_color = self.color_string_to_rgb(color_name)

        # TODO: Add dynamic coloring based on properties here

        return base_color
