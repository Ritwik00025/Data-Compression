import math


def bin_fix(n, k):
    num = bin(n)
    return num[2:].zfill(k)


def rle_encode(str1):
    count = 0
    length = len(str1)
    i = 0
    final_rle = []
    rle = []
    previous_character = str1[0]
    while (i <= length - 1):
        while (str1[i] == previous_character):
            i = i + 1
            count = count + 1
            if i > length - 1:
                break
        x = [previous_character, count]
        rle.append(x)
        if i > length - 1:
            break
        previous_character = str1[i]
        count = 0
    alphabets = []
    alpha_codes = []
    rle_max = max(rle, key=lambda x: x[1])
    places_code = math.ceil(math.log(rle_max[1], 2))
    for i in range(len(rle)):
        rle[i][1] = bin_fix(rle[i][1], places_code)
    for i in range(0,len(rle)):
        a = rle[i][0]
        if a not in alphabets:
            alphabets.append(a)
    places_alpha = math.ceil(math.log(len(alphabets),2)) 
    for i in range(len(alphabets)):
        numb = bin_fix(i, places_alpha)
        alpha_codes.append([alphabets[i],numb])
    for i in range(len(rle)):
        for j in range(len(alpha_codes)):
            if alpha_codes[j][0] == rle[i][0]:
                final_rle.append((alpha_codes[j][1],rle[i][1]))
    final_rle = tuple(final_rle)
    return [final_rle,alpha_codes]



def rle_decode(decompressor):
    final_str = []
    final_strg = ''
    str1 = []
    final_rle1 = decompressor[0]
    final_rle = list(map(list,final_rle1))
    alpha_codes = decompressor[1]
    for i in range(len(final_rle)):
        for j in range(len(alpha_codes)):
            if alpha_codes[j][1] == final_rle[i][0]:
                str1.append([alpha_codes[j][0],final_rle[i][1]])
    for i in range(len(str1)):
        final_str.append([str1[i][0],int(str1[i][1],2)])
    for i in range(len(final_str)):
        for j in range(final_str[i][1]):
            final_strg = final_strg + str(final_str[i][0])
    return final_strg
            

str1 = input("Enter the string: ")
print("String to be encoded: ", str1)
a = rle_encode(str1)
print("Run Length Encoding: ", a[0])
print("Decoded string: ", rle_decode(a))
