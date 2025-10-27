from gen_functions import gen_VRP_data, get_data, A2At, b2c, c2b
import numpy as np
obj = get_data("inpt2.json")

print(obj)

A_ij = np.array(obj["A_ij"])
b_i = np.array(obj["b_i"])
c_i = np.array(obj["c_i"])

rows, cols = A_ij.shape

print(rows)
n = rows+cols

delta_i = [0,0,0,0,0]
fi_i = [0,0,0,0,0]
Xbasis_i = np.array([[3],[4],[5]])




def Xbasis_add(cols,rows):
    Xbasis_arr = []
    for i in range(cols):
        Xbasis_arr.append([i+rows+1])
    return Xbasis_arr

print(Xbasis_add(4,12))


def list_null(n):
    out_arr = []
    for i in range(n):
        out_arr.append(0)
    return out_arr

def add_basis(A_ij):
    rows, cols = A_ij.shape
    one = np.eye(rows,dtype=int)
    all = np.hstack((A_ij,one))
    return all

def add_nulls_c_i(c_i,rows):
    nl = list_null(rows)
    c_i=np.append(c_i,nl)
    return c_i

c_i = add_nulls_c_i(c_i,rows)
print(c_i)
# print(add_basis(A_ij))

# print(list_null(5))