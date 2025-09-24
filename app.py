import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import kagglehub

# Download latest version
path = kagglehub.dataset_download("hojjatk/mnist-dataset")

print("Path to dataset files:", path)