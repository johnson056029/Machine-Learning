import numpy as np
from polynomial import Polynomial
import matplotlib.pyplot as plt
import sys

def output(method, fitting_line, total_error, data):
    
    print(method, "\b:")
    print("Fitting line: ", fitting_line)
    print("Total error: ", total_error[0])
    
    data_x = data[:,[0]].reshape(-1,1)
    data_y = data[:,[1]].reshape(-1,1)
    plt.plot(data_x,data_y,'ro')
    
    plt.plot(np.arange(-6,6,0.1),fitting_line.calculate(np.arange(-6,6,0.1)),'k')
    plt.show()