from ui.color_manager import ColorManager
from ui.renderers.base_renderer import BaseRenderer
from world.config import config
import pygame


class PredatorRenderer(BaseRenderer):
    """Renderer for predators."""

    def __init__(self, model):
        """Initialize the predator renderer."""
        self.model = model
        self.color_manager = ColorManager()
        self.size = config.predator_portrayal["size"]

    def render(self, screen):
        """Render the predators."""
        if screen is None:
            return

        for agent in self.model.predators:
            color = self.color_manager.get_agent_color(agent.properties)
            x, y = agent.pos
            pygame.draw.circle(screen, color, (int(x), int(y)), self.size)
