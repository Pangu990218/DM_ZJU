import numpy as np
from kmeans import kmeans as kmeans


def spectral(W, k):
    '''
    SPECTRUAL spectral clustering

        Input:
            W: Adjacency matrix, N-by-N matrix
            k: number of clusters

        Output:
            idx: data point cluster labels, n-by-1 vector.
    '''
    # YOUR CODE HERE
    n, n = np.shape(W)
    idx = np.zeros((n ,1))
    D = np.zeros((n, n))
    
    for i in range(n):
        D[i][i] = np.sum(W[i][:])
    L = D - W
    # begin answer
    eng = np.linalg.eig(L)
    enval = eng[0]
    en = eng[1]
    sort_index = np.argsort(enval)
    topk = en[:,sort_index[:k]]
    idx = kmeans(topk, k)
    
    return idx
    # end answer
