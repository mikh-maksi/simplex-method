import json

def get_data(fname="inpt.json"):
    import json
    filename = "c:/Work/repo/simplex-method/code/v.0.0.3/input_data/"+fname
    with open(filename, "r", encoding="utf-8") as f:
        json_string = f.read()
    data = json.loads(json_string)
    return data


A_ij = [[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1.0]]
b_i = [[1533],[1044],[371]]
Xbasis_i = [[3],[4],[5]]
c_i = [5,2,0,0,0]
Z_0 = 0
delta_i = [0,0,0,0,0]
fi_i = [0,0,0,0,0]

obj = {"A_ij":A_ij,"b_i":b_i,"Xbasis_i":Xbasis_i,"c_i":c_i}

obj1 = get_data("data_VRP.json")
print(obj1["A_ij"])