from fitellipsoid import ellipsoid, util
import numpy as np

## Input our parameters for size/shape distribution of each phases
mu       = [0.50, 0.91, -0.3, 0.81]
sigma    = [0.75, 0.57, 0.79, 0.80]
alpha    = [3.82, 3.54, 3.72, 3.08]
beta     = [2.99, 2.85, 3.24, 3.13]
fraction = [1, 1, 1, 1]

## RVE constants, including dimensions and resolution
dim = 100
res = 0.2

## Number of RVEs for evaluation
n = 5

## Loop through each RVE
for i in range(1, n + 1):
    data_path = f'data/{i}/QP_FFT_data.txt'
    d, a = ellipsoid.fitRVE(data_path, res)
    util.mkdr(i)
    util.graph_plot(d, a, i, mu, sigma, alpha, beta)