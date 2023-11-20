from fitellipsoid import ellipsoid, util
import numpy as np

## Input our parameters for size/shape distribution of each phases
mu       = [1, 1, 1, 1]
sigma    = [1, 1, 1, 1]
alpha    = [1, 1, 1, 1]
beta     = [1, 1, 1, 1]
fraction = [1, 1, 1, 1]

## RVE constants, including dimensions and resolution
dim = 100
res = 0.2