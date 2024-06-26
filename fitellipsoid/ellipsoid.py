from fitellipsoid import preprocessing
import numpy as np

def fitEllipsoid(id, RVE, vertices):
    """
        Returns the best-fitted ellipsoid to a 3D region defined by a set of voxels' vertices on xyz-coordinate.
            Input:
                id       : our grain ID
                RVE      : RVE dictionary from fitellipsoid/preprocessing
                vertices : vertices dictionary from fitellipsoid/preprocessing
            Output:
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
    
    ## Return the results
    return mu_x, mu_y, mu_z, Sigma, L, R


def fitPhase(RVE, vertices, phases, res):
    """
        Returns the size and shape distribution of the grains belong to each phase.
            Input:
                RVE      : RVE dictionary from fitellipsoid/preprocessing
                vertices : vertices dictionary from fitellipsoid/preprocessing
                phases   : phases dictionary from fitellipsoid/preprocessing
                res      : RVE resolution
            Output:
                d : size dictionary with phase ID as key and the corresponding distribution as value
                a : shape dictionary with phase ID as key and the corresponding distribution as value
    """
    ## Dictionaries of size and shape to return
    d = {}
    a = {}
    for id in RVE:
        mu_x, mu_y, mu_z, Sigma, L, R = fitEllipsoid(id, RVE, vertices)
        ## Only consider the ellipsoid if it is not a sphere
        if min(L)/max(L) < 1:
            ## Calculate equivalent diameter, scaled with the resolution
            if phases[id] in d:
                d[phases[id]].append(np.cbrt(np.prod(L)) * 2 * res)
            else:
                d[phases[id]] = [np.cbrt(np.prod(L)) * 2 * res]
            ## Calculate grain aspect ratio
            if phases[id] in a:
                a[phases[id]].append(min(L)/max(L))
            else:
                a[phases[id]] = [min(L)/max(L)]
    ## Return the dictionaries
    return d, a


def fitRVE(data, res):
    """
        Returns the size and shape distribution of the grains belong to each phase in an RVE.
        Input:
            data: data path
            res : RVE resolution
        Output:
            d : size dictionary with phase ID as key and the corresponding distribution as value
            a : shape dictionary with phase ID as key and the corresponding distribution as value
    """
    ## Extract data from data path
    RVE, vertices, phases = preprocessing.preprocess(data)
    ## Dictionaries of size and shape by phases
    d, a = fitPhase(RVE, vertices, phases, res)
    ## Return the results
    return d, a