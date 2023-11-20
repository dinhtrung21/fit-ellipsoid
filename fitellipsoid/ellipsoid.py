import numpy as np

def fitEllipsoid(id, RVE, vertices):
    """
        Returns the best-fitted ellipsoid to a 3D region defined by a set of voxels' vertices on xyz-coordinate.
        Input:
            id       : our grain ID
            RVE      : RVE dictionary from fitellipsoid/preprocessing
            vertices : vertices dictionary from fitellipsoid/preprocessing
        Output
            mu_x, mu_y, mu_z: the center of our ellipsoid
            Sigma           : a matrix such that inv(Sigma) define our quadric surface
            L               : an array containing the length of the semi-axes of our ellipsoid
            R               : the rotational matrix
    """
    ## Get the grain's vertices and volume
    A = np.transpose(vertices[id])
    n = np.shape(RVE[id])[0]

    ## Calculate the center of our ellipsoid
    mu_x = np.average(A[0])
    mu_y = np.average(A[1])
    mu_z = np.average(A[2])
    ## Define our quadric surface, which is equal to the dispersion matrix of our data
    Sigma = [[np.cov(A[0],A[0])[0][1], np.cov(A[0],A[1])[0][1], np.cov(A[0],A[2])[0][1]],
             [np.cov(A[1],A[0])[0][1], np.cov(A[1],A[1])[0][1], np.cov(A[1],A[2])[0][1]],
             [np.cov(A[2],A[0])[0][1], np.cov(A[2],A[1])[0][1], np.cov(A[2],A[2])[0][1]]]
    ## Extract the axes and the rotation matrix
    L, R = np.linalg.eig(Sigma)

    ## Scale the axes by volume
    scaling = np.cbrt(3*n/(4*np.pi*np.sqrt(np.prod(L))))
    L = np.sqrt(L) * scaling
    ## Correct the rotation matrix
    R = np.transpose(R)
    
    ## Return the results
    return mu_x, mu_y, mu_z, Sigma, L, R    