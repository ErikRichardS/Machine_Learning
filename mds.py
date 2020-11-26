import numpy as np

from scipy.linalg import sqrtm

from settings import *
from data_handler import *
from pca import *


import matplotlib.pyplot as plt


def eigen_decomposition(matrix):
	return np.linalg.eigh(matrix)


def distance(v1, v2):
	return np.linalg.norm(v1 - v2) 


def create_distance_matrix(matrix):
	n = matrix.shape[1]
	distance_matrix = np.zeros((n, n))

	for i in range(n):
		for j in range(i+1,n):
			dist = distance(matrix[:,i], matrix[:,j])
			distance_matrix[i,j] = dist
			distance_matrix[j,i] = dist

	return distance_matrix


def data_to_similarity_matrix(matrix):
	return np.transpose(matrix) @ matrix


def distance_to_similarity_matrix(distance_matrix):
	n = distance_matrix.shape[0]
	ones = np.ones(distance_matrix.shape)
	mean_rows = (distance_matrix @ ones) / n
	mean_cols = (ones @ distance_matrix) / n

	mean_all = (ones @ distance_matrix @ ones) / (n*n)

	similarity_matrix = distance_matrix - mean_rows
	similarity_matrix -= mean_cols
	similarity_matrix += mean_all
	similarity_matrix /= -2

	return similarity_matrix



def mds(distance_matrix):
	sim_mat = distance_to_similarity_matrix(distance_matrix)

	v, u = eigen_decomposition(sim_mat)
	v = sqrtm( np.diag(v) )[-2:,:]
	ut = np.transpose(u)

	x = v @ ut
	x = np.real(x)

	return x


def mds_data(matrix):
	sim_mat = data_to_similarity_matrix(matrix)

	v, u = eigen_decomposition(sim_mat)
	v = sqrtm( np.diag(v) )[-2:,:]
	ut = np.transpose(u)

	x = v @ ut
	x = np.real(x)

	return x


def pca_mds(matrix):
	u, s, vh = svd(matrix)
	uk = np.transpose(u[:,:12] )

	mat = uk @ matrix

	dist_mat = create_distance_matrix(mat)

	return mds(dist_mat)

def mds_weighted(matrix, center=True):
	matrix[-1] /= 4 # Catsize
	matrix[-2] /= 2 # Domestic
	matrix[-4] /= 4 # Nr legs

	if center:
		matrix = center_matrix(matrix)

	dist_mat = create_distance_matrix(matrix)

	return mds(dist_mat)
	



#mat, zoo_type = get_data_matrix()

#mds_weighted(mat)

#mat = center_matrix(mat)



#mat = center_matrix(mat)
#mds_data(mat)

