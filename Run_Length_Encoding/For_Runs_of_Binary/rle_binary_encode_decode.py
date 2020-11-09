def bin_fix(num, k):
    bin_cd = bin(num)
    return bin_cd[2:].zfill(k)


def rle_encode_binary(string, k):
    count_list = []
    listc = [i for i in string]
    count = 0
    i = 0
    previous_character = listc[0]
    while (i <= len(listc) - 1):
        while (listc[i] == previous_character):
            i = i + 1
            count = count + 1
            if i > len(listc) - 1:
                break
        x = [previous_character, count]
        count_list.append(x)
        if i > len(listc) - 1:
            break
        previous_character = listc[i]
        count = 0
    max_bits = ((2**k) - 1)
    encode = ""
    for i in range(len(count_list)):
        if count_list[i][0] == '0':
            if count_list[i][1] < max_bits:
                code = bin_fix(count_list[i][1], k)
                encode = encode + code
            else:
                this = count_list[i][1]
                while(this != 0):
                    if this > max_bits:
                        code = bin_fix(max_bits, k)
                        encode = encode + code
                        this = this - max_bits
                    elif this == max_bits:
                        if count_list[i + 1][0] == '0':
                            code = bin_fix(max_bits, k)
                            encode = encode + code
                            this = 0
                        else:
                            code = bin_fix(max_bits, k)
                            encode = encode + code
                            encode = encode + bin_fix(0, k)
                            this = 0 
                    else:
                        code = bin_fix(this, k)
                        encode = encode + code
                        this = 0
        else:
            if(int(count_list[i][1]) > 1):
                for i in range(count_list[i][1] - 1):
                    encode = encode + bin_fix(0, k)
    print("Encoded Run Length Sequence is: ", encode)
    return [encode, k]


def rle_decode_binary(master_file):
    encoded = master_file[0]
    k = master_file[1]
    seq_mas = []
    while encoded:
        seq_mas.append(encoded[:k])
        encoded = encoded[k:]
    decode = ""
    int_val = []
    max_bits = ((2 ** k) - 1)
    for i in range(len(seq_mas)):
        integer = int(seq_mas[i],2)
        int_val.append(integer)
    for i in range(len(int_val)):
        if int_val[i] == max_bits:
            decode = decode  + '0' * max_bits
            if int_val[i + 1] == '0':
                decode = decode + '1'
            else:
                pass
        elif int_val[i] == '0':
            decode = decode + '1'
        else:
            decode = decode + ('0' * int_val[i])
            decode = decode + '1'
    length = len(decode)
    if(int_val[-1] > 0):
        print("The decoded sequence is: " + decode[:length - 1])
    else:
        print("The decoded sequence is: " + decode)


String = input("Enter the string: ")
k = int(input("Enter number of bits: "))
master_file = rle_encode_binary(String,k)
rle_decode_binary(master_file)
