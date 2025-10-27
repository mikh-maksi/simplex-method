from simplex_functions import min_n, check_simplex_next_f 
from gen_functions import gen_VRP_data, get_data, A2At, b2c, c2b
import numpy as np
from simplex_out_f import simplex_out_fnc

obj = get_data("inpt2.json")
obj_t = get_data("inpt2_double.json")

A_ij = np.array(obj["A_ij"])
A_ij_double = np.array(obj_t["A_ij"])

def A2At(A_ij):
    return A_ij.transpose()

def b2c(b_i):
    c_out = np.array([],dtype=int)
    for el in b_i:
        c_out=np.append(c_out,el[0])
    return c_out

def c2b(c_i):
    b_out = np.array([],dtype=int)
    for el in c_i:
        b_out=np.append(b_out,[el])
    return b_out

A_ij_t = A2At(A_ij)

# print(A_ij)
print(A_ij_t)
print(A_ij_double)


b_i = np.array(obj["b_i"])
b_i_double =  np.array(obj_t["b_i"])

c_i = np.array(obj["c_i"])
c_i_double = np.array(obj_t["c_i"])

# from b 2 c

# print(b2c(b_i))
# print(c_i_double)

# from c 2 b



# print("---------")

# print(b_i_double)

# print(c_i)
# print(c2b(c_i))