from utils import *
from DESIGN_MATRIX import *
from INVERSE import *
from polynomial import Polynomial

def LSE(data, num_bases, lambda_):

    num_data, data_x, data_y = get_2d_data_points(data)

    A = make_design_mat(data_x, num_data, num_bases)
    
    x = ivrs( (A.T@A + lambda_*np.identity((A.shape[1])) ) ) @ A.T @ data_y

    fitting_line = Polynomial(x.reshape(-1))

    total_error = sum((data_y - fitting_line.calculate(data_x))**2)

    return fitting_line, total_error