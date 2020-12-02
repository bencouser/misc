#!/bin/bash python

import sys
import numpy as np
import matplotlib.pyplot as plt

def read_data(file_name):
    with open(file_name,'r') as f:
        lines = f.read().split('\n')[:-1]
        data = np.array(
                [[float(entry)
                    for entry in line.split(',')]
                    for line in lines])
    return data

Eo_data = read_data(sys.argv[1])

Masses = Eo_data[:,0]
Eos = Eo_data[:,1]
Eo_errs = Eo_data[:,2]

Mass = Masses[1]
Eo = Eos[1]
Eo_errs = Eo_errs[1]

a = 0.01
u = 1
N = 100000
j = int(sys.argv[2])

def R(u):
    R = 1 + (a**2 * u**2 / 2) - a*u*(1+(a**2 * u**2 / 4))**(1/2)
    return R


def First_E(j):
    E_F = Eo - (1/a) * np.log((R(u)**(j+1) - R(u)**(N-j-1)) / (R(u)**(j) - R(u)**(N-j)))
    return E_F

def E_Ferr(Eo, E_F, Eo_errs):
    E_Ferr = (E_F/Eo) * Eo_errs
    return E_Ferr

First_Excit_State = First_E(j)
std = E_Ferr(Eo, First_E(j), Eo_errs)

print('{},{}'.format(First_Excit_State,std))
