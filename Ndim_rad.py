#!/bin/env python
import numpy as np
import sys

# Gets first argument given to this script
dim = int(sys.argv[1])

R = float(sys.argv[2])
N = int(1e4)

# Create array of random coordinates
points = R * np.random.random_sample([dim,N])

# Define points inside circle
inside = np.sum(points**2,axis=0) < R**2

# Count points in circle
N_inside = np.sum(inside)

# Find fraction of points in circle
fraction = N_inside/N
fraction_error = np.sqrt(fraction/N)

# Calculate area of unit circle
area = fraction*(2*R)**dim
error = fraction_error*(2*R)**dim

# Calculate uncertainty of area
print('{},{}'.format(area,error))
