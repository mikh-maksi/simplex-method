from simplex_functions import min_n, check_simplex_next_f 
from gen_functions import gen_VRP_data, get_data,add_artif_basis, A2At, b2c, c2b
import numpy as np
from simplex_out_f import simplex_out_fnc

obj = get_data("inpt1.json")

# Отримання основних елементів: A_ij, b_i, c_i
A_ij = np.array(obj["A_ij"])
b_i = np.array(obj["b_i"])
c_i = np.array(obj["c_i"])

# Взяття двоїстої задачі
A_ij = A2At(A_ij)
base_c_i = c_i
c_i = b2c(b_i)
b_i = c2b(base_c_i)

# Приведення до нормальної форми
# A_ij = A_ij*(-1)
# b_i = b_i*(-1)

# print(f"c_i = {c_i}")
# print(f"A_ij = {A_ij}")
# print(f"b_i = {b_i}")

# Додавання штучного базису
A_ij,c_i,Xbasis_i,Z_0,delta_i,fi_i=add_artif_basis(A_ij,c_i)

# print(A_ij,c_i,Xbasis_i,Z_0,delta_i,fi_i)
# Вхідні значення для задачі
print(f"c_i = {c_i}")
print(f"A_ij = {A_ij}")
print(f"b_i = {b_i}")