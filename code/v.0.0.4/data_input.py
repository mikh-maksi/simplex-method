import json
from gen_functions import gen_VRP_data

A_ij,b_i,Xbasis_i,c_i = gen_VRP_data(4)
data = {"A_ij":A_ij,"b_i":b_i,"Xbasis_i":Xbasis_i,"c_i":c_i}

print(data)
json_string = json.dumps(data)
#print(json_string)
#with open("c:/Work/repo/simplex-method/code/v.0.0.3/input_data/data.json", "w", encoding="utf-8") as f:
#    json.dump(data, f, ensure_ascii=False, indent=4)

