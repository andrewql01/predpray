"""
Base strategy interface for agent actions.
"""

from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from agents.agent import BaseAgent


class ActionStrategy(Protocol):
    """
    Protocol for action strategies.
    Each agent type should implement its own strategy.
    """

    def act(self, agent: "BaseAgent") -> None:
        """
        Execute action for the agent.

        Args:
            agent: The agent to act for
        """
        ...
