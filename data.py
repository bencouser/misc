#!/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt

# This file takes four arguments
# ipython3 filename [1 = MASS] [2 = ELASTIC CONSTANT] [3 = LATTIC CONSTANT] [4 = Trail Step]

np.seterr(all='ignore')

m = float(sys.argv[1])
u = float(sys.argv[2])
lc = float(sys.argv[3])
trial_step = float(sys.argv[4])

N = 100000 #Iterations of change
n = 1000 #number of intervals

points = []

for i in range(n):
	x = np.random.uniform(-1, 1)
	points.append(x)

def SE(b,a):
    diff = (1/2)*((m/(lc**2) * (y**2 - a**2 - 2*points[i+1]*(y-a))) + (u**2 * (y-a)**2))
    return diff

x_square = []
acpt = 0

for itera in range(N):
    for i in range(n):
            a = points[i+(n*itera)]
            y = a + trial_step * (2 * np.random.uniform(0,1) - 1)
            P_Metro = np.exp(-lc*(SE(y, a)))
            b = np.random.uniform(0,1)
            if b < P_Metro:
                a = y
                points.append(a)
#                acpt += 1
            if b > P_Metro:
                points.append(a)

            k = np.array(a**2)
    k = np.mean(k)
    x_square.append(k)

#acceptance_rate = acpt/len(points)
#print(acceptance_rate)

w = (u/(m**(1/2))) * ((1+((u**2 * lc**2)/(12*m)))**(1/2))

def y(x):
    y = (m*w/np.pi)**(1/2) * np.exp(-m*w*(x**2))
    return y

x = np.linspace(-3,3,100)

P = y(x)**2

plt.hist(points, 500, density=True)
plt.plot(x, P, label='Theoretical Relationship')
plt.ylabel('Probability')
plt.xlabel('Position')
plt.title('Probability Distribution of Position')
plt.savefig('Probability_Distribution_h.pdf')

x_square = np.array(x_square)

Ground_Energy = u**2 * x_square

np.savetxt("ground_energies.txt", Ground_Energy, fmt="%s")

