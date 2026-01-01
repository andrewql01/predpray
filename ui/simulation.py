"""
Simulation class for pygame-based visualization of the predator-prey simulation.
"""

import sys
import pygame
from ui.color_manager import ColorManager
from ui.renderers.prey_renderer import PreyRenderer
from ui.renderers.predator_renderer import PredatorRenderer
from world.config import config
from world.environment import Environment


class Simulation:
    """
    Simulation class that manages the pygame visualization and game loop.
    """

    def __init__(self):
        """Initialize the simulation."""
        self.width = config.world_width
        self.height = config.world_height
        self.fps = config.fps

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Predator-Prey Simulation")
        self.clock = pygame.time.Clock()

        self.environment = Environment()
        self.prey_renderer = PreyRenderer(self.environment)
        self.predator_renderer = PredatorRenderer(self.environment)
        self.color_manager = ColorManager()

        self.running = True

    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self):
        """Draw the current state of the simulation."""
        self.screen.fill((255, 255, 255))  # White background

        self.prey_renderer.render(self.screen)
        self.predator_renderer.render(self.screen)

        pygame.display.flip()

    def update(self):
        """Update the simulation state."""
        self.environment.step()  # type: ignore[call-arg]

    def run(self):
        """Run the simulation main loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        self.quit()

    def quit(self):
        """Clean up and quit pygame."""
        pygame.quit()
        sys.exit()
