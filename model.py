import math

import  torch.nn.functional as F
from torch import nn

class Generator(nn.Module):
    def __init__(self, scale_factor):


class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__():
            self.conv1 = nn.Conv2(channels, channels, kernel_size=3, )