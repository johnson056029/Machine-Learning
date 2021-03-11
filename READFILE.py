#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import re

# read in txt file consists of 2-d data points and output a numpy array of num_data_pointsX2

def read_data_points(file_name):
    file_string = open(file_name).read()
    num_data_points = file_string.count(',')
    splitted_string = re.split('[,\n]', file_string)
    splitted_float_mapobj = map(float, splitted_string)
    splitted_float = list(splitted_float_mapobj)
    data_points_array = np.array(splitted_float).reshape(num_data_points, 2)
    return data_points_array

