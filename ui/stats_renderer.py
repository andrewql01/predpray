"""
Renderer for displaying simulation statistics on screen.
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from world.environment import Environment


class StatsRenderer:
    """Renders simulation statistics on the pygame screen."""

    def __init__(self, environment: "Environment", font_size: int = 16):
        """Initialize the stats renderer."""
        self.environment = environment
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        self.text_color = (0, 0, 0)  # Black text
        self.bg_color = (255, 255, 255, 200)  # Semi-transparent white background
        self.padding = 10
        self.line_height = 20

    def render(self, screen: pygame.Surface) -> None:
        """Render statistics on the screen."""
        if screen is None:
            return

        stats = self._collect_stats()
        lines = self._format_stats(stats)

        # Calculate background rectangle
        max_width = max(len(line) * 8 for line in lines) if lines else 200
        bg_height = len(lines) * self.line_height + self.padding * 2
        bg_rect = pygame.Rect(self.padding, self.padding, max_width, bg_height)

        # Draw semi-transparent background
        bg_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        bg_surface.fill(self.bg_color)
        screen.blit(bg_surface, bg_rect)

        # Draw text lines
        y_offset = self.padding + 5
        for line in lines:
            text_surface = self.font.render(line, True, self.text_color)
            screen.blit(text_surface, (self.padding + 5, y_offset))
            y_offset += self.line_height

    def _collect_stats(self) -> dict:
        """Collect statistics from the environment."""
        stats = {
            "predators": len(self.environment.predators),
            "prey": len(self.environment.prey),
            "grass": len([g for g in self.environment.grass if g.is_available()]),
        }

        # Best fitness
        alive_predators = [
            p for p in self.environment.predators if p.is_alive() and p.properties
        ]
        if alive_predators:
            best_predator = max(alive_predators, key=lambda a: a.fitness)
            stats["best_predator_fitness"] = best_predator.fitness

        alive_prey = [p for p in self.environment.prey if p.is_alive() and p.properties]
        if alive_prey:
            best_prey = max(alive_prey, key=lambda a: a.fitness)
            stats["best_prey_fitness"] = best_prey.fitness

        # Average energy
        alive_predators = [
            p for p in self.environment.predators if p.is_alive() and p.properties
        ]
        if alive_predators:
            avg_predator_energy = sum(p.energy for p in alive_predators) / len(
                alive_predators
            )
            stats["avg_predator_energy"] = avg_predator_energy

        alive_prey = [p for p in self.environment.prey if p.is_alive() and p.properties]
        if alive_prey:
            avg_prey_energy = sum(p.energy for p in alive_prey) / len(alive_prey)
            stats["avg_prey_energy"] = avg_prey_energy

        return stats

    def _format_stats(self, stats: dict) -> list[str]:
        """Format statistics as text lines."""
        lines = []

        # Population counts
        lines.append(f"Predators: {stats['predators']}")
        lines.append(f"Prey: {stats['prey']}")
        lines.append(f"Grass: {stats['grass']}")

        # Energy stats
        if "avg_predator_energy" in stats:
            lines.append(f"Avg Predator Energy: {stats['avg_predator_energy']:.1f}")
        if "avg_prey_energy" in stats:
            lines.append(f"Avg Prey Energy: {stats['avg_prey_energy']:.1f}")

        # Fitness stats
        if "best_predator_fitness" in stats:
            lines.append(f"Best Predator Fitness: {stats['best_predator_fitness']:.1f}")
        if "best_prey_fitness" in stats:
            lines.append(f"Best Prey Fitness: {stats['best_prey_fitness']:.1f}")

        return lines
