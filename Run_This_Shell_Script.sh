#!/bin/bash
#Clears the previous data set.
data_rad="changing_radius.txt"
data_dim="changing_dimension.txt"

echo Clearing data files
rm $data_rad
rm $data_dim
touch $data_rad
touch $data_dim

#Performs a range of dimensional values from 1-10
echo Keeps radius fixed at r=1, Changing dimension
for d in 1 2 3 4 5 6 7 8 9 10 
do
echo "d = " $d ", r = 1"
variable=`python Ndim_rad.py $d 1`
echo -e "$d,$variable" >> $data_dim
done

#Performs a range of radius values provided in the argument.
echo Keeps dimension fixed at d=3, Changing radius 
for r in $@ 
do
echo "d = 3, r = " $r
variable=`python Ndim_rad.py 3 $r`
echo -e "$r,$variable" >> $data_rad
done

#Executes the process to return the two text files and a pdf.
python plotting.py $data_rad $data_dim "plot.pdf"
echo Outputted file to plot.pdf
