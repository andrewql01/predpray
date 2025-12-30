"""
Main entry point for the predator-prey simulation using pygame visualization.

To run this simulation, use:
    python main.py
"""

from ui.simulation import Simulation


def main():
    """Main entry point."""
    # Create and run the simulation
    sim = Simulation()
    sim.run()


if __name__ == "__main__":
    main()
