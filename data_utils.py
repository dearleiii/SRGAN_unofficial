from os import listdir
from os.path import join

from PIL import Image
from torch.utils.data.dataset import Dataset
import torchvision.transforms as transforms

def is_image_file(filename):
    return any(filename.endswith(extension) for extension in [".png", ".jpg", ".jpeg"])

def calculate_valid_crop_size(crop_size, upscale_factor):
    return crop_size - ()

def train_hr_transform(crop_size):
    return Compose([
        transforms.RandomCrop(crop_size),
        transforms.ToTensor(),
    ])

