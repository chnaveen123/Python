
def encode(cls,string,k):
    n = len(string)
    i = 0
    while i < n:
        j = i
        length = 0
        freq = 0

        while j < n  and string[j].isalpha():
            j += 1
            length += 1
        while j < n and string[j].isdigit():
            freq = freq * 10 + int(string[j])
            j += 1

        num = freq * length

        if k > num:
            k -= num
            i = j
        else:
            k -= 1
            k %= length
            return string[i + k]
    return string[k - 1]
if __name__ == '__main__':
    string = "a1b1c3"
    k = 5
    print(encode(string,k))

