
FL = open("data.txt", "rb")

fl_pos = FL.seek(100,0)

print(fl_pos)

fl_pos = FL.seek(50, 1)

print(fl_pos)
print(FL.seek(50, 1))

FL.close()
