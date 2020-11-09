import math


def binary_fix(i, n):
    binary = bin(i)
    return binary[2:].zfill(n)


def tunstall_encode(alpha, prob, k, N, n, string):
    final = []
    for i in range(N):
        final.append([alpha[i], prob[i]])
    for i in range(k):
        last = max(final, key = lambda x:x[1])
        for i in range(N):
            final.append([last[0] + alpha[i], last[1] * prob[i]])
        final.pop(final.index(last))
    for i in range(len(final)):
        final[i][1] = binary_fix(i, n)
    print("The set of alphabets and codes are: ")
    print("Alphabet\tCode")
    print("-------------------------")
    for i in range(len(final)):
        print(final[i][0], end = "\t")
        print(final[i][1])
    stri = list(string)
    encode = ""
    count = 0
    flag = 0
    for i in range(len(stri)):
        for j in range(len(final)):
            if stri[i] == final[j][0]:
                encode = encode + str(final[j][1])
                flag = 1
        if flag == 1:
            flag = 0
        else:
            count = count + 1
            if count == len(stri):
                break
            else:
                stri.insert(i + 1,str(stri[i]+stri[i + 1]))
                stri.pop(i + 2)
    print("Generated tunstall code for string " + string + " is: " + encode)
    return[encode, final, n]


def tunstall_decode(master_directory):
    encode = master_directory[0]
    final = master_directory[1]
    n = master_directory[2]    
    decode = []
    while encode:
        decode.append(encode[:n])
        encode = encode[n:]
    string = ""
    for i in range(len(decode)):
        for j in range(len(final)):
            if decode[i] == str(final[j][1]):
                string = string + final[j][0]
    print("---------------------------------------------------------------")
    print("Decoded string is:", end = " ")
    return string


n = int(input("Enter number of bits: " ))
string = input("Enter the string to be encoded: ")
len_str = len(string)
dictionary = dict()
for i in string:
    if i in dictionary:
        dictionary[i] = dictionary[i] + 1
    else:
        dictionary[i] = 1
alphabet = []
probability = []
for i in dictionary.items():
    alphabet.append(i[0])
    probability.append(i[1])
for i in range(len(probability)):
    probability[i] = probability[i] / len_str
N = len(alphabet)
k = math.floor(((2 ** n) - N)/ (N - 1))
master_directory = tunstall_encode(alphabet, probability, k, N, n, string)
print(tunstall_decode(master_directory))
