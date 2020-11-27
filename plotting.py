#!/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np

#This file takes three arguments.
#python filename [DATA1][DATA2][OUTPUT]


# Reads data from files with columns. 
# With comma sperated variables (txt, or csv).
def read_data(file_name):
    with open(file_name,'r') as f:
        lines = f.read().split('\n')[:-1]
        data = np.array(
                    [[float(entry) 
                        for entry in line.split(',')] 
                        for line in lines])
    return data

# Defines the figure and the two axes
fig,[ax1,ax2] = plt.subplots(1,2)

# Plots the data for the constant N=3 case, 
# Reading the data from the file given as the first argument
# Error read and plotted
const_N = read_data(sys.argv[1])
Radius = const_N[:,0]
Volume = const_N[:,1]
V_err1 = const_N[:,2]
ax1.errorbar(Radius, Volume, yerr = V_err1, fmt='.')
ax1.set_title('Constant N = 3')
ax1.set_xlabel('Radius')
ax1.set_ylabel('Volume') 

# Plots the data for the constant r=1 case,
# Reading the data from the file given as the second argument
# Errors read and plotted
const_r = read_data(sys.argv[2])
Dimensions = const_r[:,0]
Volume = const_r[:,1]
V_err2 = const_r[:,2]
ax2.errorbar(Dimensions, Volume, yerr = V_err2, fmt='.')
ax2.set_title('r = 1')
ax2.set_xlabel('Dimensions')
ax2.set_ylabel('Volume')

#save to a image who's file name is the 3rd argument
#plt.show()
plt.savefig(sys.argv[3])
