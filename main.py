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
	shutdown()


arg = sys.argv[1]



mat, zoo_type, zoo_name = get_data_matrix()
x = None

if arg == "pca":
	x = pca(mat)
	
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
