<h1>Introducción</h1>
Golomb coding is a lossless data compression method invented by Solomon W. Golomb. Symbols following a geometric distribution will have a Golomb code as an optimal prefix code, making Golomb coding highly suitable for situations in which the occurrence of small values in the input stream is significantly more likely than large values.

<hr>
<h1>How the Encoder Works???</h1>

We start with passing the arguments as n and m in the encode_golomb function. Here, firstly we calculate the quotient, i.e. q and take its floor value. This q then further proceeds to another nested function to calculate the unary code. The unary code is calculated by assigning 1 for the magnitude of the integer that is the number of times 1 will be appended till the value of q. And a zero is appended at the end. The values in the list is then converted into an integer value and it is returned to the encode_golomb function.

```<br>
 def encode_golomb(n, m):
    q1 = (n / m)
    q = math.floor(q1)
    unary_code = unary(q)
 ```
 ```<br>
 def unary(q):
    code1 = []
    for i in range(q):
        code1.append(1)
    code1.append(0)
    code2 = [str(i) for i in code1]
    code = "".join(code2)
    return code 
 ```

We then proceed to calculate the values of k (and take it’s ceil value), c and r and now check for the conditions of the truncation of bits of the remainder and constant. 
If 0 <= r < c, then r is truncated to k – 1 bits, else r + c is truncated to k bits. This truncation of bits is done by another nested function, rem_trun.
This function calculates the binary value of r (or r + c) and truncates it to the value of k – 1 (or k) bits. 

 ```<br>
 def rem_trun(r, k):
    rem = bin(r)
    return rem[2:].zfill(k)
 ```

The unary code and r’ are returned back and printed as Golomb Code. The value of m is also returned and stored along with golomb code in form of a list which passes to the decoder function.
 
 ```<br>
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
```
The print statements describe the working of the encoder.

<br>
<hr>
<br>
<h1>How the Decoder Works???</h1>
<br>


Moving on to the decoding part, the decode_golomb takes the parameter of the list returned by the encode_golomb function and splits it into the golomb code and the value of m, storing them in different variables. Knowing the value of m, we calculate k and take ceil value to calculate c. Initially q is assigned as 0.

```<br>
def decode_golomb(master_directory):
    m = master_directory[1]
    code = list(master_directory[0])
    k1 = math.log(m, 2)
    k = math.ceil(k1)
    c = ((2 ** k) - m)
    q = 0
```

The unary code is then traversed and the number of 1’s is counted and traversing is stopped upon encountering the first zero. Each time 1 occurs the value of q is incremented by 1 and this 1 is removed from the golomb code leaving us with the remainder or remainder + constant which is stored in the form of an integer.

```<br>
for i in range(len(code)):
        if int(code[i]) == 1:
            q = q + 1
        else:
            break
    for i in range(q + 1):
        code.pop(0)
    code1 = [str(i) for i in code]
    code2 = "".join(code1)
```

The remainder is first calculated till k – 1 bits and the value of remainder is converted to its equivalent decimal. If r < c, the n is calculated as q multiplied by m plus the remainder.

```<br>
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
```
 

Else, we calculate the remainder + constant (rc) up to k bits and convert the binary value to it’s equivalent decimal and calculate the value of n as q multiplied by m plus the rc minus constant.

```<br>
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
```
 
The display of values of different parameters tell us the working of the decoder.

<br>
<hr>
<br>
<h1>The Driver Code!!!</h1>
<br>

The driver code is executes all the above functionalities for a smooth operation.

```<br>
n = int(input("Enter value of n: "))
m = int(input("Enter value of m: "))
master_directory = encode_golomb(n, m)
print("Golomb Code is: ", master_directory[0])
decode_golomb(master_directory)
```

<hr>

<h3>If you like this code and the explanation, make sure to leave a star on my repository.😁</h3>
