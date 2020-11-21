import numpy as np

from mds import *
from pca import *

import scipy.linalg as li


mat, zoo_type = get_data_matrix()
mat = center_matrix(mat)

u, s, vh = svd(mat)


s = li.diagsvd(s, *mat.shape)


eye1 = np.transpose(u) @  u[:,-2:] @ np.transpose(u[:,-2:]) @ u


print(np.trace(eye1))



w = np.zeros(u[:,-2:].shape)
w[0,0] = 1
w[1,1] = 1

eye2 = np.transpose(u) @  w @ np.transpose(w) @ u

print(np.trace(eye2))


d = np.transpose(s) @ s

m = vh @ d @ np.transpose(vh)


"""
print(np.trace(d))
print(np.linalg.det(d))


print(np.trace(m))
print(np.linalg.det(m))
"""


