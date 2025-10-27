def take_file_number():
    f_num = open(f"c:/Work/repo/simplex-method/out/actual_number.txt", "r")
    n_str = str(f_num.readline())
    num = int(n_str)
    num+=1
    f_num.close()
    f_num = open(f"c:/Work/repo/simplex-method/out/actual_number.txt", "w")
    f_num.write(str(num))
    f_num.close()
    return num-1
print(take_number())

