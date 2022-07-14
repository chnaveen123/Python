FW = open("Emp.csv","r")

gender = {}
#desig = []

for line in FW.readlines():

    gender += (line.split(",")[2])
    print(gender)
    """ds = line.split(",")[3]


    if g in gender:
        gender[g] += 1

    else:
        gender[g] = 1

    if ds not in desig:
        desig.append(ds)
"""
FW.close()

#print(f"gender :{gender}")
#print(f"Designation : {desig}")