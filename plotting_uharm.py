#!/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np

np.seterr(all='ignore')

def R(u):
    R = 1 + (a**2 * u**2 / 2) - a*u*(1+(a**2 * u**2 / 4))**(1/2)
    return R

def x_square_theo(u):
    x_square_theo = 1 / ((2*u*(1+(a**2 * u**2 / 4))**(1/2))) * ((1+R(u)**N)/(1-R(u)**N))
    return x_square_theo

def EoTheo(u):
    EoTheo = u**2 * x_square_theo(u)
    return EoTheo

utheo = np.linspace(0, 3, 200)
a = 0.01
N = 100000

def read_data(file_name):
    with open(file_name,'r') as f:
        lines = f.read().split('\n')[:-1]
        data = np.array(
                [[float(entry)
                    for entry in line.split(',')]
                    for line in lines])
    return data

const_m = read_data(sys.argv[1])
Elastic_Constant = const_m[:,0]
Ground_Energy = const_m[:,1]
GE_err = const_m[:,2]
plt.errorbar(Elastic_Constant, Ground_Energy, yerr = GE_err, label='Found Data', fmt='.')
plt.plot (utheo, EoTheo(utheo), label='Theoretical Values')
plt.legend()
plt.title('Constant m = 1')
plt.xlabel('Elastic Constant')
plt.ylabel('Ground_Energy')
plt.savefig(sys.argv[2])

