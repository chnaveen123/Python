counter = 0
for num in range(150, 49, -1):

        for i in range(2,num):
            if (num % i ) == 0:
                break
        else:
            print(num, end=" ")
            counter += 1
print(counter)




