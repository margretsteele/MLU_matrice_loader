import csv

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import sparse

users = []
movies = []
ratings = []

with open('ratings.csv', 'rb') as csvfile:
	hasHeader = csv.Sniffer().has_header(csvfile.read(1024))
	csvfile.seek(0)  # rewind
	knownRatings = csv.reader(csvfile)
	if hasHeader:
		next(knownRatings)  # skip header row

	for row in knownRatings:
		users.append(np.int_(row[0]))
		movies.append(np.int_(row[1]))
		ratings.append(np.float_(row[2]))

matrix = sparse.coo_matrix((ratings, (users, movies)))
