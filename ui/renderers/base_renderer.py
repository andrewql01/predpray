from typing import Protocol
import pygame


class BaseRenderer(Protocol):
    """Base renderer class."""

    def __init__(self, model):
        """Initialize the renderer."""
        pass

    def render(self, screen: pygame.Surface):
        """Render the model."""
        pass
