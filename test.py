import numpy as np

from mds import *
from pca import *

import scipy.linalg as li


mat, zoo_type = get_data_matrix()
mat = center_matrix(mat)


mat = np.random.rand(20,20)

u, s, vh = svd(mat)

print(li.det(u))


"""
print(np.trace(d))
print(np.linalg.det(d))


print(np.trace(m))
print(np.linalg.det(m))
"""


