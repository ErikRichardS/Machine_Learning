import numpy as np

from settings import *
from data_loader import *

import matplotlib.pyplot as plt


def center_matrix(matrix):
	n = matrix.shape[1]

	matrix -= ( matrix @ np.ones((n,n)) ) / n

	return matrix




def svd(matrix):
	return np.linalg.svd(matrix)



def pca(matrix):
	mat = center_matrix(mat)

	u, s, vh = svd(mat)
	uk = np.transpose(u[:,:2] )

	x = uk @ mat

	show_data(x, zoo_type)





mat, zoo_type = get_data_matrix()








