import torch
import torch.nn as nn

class AgentNetwork(nn.Module):
    """
    Simple MLP network for agent control.
    """
    
    def __init__(self, input_size: int, hidden_size: int, output_size: int) -> None:
        super().__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, output_size)
        self.l3 = nn.Linear(output_size, output_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.relu(self.l1(x))
        x = torch.relu(self.l2(x))
        output = self.l3(x)

        dx_dy = torch.tanh(output[..., :2])
        intensity = torch.sigmoid(output[..., 2:3])

        return torch.cat([dx_dy, intensity], dim=-1)
    
    def get_weights(self) -> dict:
        return self.state_dict()
    
    def set_weights(self, weights: dict) -> None:
        self.load_state_dict(weights)
    
    def mutate(self, mutation_rate=0.1: float) -> AgentNetwork:
        instance = AgentNetwork(
            self.input_size, 
            self.hidden_size, 
            self.output_size
        )

        with torch.no_grad():
            for (name, param), (instance_name, instance_param) 
            in zip(self.named_parameters(), instance.named_parameters()):
                noise = torch.randn_like(param) * mutation_rate
                instance_param.data = param.data + noise

        return instance