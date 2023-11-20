import numpy as np

def preprocess(data):
    """
        Process input data into usable arrays for calculation of best-fitted ellipsoid
        Input:
            data: data path
        Output:
            RVE     : dictionaries of RVE coordinates
            vertices: dictionaries of voxels' vertices
            phases  : dictionaries of voxels' phases
    """
    ## Dictionaries to return
    RVE      = {}
    vertices = {}
    phases   = {}

    file_open = open(data, 'r')
    ## Fill in the RVE dictionaries
    for line in file_open:
        line_split = line.split(" ")
        grainID = int(line_split[-2])
        if grainID in RVE:
            RVE[grainID].append([int(line_split[3]), int(line_split[4]), int(line_split[5]), int(line_split[-1])])
        else:
            RVE[grainID] = [[int(line_split[3]), int(line_split[4]), int(line_split[5]), int(line_split[-1])]]
    
    ## Fill in the vertices & phases dictionaries
    for i in RVE:
        x, y, z, phase = np.transpose(RVE[i])
        u = np.transpose([x, y, z])
        u = np.append(u, np.transpose([x, y, z]) - [1, 0, 0], axis=0)
        u = np.append(u, np.transpose([x, y, z]) - [0, 1, 0], axis=0)
        u = np.append(u, np.transpose([x, y, z]) - [0, 0, 1], axis=0)
        u = np.append(u, np.transpose([x, y, z]) - [1, 1, 0], axis=0)
        u = np.append(u, np.transpose([x, y, z]) - [1, 0, 1], axis=0)
        u = np.append(u, np.transpose([x, y, z]) - [0, 1, 1], axis=0)
        u = np.append(u, np.transpose([x, y, z]) - [1, 1, 1], axis=0)
        vertices[i] = np.unique(u, axis=0)
        phases[i]   = phase[0]

    ## Return the preprocessed data
    return RVE, vertices, phases
