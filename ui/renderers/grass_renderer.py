"""
Grass renderer for pygame visualization.
"""

import pygame
from ui.renderers.base_renderer import BaseRenderer
from ui.color_manager import ColorManager
from world.config import config


class GrassRenderer(BaseRenderer):
    """
    Renders grass agents on the screen.
    """

    def __init__(self, model):
        """Initialize the grass renderer."""
        self.model = model
        self.color_manager = ColorManager()
        self.size = config.grass_portrayal["size"]

    def render(self, screen):
        """Render all grass agents."""
        for grass in self.model.grass:
            if not grass.is_available() or grass.pos is None:
                continue

            x, y = grass.pos
            color = self.color_manager.color_string_to_rgb(
                config.grass_portrayal["color"]
            )
            pygame.draw.circle(screen, color, (int(x), int(y)), self.size)
