#!/bin/env python
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

# Binning data

def bins(dat, numBin):
    bins_size = []

    lgth = int(dat.shape[0] / numBin)
    for i in range(numBin):
        me = np.mean(dat[lgth*i:lgth*(i+1)])
        bins_size.append(me)
    bins_size = np.array(bins_size)
    return bins_size

# Bootstrapping

def bootst(dat, numBin, tot_iter):

    tot_boot_dat = []

    for i in range(tot_iter):
        boot_dat = []
        for i in range(numBin):

            rp = np.random.randint(numBin)
            boot_Ener = dat[rp]
            boot_dat.append(boot_Ener)
        boot_dat = np.array(boot_dat)
        m_boot = np.mean(boot_dat)
        tot_boot_dat.append(m_boot)

    tot_boot_dat = np.array(tot_boot_dat)
    mean_boot = np.mean(tot_boot_dat)
    std_boot = np.std(tot_boot_dat)
    return mean_boot, std_boot

unbinned = read_data(sys.argv[1])

numBin = int(sys.argv[2])

bin_size = bins(unbinned, numBin)

tot_iter = 10000

mean, std = bootst(bin_size, numBin, tot_iter)

#np.savetxt("bootbindata.txt", mean, fmt="%s")
#np.savetxt("bootbinstd.txt", std, fmt="%s")

print('{},{}'.format(mean,std))
