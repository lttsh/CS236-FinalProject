"""
Image grid saver, based on color_grid_vis from github.com/Newmu
"""

import numpy as np
import scipy.misc
from scipy.misc import imsave

def save_images(X, save_path, rows):
    print(X.shape)
    # [0, 1] -> [0,255]
    if isinstance(X.flatten()[0], np.floating):
        X = (255.99*X).astype('uint8')

    nh, nw = rows, int(X.shape[0] / rows)

    if X.ndim == 2:
        X = np.reshape(X, (X.shape[0], int(np.sqrt(X.shape[1])), int(np.sqrt(X.shape[1]))))

    if X.ndim == 4:
        # BCHW -> BHWC
        X = X.transpose(0, 2, 3, 1)
        h, w = X[0].shape[:2]
        img = np.zeros((h * nh, w * nw, 3))
    elif X.ndim == 3:
        h, w = X[0].shape[:2]
        img = np.zeros((int(h*nh),int(w*nw)))
    for n, x in enumerate(X):
        j = int(n/nh)
        i = int(n%nh)
#        print(i,j, h, w)
        img[i*h:i*h+h, j*w:j*w+w] = x

    imsave(save_path, img)
