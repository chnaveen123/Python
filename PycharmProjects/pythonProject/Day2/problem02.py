m = int(input("1st value : "))
n = int(input("2nd Values : "))

for num in range(m, n + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if num == sum:
            print(num)