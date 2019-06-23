import numpy as np
import matplotlib.pyplot as plt
from pca import PCA as pca

def hack_pca(filename):
    '''
    Input: filename -- input image file name/path
    Output: img -- image without rotation
    '''
    img_r = (plt.imread(filename)).astype(np.float64)
    

    img = img_r[:,:,1]# - img_r[:,:,3]
    n, p = img.shape
    plt.imshow(img)
    set
    for i in range(n):
        for j in range(p):
            if(img[i][j] > 0):
                print(img[i][j])

   
   

    # YOUR CODE HERE
    # begin answer
    # end answer