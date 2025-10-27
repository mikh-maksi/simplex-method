import json
from gen_functions import gen_VRP_data
def get_data(fname="inpt.json"):
    import json
    filename = "c:/Work/repo/simplex-method/code/v.0.0.3/input_data/"+fname
    with open(filename, "r", encoding="utf-8") as f:
        json_string = f.read()
    data = json.loads(json_string)
    return data

A_ij,b_i,Xbasis_i,c_i = gen_VRP_data(4)
# A_ij = [[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1.0]]
# b_i = [[1533],[1044],[371]]
# Xbasis_i = [[3],[4],[5]]
# c_i = [5,2,0,0,0]


obj = {"A_ij":A_ij,"b_i":b_i,"Xbasis_i":Xbasis_i,"c_i":c_i}

obj1 = get_data("inpt_VRP.json")
print(obj1["A_ij"])