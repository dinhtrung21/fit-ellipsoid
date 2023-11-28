from fitellipsoid import ellipsoid, util
import numpy as np

## Input our parameters for size/shape distribution of each phases
mu       = [0.50, 0.91, -0.3, 0.81]
sigma    = [0.75, 0.57, 0.79, 0.80]
alpha    = [3.82, 3.54, 3.72, 3.08]
beta     = [2.99, 2.85, 3.24, 3.13]
fraction = [0.09, 0.08, 0.23, 0.45]

## RVE constants, including dimensions and resolution
dim = 64
res = 1

## Number of RVEs for evaluation
n = 10


## Function to automatically calculate the difference between the RVE and the experimental data
def RVE_difference(d, a):
    """
        Evaluate the difference between the RVE and the experimental data using the Hellinger distance.
            Input:
                d : size dictionary of the RVE
                a : shape dictionary of the RVE
            Output:
                H_d: total Hellinger distance of the size distribution
                H_a: total Hellinger distance of the shape distribution
                E : the differene between the RVE and the experimental data
    """
    ## Initialize the difference
    H_d = 0
    H_a = 0
    E   = 0
    ## Loop through each phase
    for i in d:
        ## Calculate the Hellinger distance of the size distribution
        mu_, sigma_ = util.fit_lognorm(d[i])
        H_d        += fraction[i-1] * util.hellinger_lognorm(mu_, mu[i-1], sigma_, sigma[i-1])/np.sum(fraction)
        ## Calculate the Hellinger distance of the shape distribution
        ap_, be_ = util.fit_beta(a[i])
        H_a     += fraction[i-1] * util.hellinger_beta(ap_, alpha[i-1], be_, beta[i-1])/np.sum(fraction)
        ## Calculate the difference
    E = (H_d + H_a)/2
    ## Return the difference
    return H_d, H_a, E


## Loop through each RVE
min_error = 1e10            # Initialize the minimum error
best_RVE  = 0               # Initialize the best RVE
for i in range(1, n + 1):
    data_path = f'data/{i}/QP_FFT_data.txt'
    d, a = ellipsoid.fitRVE(data_path, res)
    util.mkdr(i)
    util.graph_plot(d, a, i, mu, sigma, alpha, beta)
    ## Calculate the difference between the RVE and the experimental data
    H_d, H_a, E = RVE_difference(d, a)
    print(f'RVE #{i} has size error of {H_d}, shape error of {H_a}, average error is {E}.')
    ## Update the minimum error and the best RVE
    if E < min_error:
        min_error = E
        best_RVE  = i

## Print the best RVE
print(f'The best RVE is RVE #{best_RVE} with an error of {min_error}.')