#!/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np

def read_data(file_name):
    with open(file_name,'r') as f:
        lines = f.read().split('\n')[:-1]
        data = np.array(
                [[float(entry)
                    for entry in line.split(',')]
                    for line in lines])
    return data

const_u_l = read_data(sys.argv[1])
Mass = const_u_l[:,0]
Ground_Energy = const_u_l[:,1]
GE_err1 = const_u_l[:,2]
plt.errorbar(Mass, Ground_Energy, yerr = GE_err1, fmt='.')
plt.title('Constant u = 1, Lambda = 1')
plt.xlabel('Mass')
plt.ylabel('Ground_Energy')
plt.savefig("Const_an_u_lambda.pdf")

const_m_l = read_data(sys.argv[2])
Elastic_Constant = const_m_l[:,0]
Ground_Energy = const_m_l[:,1]
GE_err2 = const_m_l[:,2]
plt.errorbar(Elastic_Constant, Ground_Energy, yerr = GE_err2, fmt='.')
plt.title('Constant m = 1, Lambda = 1')
plt.xlabel('Elastic Constant')
plt.ylabel('Ground_Energy')
plt.savefig("Const_an_m_lambda.pdf")

const_m_u = read_data(sys.argv[3])
Lambda = const_m_u[:,0]
Ground_Energy = const_m_u[:,1]
GE_err3 = const_m_u[:,2]
plt.errorbar(Lambda, Ground_Energy, yerr = GE_err3, fmt='.')
plt.title('Constant m = 1, u = 1')
plt.xlabel('Lambda')
plt.ylabel('Ground Energy')
plt.savefig("Const_an_m_u.pdf")
