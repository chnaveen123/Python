FW = open("Emp.csv","r")

gender = {}
desig = []
dept = []
sal = 0
sal1 = 0

for line in FW.readlines():
    g = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]


    if g in gender:
        gender[g] += 1

    else:
        gender[g] = 1

    if ds not in desig:
        desig.append(ds)
    if dp not in dept:
        dept.append(dp)

    sal += int(line.split(",")[5])

    if dp == "HR":
        sal1 += int(line.split(",")[5])

FW.close()

print(f"gender :{gender}")
print(f"Designation : {desig}")
print(f"Department : {dept}")
print(f"Salary : {sal}")
print(f"Salary of HR Dept: {sal1}")