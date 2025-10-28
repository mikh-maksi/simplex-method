from gen_functions import gen_VRP_data, get_data, A2At, b2c, c2b, add_basis,list_null,add_nulls_c_i,add_artif_basis
import numpy as np

obj = get_data("data_VRP_small.json")
A_ij = np.array(obj["A_ij"])
b_i = np.array(obj["b_i"])
c_i = np.array(obj["c_i"])

A_ij = A2At(A_ij)
c_i = b2c(b_i)
b_i = c2b(c_i)

print(b_i)

# A_ij,c_i,Xbasis_i,Z_0,delta_i,fi_i=add_artif_basis(A_ij,c_i)

# print(A_ij,c_i,Xbasis_i,Z_0,delta_i,fi_i)
