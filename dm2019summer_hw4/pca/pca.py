import numpy as np
import scipy as scipy
def PCA(data):
    '''
    PCA	Principal Component Analysis

    Input:
      data      - Data numpy array. Each row vector of fea is a data point.
    Output:
      eigvector - Each column is an embedding function, for a new
                  data point (row vector) x,  y = x*eigvector
                  will be the embedding result of x.
      eigvalue  - The sorted eigvalue of PCA eigen-problem.
    '''

    # YOUR CODE HERE
    # Hint: you may need to normalize the data before applying PCA
    # begin answer
    n, p = np.shape(data)
    data_mean = np.mean(data, axis=0)
    data_minus = data - np.tile(data_mean,(n,1))
    S = np.dot(data_minus.T, data_minus)
    eigvalue,eigvector = scipy.sparse.linalg.eigs(S, k = 2, which = 'LM')
    eigvalue = np.diag(eigvalue)
    # end answer