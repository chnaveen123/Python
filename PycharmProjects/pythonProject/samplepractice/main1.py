import SampleAss2


FW = open("firstq.py","r")
gender = {}
for line in FW.readlines():
    g = line.split(",")[3]

    if g in gender:
        gender[g] += 1
    else:
        gender[g] = 1

FW.close()

print(f"gender :{gender}")