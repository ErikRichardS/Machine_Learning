import torch
import numpy as np
import matplotlib.pyplot as plt

from settings import *





def get_data_matrix():
	data_file = open("zoo.data")
	data_lines = data_file.readlines()

	# Create a zero d x n matrix
	data_matrix = np.zeros( (nr_attributes, len(data_lines)) )

	zoo_type = np.zeros((len(data_lines)))

	for i, line in enumerate(data_lines):
		attributes = line.split(",")[1:]

		zoo_type[i] = int(attributes[-1])

		for j, t in enumerate(attributes[:-1]):
			data_matrix[j,i] = int(t)

	return data_matrix, zoo_type


def show_data(x, zoo_type):
	#print(x.shape)

	zoo_color = []
	for i in range(len(zoo_type)):
		indx = int(zoo_type[i])-1
		zoo_color.append( color_map[ indx ] )

	plt.scatter(x[0], x[1], c=zoo_color)
	plt.show()




#mat, zoo_type = get_data_matrix()

#print(zoo_type.shape)

#print(mat.shape)