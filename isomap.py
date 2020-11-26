import numpy as np

from settings import *
from data_handler import *
from mds import *

import matplotlib.pyplot as plt



# Creates an isomap graph matrix
def create_isomap_graph(distance_matrix, p=15):
	n = distance_matrix.shape[0]
	

	graph_matrix = np.ones(distance_matrix.shape)*-1 + np.eye(n)
	

	for i in range(n):
		distances = distance_matrix[i]

		for pi in range(p):
			min_val = 1e10
			min_i = -1

			# Find shortest distance
			for j in range(n):
				if j == i:
					continue

				if distances[j] < min_val:
					min_val = distances[j]
					min_i = j


			graph_matrix[i,min_i] = distances[ min_i ]
			graph_matrix[min_i,i] = distances[ min_i ]
			distances[ min_i ] = 1e10



	return graph_matrix

def floyd_warshall(graph_matrix):
	#print(graph_matrix[0])

	n = graph_matrix.shape[0]
	graph_distance_matrix = np.ones(graph_matrix.shape)*1e10
	for i in range(n):
		for j in range(n):
			if graph_matrix[i,j] != -1:
				graph_distance_matrix[i,j] = graph_matrix[i,j]
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if graph_distance_matrix[i,j] > graph_distance_matrix[i,k] + graph_distance_matrix[k,j]:
					graph_distance_matrix[i,j] = graph_distance_matrix[i,k] + graph_distance_matrix[k,j]


	#print(1e10 in graph_distance_matrix)

	return graph_distance_matrix





#mat, zoo_type = get_data_matrix()

#dist_mat = create_distance_matrix(mat)

#graph_mat = create_isomap_graph(dist_mat)

#graph_dist_mat = floyd_warshall(graph_mat)



#mds(graph_dist_mat)
