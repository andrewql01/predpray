"""
Main entry point for the predator-prey simulation.
"""

from world.environment import Environment
from ui.visualization import SimulationVisualizer


def main():
    """Main function to run the simulation visualization."""
    # Create environment
    env = Environment()
    
    # Initialize grid
    env._update_spatial_grid()
    
    # Create and run visualizer
    visualizer = SimulationVisualizer(env)
    visualizer.run()


if __name__ == "__main__":
    main()
