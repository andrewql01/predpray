import torch.nn as nn

from enum import Enum
from agent_properties import AgentProperties
from network import AgentNetwork
from world.environment import Environment

class AgentType(Enum):
    """Agent type enum - for verification purposes"""
    PREDATOR = "predator"
    PREY = "prey"

class Agent:
    """ 
    Agent class used for simulation
    """

    def __init__(self, network: AgentNetwork, environment: Environment, agent_properties: AgentProperties) -> None:
        self.network = network
        self.environment = environment
        self.agent_properties = agent_properties
    
    @property
    def is_predator(self) -> bool:
        return self.agent_type == AgentType.PREDATOR


    @property
    def agent_type(self) -> AgentType:
        raise NotImplementedError("Subclasses must implement agent_type")

    def act():
        """
        Make the agent act in the environment by taking an action based on the observation.
        """
        pass
