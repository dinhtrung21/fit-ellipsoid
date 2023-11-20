from fitellipsoid import ellipsoid
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, beta

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
        Calculate the Euler angles from a given #D rotational matrix.
            Input:
                R : the rotational matrix
            Output:
                a, b, g : (improper) Euler angles from extrinsic rotation
    """
    a = np.arctan2(R[2][1], R[2][2])
    b = np.arctan2(-R[2][0], np.sqrt(R[2][1]**2 + R[2][2]**2))
    g = np.arctan2(R[1][0], R[0][0])
    return a, b, g