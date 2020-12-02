#!/bin/bash


#Clears the previous data set
data_m="ground_energies_m.txt"
data_u="ground_energies_u.txt"
First_E="first_excited_state.txt"

echo "Clearing data files"
rm $data_m
rm $data_u
rm $First_E
touch $data_m
touch $data_u
touch $First_E

echo "Finding Ground Energy while changing Mass"
for m in 0.1 1 2 3 4 5
do
echo "m = " $m ", u = 1"
variable=`python data.py $m 1 0.5 1`
variable=`python binning.py "ground_energies.txt" 1000`
echo -e "$m,$variable" >> "$data_m"
done

echo "Finding Ground Energy while changing Elastic Constant"
for u in 0.01 0.5 1 1.5 2 2.5 3
do
echo "u = " $u ", m = 1"
variable=`python data.py 1 $u 0.5 1`
variable=`python binning.py "ground_energies.txt" 1000`
echo -e "$u,$variable" >> "$data_u"
done

python plotting_mharm.py $data_m "plot_m.pdf"
echo "Outputted file to plot_mharm.pdf"

python plotting_uharm.py $data_u "plot_u.pdf"
echo "Outputted file to plot_uharm.pdf"

echo "Finding First Excited state when m = 1, u = 1"
for j in 0 1 2 3 4 5 6 7 8
do
variable=`python firstEm.py $data_m $j`
echo -e "$j,$variable" >> "$First_E"
done

echo "\n All Workings Finished!"
