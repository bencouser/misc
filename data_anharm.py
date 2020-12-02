#!/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt
import random #seeing if np random n generator was why odd data

# This file takes four arguments
# ipython3 filename [1 = MASS] [2 = ELASTIC CONSTANT] [3 = LATTIC CONSTANT] [4 = Trial Step] [5 = Lambda]

np.seterr(all='ignore')

m = float(sys.argv[1])
u = float(sys.argv[2])
lc = float(sys.argv[3])
trial_step = float(sys.argv[4])
lam = float(sys.argv[5])

N = 100000
n = 1000

points = []

for i in range(n):              #making 1000 random points 
    x = random.random() - 0.5
    points.append(x)

def SE(b,a):                #the difference in energy when point a becomes y
    diff = (m / (2 * lc**2) * (y**2 - a**2 - 2 * points[i+1] * (y - a))) + ((u**2 / 2) * (y**2 - a**2)) + (lam * (y**4 - a**4))
    return diff

x_square = []
x_four = []
acpt = 0

for itera in range(N): # changing 1000 points N times dependant on weight e^diff 
    for i in range(n):
            k = []
            o = []
            a = points[i+(n*itera)]
            y = a + trial_step * (2 * random.random() - 1)
            P_Metro = np.exp(-(a*SE(y, a)))
            b = 0.4
            if b < P_Metro:
                a = y
                points.append(a)
                acpt += 1
            if b > P_Metro:
                points.append(a)

            k.append(a**2)
            o.append(a**4)
    k = np.array(k)
    o = np.array(o)
    k = np.mean(k)
    o = np.mean(o)
    x_square.append(k)
    x_four.append(o)

acceptance_rate = acpt / len(points)
print(acceptance_rate)

s = sum(points) #normalising for probability distribution
norm = [float(i)/s for i in points]

plt.hist(norm, 1000)
plt.ylabel('Probability')
plt.xlabel('Position')
plt.title('Probability Distribution of Position')
plt.savefig('Probability_Distribution_anharm.pdf')

x_square = np.array(x_square)
x_four = np.array(x_four)

Ground_Energy = u**2 * x_square + 3*lam*x_four #finding ground energy state

np.savetxt("ground_energies_an.txt", Ground_Energy, fmt="%s") #putting in text file that will then go to be binned and boot strapped
