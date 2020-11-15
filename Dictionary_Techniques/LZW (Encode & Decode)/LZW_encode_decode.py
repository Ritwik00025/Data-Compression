def LZW_encode(init_dict, sequence):
    encode_table = []
    encode_list = []
    for i in init_dict.items():
        encode_table.append([i[0], i[1]])
    init_char = ''
    init_char = init_char + sequence[0]
    index_encode_table = len(encode_table)
    next_char = ''
    for i in range(len(sequence)):
        flag = 0
        if i != len(sequence) - 1:
            next_char = next_char + sequence[i + 1]
        for j  in range(len(encode_table)):
            if str(init_char + next_char) == str(encode_table[j][0]):
                flag = 1
        if flag == 1:
            init_char = str(init_char + next_char)
        else:
            for k in range(len(encode_table)):
                if init_char == encode_table[k][0]:
                    encode_list.append(encode_table[k][1])
            index_encode_table = index_encode_table + 1
            encode_table.append([str(init_char + next_char), index_encode_table])
            init_char = next_char
        next_char = ''
    for i in range(len(encode_table)):
        if sequence[-1] == encode_table[i][0]:
            encode_list.append(encode_table[i][1])
    print("Alphabet", end = "\t")
    print("Index")
    print("-------------------------------")
    for i in range(len(encode_table)):
        for j in range(2):
            print("  ", encode_table[i][j], end = "\t\t")
        print()
    encoded_sequence = ''
    for i in range(len(encode_list)):
        encoded_sequence = encoded_sequence + str(encode_list[i]) + ' '
    print("Encoded output sequence for the sequence " + sequence + " is: " + encoded_sequence)
    return [init_dict, encode_list]
    

def LZW_decode(master_directory):
    init_dict = master_directory[0]
    encode_list = master_directory[1]
    decode_table = []
    for i in init_dict.items():
        decode_table.append([i[0], i[1]])
    decode_sequence = ''
    old = encode_list[0]
    seq = ''
    for i in range(len(decode_table)):
        if int(old) == int(decode_table[i][1]):
            seq = str(decode_table[i][0])
    cal = ''
    cal = cal + str(seq[0])
    decode_sequence = decode_sequence + seq
    index_decode_table = len(decode_table)
    for i in range(len(encode_list) - 1):
        new = encode_list[i + 1]
        flag = 1
        for j in range(len(decode_table)):
            if int(new) != int(decode_table[j][1]):
                flag = 0
        if flag == 1:
            for k in range(len(decode_table)):
                if int(old) == int(decode_table[k][1]):
                    seq = str(decode_table[k][0])
            seq = seq + cal
        else:
            for l in range(len(decode_table)):
                if int(new) == int(decode_table[l][1]):
                    seq = str(decode_table[l][0])
        decode_sequence = decode_sequence + seq
        cal = ''
        cal = cal + seq[0]
        for m in range(len(decode_table)):
            if int(old) == int(decode_table[m][1]):
                old_seq = decode_table[m][0]
        index_decode_table = index_decode_table + 1
        decode_table.append([str(old_seq + cal), index_decode_table])
        old = new
    print("Deocoded Sequence is: ", decode_sequence)
         
        
n = int(input("Enter the number of alphabets in sequence: "))
initial_dictionary = dict()
for i in range(n):
    alpha = input("Enter alphabet: ")
    ind = int(input("Enter index: "))
    initial_dictionary[alpha] = ind
sequence = input("Enter the sequence to be encoded: ")
master_directory = LZW_encode(initial_dictionary, sequence)
LZW_decode(master_directory)
