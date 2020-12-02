# Finding optimal bin depth
import numpy as np
import sys
import matplotlib.pyplot as plt

def read_data(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().split('\n')[:-1]
        data = np.array(
                [[float(entry)
                    for entry in line.split(',')]
                    for line in lines])
    return data

def std(data):
    N = data.shape[0]
    deno = N*(N-1)
    avg = np.mean(data)
    Var = np.sum((data-avg)**2)/deno
    return np.sqrt(Var)

def bin_er(obs, numBin):
    bin_size = []

    lgth = int(obs.shape[0] / numBin)
    for i in range(lgth):
        me = np.mean(obs[numBin*i:numBin*(i+1)])
        bin_size.append(me)
    bin_size = np.array(bin_size)
    
    return std(bin_size)

data = read_data(sys.argv[1])

beans = np.array([1,2,4,5,9,10,12,15,33,50,100,150,400,800,1000,3000])
tot = beans.shape[0]
diff_bins = []
for i in range(tot):
        N_bean = beans[i]
        diff_bins.append(bin_er(data,N_bean))

diff_bins = np.array(diff_bins)

plt.errorbar(beans, diff_bins, fmt = '.')
plt.xscale('log')
plt.ylabel('Error')
plt.xlabel('Bin Depth')
plt.title('Standard Deviation vs Bin Depth')
plt.savefig("Binning_Graph.jpg")
