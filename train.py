import argparse
import os
from math import log10

import pandas as pd
import torch.optim as optim
import torch.utils.data

import pytorch_ssim
from loss import GeneratorLoss
from model import Generator, Discriminator

parser = argparse.ArgumentParser(description="Train super resolution models")
parser.add_argument('--crop_size', default=88, type=int, help='training image crop size')
parser.add_argument('--upscale_factor', default=4, choices=[2, 4, 8], type=int,
                    help='super resolution upscale factor')
parser.add_argument('--num_epoches', default=100, type=int, help='train epoch number')

opt = parser.parse_args()

CROP_SIZE = opt.crop_size
UPSCALE_FACTOR = opt.upscale_factor
NUM_EPOCHS = opt.num_epoches

