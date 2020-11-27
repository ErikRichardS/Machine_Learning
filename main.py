import numpy as np

from settings import *
from data_handler import *
from pca import *
from mds import *
from isomap import *

import sys

def shutdown():
	print("Exit program")
	sys.exit()


if len(sys.argv) < 2:
	print("Missing argument")
	print("Use \'help\' to list usable arguments")
	shutdown()


arg = sys.argv[1]



if arg == "help":
	print("Usable commands:")
	arg_list = ["pca", "mds-data", "mds-dist", "mds-weight", "mds-pca", "isomap"]
	for ar in arg_list:
		print(ar)

	print()
	print("pca - can be followed by two distinct integers between 0 and 15 for custom use of columns")
	print("isomap - must be followed by a positive integer determining the number of nearest neighbors")
	shutdown()



mat, zoo_type, zoo_name = get_data_matrix()
x = None

if arg == "pca":
	if len(sys.argv) < 3:
		x = pca(mat)
	elif len(sys.argv) == 3:
		print("Invalid number of PCA integer arguments")
		shutdown()
	else:
		try:
			t1 = int(sys.argv[2])
			t2 = int(sys.argv[3])
			x = pca(mat, [t1, t2])
		except:
			print("PCA integer argument invalid")
			shutdown()

elif arg == "mds-data":
	mat = center_matrix(mat)
	x = mds_data(mat)

elif arg == "mds-dist":
	mat = center_matrix(mat)
	dist_mat = create_distance_matrix(mat)
	x = mds(dist_mat)

elif arg == "mds-weight":
	x = mds_weighted(mat)

elif arg == "mds-pca":
	mat = center_matrix(mat)
	x = pca_mds(mat)

elif arg == "isomap":
	try:
		neighbor = int(sys.argv[2])
		dist_mat = create_distance_matrix(mat)
		graph_mat = create_isomap_graph(dist_mat, p=neighbor)
		graph_dist_mat = floyd_warshall(graph_mat)

		x = mds(graph_dist_mat)
	except:
		print("Isomap neighbor argument invalid")
		shutdown()
	
else:
	print("Invalid argument")
	shutdown()


show_data(x, zoo_type, zoo_name)
