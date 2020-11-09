import math


def unary(q):
    code1 = []
    for i in range(q):
        code1.append(1)
    code1.append(0)
    code2 = [str(i) for i in code1]
    code = "".join(code2)
    return code


def rem_trun(r, k):
    rem = bin(r)
    return rem[2:].zfill(k)


def encode_golomb(n, m):
    q1 = (n / m)
    q = math.floor(q1)
    unary_code = unary(q)
    k1 = math.log(m, 2)
    k = math.ceil(k1)
    c = ((2 ** k) - m)
    r = n % m
    if (r >= 0 and r < c):
        r1 = rem_trun(r, k - 1)
        print()
        print("Case of 0 <= r < c, r is truncated to k - 1 bits")
        print("Unary Code\tRemainder\tBinary(r to k - 1 bits)")
        print("----------------------------------------------------------")
        print(unary_code, end = "\t\t")
        print(r, end = "\t")
        print(r1)
        print()
        return [unary_code + r1, m]
    else:
        r1 = rem_trun(r + c, k)
        print()
        print("Case of r > c, r + c is truncated to k bits")
        print("Unary Code\tr + c\tBinary(r + c to k bits)")
        print("----------------------------------------------------------")
        print(unary_code, end = "\t\t")
        print(r + c, end = "\t")
        print(r1)
        print()
        return [unary_code + r1, m]

    
def decode_golomb(master_directory):
    m = master_directory[1]
    code = list(master_directory[0])
    k1 = math.log(m, 2)
    k = math.ceil(k1)
    c = ((2 ** k) - m)
    q = 0
    for i in range(len(code)):
        if int(code[i]) == 1:
            q = q + 1
        else:
            break
    for i in range(q + 1):
        code.pop(0)
    code1 = [str(i) for i in code]
    code2 = "".join(code1)
    n = 0
    r1 = []
    for i in range(k - 1):
        r1.append(code[i])
    r2 = [str(i) for i in r1]
    r3 = "".join(r2)
    r = int(r3, 2)
    rc = 0
    if r < c:
        n = q * m + r
        print()
        print("Golomb Decoder")
        print("n\tm\tk\ttr\tc\tr+c")
        print("-----------------------------------------------------------")
        print(n, end = "\t")
        print(m, end = "\t")
        print(k, end = "\t")
        print(r, end = "\t")
        print(c, end = "\t")
        print(r + c)
    else:
        r1 = []
        for i in range(k):
            r1.append(code[i])
        r2 = [str(i) for i in r1]
        r3 = "".join(r2)
        rc = int(r3, 2)
        n = q * m + rc - c
        print()
        print("Golomb Decoder")
        print("n\tm\tk\tr\tc\tr+c")
        print("---------------------------------------------------------")
        print(n, end = "\t")
        print(m, end = "\t")
        print(k, end = "\t")
        print(r, end = "\t")
        print(c, end = "\t")
        print(r + c)
    
    
n = int(input("Enter value of n: "))
m = int(input("Enter value of m: "))
master_directory = encode_golomb(n, m)
print("Golomb Code is: ", master_directory[0])
decode_golomb(master_directory)
