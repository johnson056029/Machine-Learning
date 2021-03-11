from DESIGN_MATRIX import *
from INVERSE import *
from polynomial import Polynomial
from utils import *
import sys


def Gradient(A,x,data_y):
    G = 2 * A.T @ A @ x - 2 * A.T @ data_y
    return G

def Hessian(A):
    H = 2 * A.T @ A
    return H

def Newton(data, num_bases):
    
    num_data, data_x, data_y = get_2d_data_points(data)

    A = make_design_mat(data_x, num_data, num_bases)
    
    x = np.random.rand(A.shape[1],1)
    error = sys.float_info.max
    while error > 1:
        G = Gradient(A, x, data_y)
        H = Hessian(A)
        x_update = x - ivrs(H) @ G
        error = sum((x - x_update)**2)
        x = x_update
        
    fitting_line = Polynomial(x.reshape(-1))
    total_error = sum((data_y - fitting_line.calculate(data_x))**2)
    
    return fitting_line, total_error