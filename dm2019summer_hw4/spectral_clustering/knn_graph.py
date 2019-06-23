import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

def knn_graph(X, k, threshold):
    '''
    KNN_GRAPH Construct W using KNN graph

        Input:
            X - data point features, n-by-p maxtirx.
            k - number of nn.
            threshold - distance threshold.

        Output:
            W - adjacency matrix, n-by-n matrix.
    '''

    # YOUR CODE HERE
    # begin answer
    n, p = np.shape(X)
    W = np.zeros((n, n))
    Dist = np.zeros((n, n))
    


    distA=pdist(X,metric='euclidean')
    # 将distA数组变成一个矩阵
    Dist = squareform(distA)
  
      
    for i in range(n):
        dis = Dist[i].argsort()
        for j in range(k):
            if(Dist[i][dis[j]] < threshold):
                W[i][dis[j]] = 1
                W[dis[j]][i] = 1
        W[i][i] = 0
    
    return W  
    # end answer
