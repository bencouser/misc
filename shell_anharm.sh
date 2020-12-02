#!/bin/bash


data_m_an="ground_energies_m_an.txt"
data_u_an="ground_energies_u_an.txt"
data_lambda_an="ground_energies_lambda_an.txt"

echo "Clearing data files"
rm $data_m_an
rm $data_u_an
rm $data_lambda_an
touch $data_m_an
touch $data_u_an
touch $data_lambda_an

echo "Finding Ground Energy while changing Mass"
for m in 0.1 0.4 0.6 1 2
do
echo "m = " $m ", u = 1 , lambda = 1"
variable=`python data_anharm.py $m 1 0.1 1 1`
variable=`python binning.py "ground_energies_an.txt" 1000`
echo -e "$m,$variable" >> "$data_m_an"
done

echo "Finding Ground Energy while changing Elastic Constant"
for u in -5 -3 -1 0 1 3 5
do
echo "u = " $u ", m = 1 , lambda = 1"
variable=`python data_anharm.py 1 $u 0.1 1 1`
variable=`python binning.py "ground_energies_an.txt" 1000`
echo -e "$u,$variable" >> "$data_u_an"
done

echo "Finding Ground Energy while changing Lambda"
for lambda in 0.01 0.05 0.1 0.2 0.5 1
do
echo "lambda = " $lambda ", m = 1 , u = -3"
variable=`python data_anharm.py 1 -3 0.1 1 $lambda`
variable=`python binning.py "ground_energies_an.txt" 1000`
echo -e "$lambda,$variable" >> "$data_lambda_an"
done

python plotting_an.py $data_m_an $data_u_an $data_lambda_an
echo "Outputted file to plot_an.pdf"

