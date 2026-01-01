import pygame
from ui.renderers.base_renderer import BaseRenderer
from ui.color_manager import ColorManager
from world.config import config


class PreyRenderer(BaseRenderer):
    """Renderer for prey."""

    def __init__(self, model):
        """Initialize the prey renderer."""
        self.model = model
        self.color_manager = ColorManager()
        self.size = config.prey_portrayal["size"]

    def render(self, screen):
        """Render the prey."""
        if screen is None:
            return

        for agent in self.model.prey:
            color = self.color_manager.get_agent_color(agent.properties)
            x, y = agent.pos
            pygame.draw.circle(screen, color, (int(x), int(y)), self.size)
