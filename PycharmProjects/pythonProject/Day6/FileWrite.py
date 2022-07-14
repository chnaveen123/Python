
FW = open("myfile.txt","w")

#st = input("Enter the contents of the file :")

l1 = "this is the 1st line.\n"
l2 = "this is the 2nd line.\n"
l3 = "this is the 3rd line.\n"

FW.writelines([l1,l2,l3])

FW.close()