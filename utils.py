#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def get_2d_data_points(data):
    num_data = data.shape[0]
    data_x = data[:,[0]].reshape(-1,1)
    data_y = data[:,[1]].reshape(-1,1)
    return num_data, data_x, data_y


# In[ ]:




