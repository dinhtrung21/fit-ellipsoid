import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, beta

def mkdr(ind):
    try:
        os.mkdir(f'result/{ind}')
    except FileExistsError:
        print(f'Directory result/{ind} already exists. Enter new RVE number or hit enter to overwrite.')
        new = input()
        if new == '':
            return f'result/{ind}'
        else:
            mkdr(input)
            return f'result/{input}'



def plot_ellipsoid(mu_x, mu_y, mu_z, L, R):
    """
        Returns an array of points on the quadric surface of the ellipsoid we want to plot.
            Input:
                mu_x, mu_y, mu_z : the center of our ellipsoid
                L                : an array containing the length of the semi-axes of our ellipsoid
                R                : the rotational matrix
            Output:
                ellipsoid : an array of points on the surface of the ellipsoid 
    """
    ## Pre-transformed center
    mu_ = np.transpose(R) @ [mu_x, mu_y, mu_z]
    ellipsoid = []
    for i in range(0,100000):                               # Here, the size of our array is 100000
        x, y, z = np.random.uniform(-1, 1, 3)               # Simulate points on a sphere
        [x, y, z] = [x, y, z]/np.sqrt(x**2 + y**2 + z**2)   # Transform into an ellipsoid
        [x, y, z] = [x, y, z] * L + mu_
        p = R @ [x, y, z]                                   # Rotate the ellipsoid
        ellipsoid += [p]                                    # Add the point into the array
    ## Return the array
    return ellipsoid


def euler_angles(R):
    """
        Calculate the Euler angles from a given 3D rotational matrix.
            Input:
                R : the rotational matrix
            Output:
                a, b, g : (improper) Euler angles from extrinsic rotation
    """
    a = np.arctan2(R[2][1], R[2][2])
    b = np.arctan2(-R[2][0], np.sqrt(R[2][1]**2 + R[2][2]**2))
    g = np.arctan2(R[1][0], R[0][0])
    return a, b, g


def hellinger_lognorm(mu_1, mu_2, sigma_1, sigma_2):
    """
        Calculate the Hellinger distance of the lognormal size distribution.
            Input:
                mu_1, sigma_1 : parameters of the experimental distribution
                mu_2, sigma_2 : parameters of the RVE-generated distribution
            Output:
                H : Hellinger distance
    """
    H = np.sqrt(1 - np.sqrt(2*sigma_1*sigma_2/(sigma_1**2 + sigma_2**2))*np.exp(-1/4 * (mu_1 - mu_2)**2/(sigma_1**2 + sigma_2**2)))
    return H


def graph_plot(d, a, ind, mu, sigma, ap, be):
    """
        Simple plotter for all the different phases of size and shape distribution in the grains of an RVE
            Input:
                d, a     :  size and shape dictionaries with phase ID as key and the corresponding distribution as value
                ind      :  index of our RVE
                mu, sigma:  size experimental distribution parameter of each phase
                ap, be   :  shape experimental distribution parameter of each phase
    """
    fig, axes = plt.subplots(4, 2, figsize=(15,20))
    for i in range(4):
        ## Plot the RVE equivalent diameter distribution
        axes[i, 0].hist(d[i+1], color='g', bins=np.linspace(0, max(d[i+1]), 50), alpha=0.5, density=True)
        axes[i, 0].plot(np.linspace(min(d[i+1]), max(d[i+1]), 50), lognorm.pdf(np.linspace(min(d[i+1]), max(d[i+1]), 50), sigma[i], scale=np.exp(mu[i])), 
                    'r-', lw=2, label='Experimental distribution')
        axes[i, 0].set_xlabel("Equivalent diameter")
        axes[i, 0].set_ylabel("Density")
        axes[i, 0].set_title(f"Phase {i+1} - RVE equivalent diameter distribution")
        axes[i, 0].legend()
        ## Plot the RVE grain aspect ratio distribution
        axes[i, 1].hist(a[i+1], color='g', bins=np.linspace(0, 1, 50), alpha=0.5, density=True)
        axes[i, 1].plot(np.linspace(min(a[i+1]), max(a[i+1]), 50), beta.pdf(np.linspace(min(a[i+1]), max(a[i+1]), 50), ap[i], be[i]), 
                    'r-', lw=2, label='Experimental distribution')
        axes[i, 1].set_xlabel("Grain aspect ratio")
        axes[i, 1].set_ylabel("Density")
        axes[i, 1].set_title(f"Phase {i+1} - RVE grain aspect ratio distribution")
        axes[i, 1].legend()
    plt.savefig(f'result/{ind}/Distribution of RVE.png')
    plt.close()

