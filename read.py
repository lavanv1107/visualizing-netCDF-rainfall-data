#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:07:17 2021

@author: lauren_hb
"""
from netCDF4 import Dataset

#Read Data
#Change the path name to the location of the TRMM_2.5x2.5.nc on your computer
rain_file = '/Users/DELL/Downloads/file.nc'
my_TRMM_data = Dataset(rain_file)

#Rainfall Variables from the TRMM_2.5x2.5.nc file
rainfall_data = my_TRMM_data.variables['PREC'][:]#(TIME SIZE=8034, LAT SIZE =72, LON SIZE=144)
lat= my_TRMM_data.variables['LAT'][:]#LAT SIZE = 72
lon= my_TRMM_data.variables['LON'][:]#LON SIZE= 144
time= my_TRMM_data.variables['TIME'][:]# TIME SIZE= 8034  Also, Note that the dataset starts on Jan 01, 1998

print(my_TRMM_data)


"""
Also, please note that when you slice the data say for time (shown below): 
    
time[0] 

So, "time[0]" would correspond with Jan 01, 1998, the very first day (or index) in the dataset


"""