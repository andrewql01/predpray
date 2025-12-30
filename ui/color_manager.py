"""
Color manager class for handling color conversions and management.
"""

COLOR_MAP = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "gray": (128, 128, 128),
    "green": (0, 255, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}


class ColorManager:
    """
    Manages color conversions and color-related operations.
    """

    def __init__(self):
        """Initialize the color manager."""
        pass

    def _color_string_to_rgb(self, color_str: str) -> tuple:
        """Convert color string to RGB tuple."""
        return COLOR_MAP.get(color_str.lower(), (128, 128, 128))

    def get_agent_color(self, agent_type: str) -> tuple:
        """Get the color for a specific agent type."""
        return self._color_string_to_rgb(agent_type)
