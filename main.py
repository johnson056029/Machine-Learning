from READFILE import *
from INPUT import *
from LSE import *
from NEWTONS_METHOD import *
from OUTPUT import *
import matplotlib.pyplot as plt

data = read_data_points("testfile.txt")

num_bases, lambda_ = get_input()

fitting_line, total_error = LSE(data, num_bases, lambda_)
output("LSE", fitting_line, total_error, data)

fitting_line, total_error = Newton(data, num_bases)
output("Newton's method", fitting_line, total_error, data)