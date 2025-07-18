import torch
import torch.nn as nn

class ContentRecommender(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim * 2, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, worker_feat, task_feat):
        x = torch.cat([worker_feat, task_feat], dim=1)
        return self.fc(x)
