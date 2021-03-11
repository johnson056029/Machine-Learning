#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def make_design_mat(data_x, num_data, num_bases):
    A = np.empty((23,0))
    for i in range(num_bases-1,-1,-1):
        A = np.hstack((A, data_x**i))
    return A

