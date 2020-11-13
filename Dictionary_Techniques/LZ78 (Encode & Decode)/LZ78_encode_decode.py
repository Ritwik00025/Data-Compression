def LZ78_encode(dictionary, sequence):
    len_seq = len(sequence)
    index_dir = ['']
    encode_list = list()
    word = ''
    alphabet = list(dictionary.keys())
    codewords = list(dictionary.values())
    for i in sequence:
        word = word + i
        if not word in index_dir:
            index_dir.append(word)
            encode_list.append([index_dir.index(word[:-1]), word[-1]])
            word = ''
        elif i == len_seq:
            encode_list.append([index_dir.index(word), ''])
            word = ''
    for i in range(len(encode_list)):
        for j in range(len(alphabet)):
            if encode_list[i][1] == alphabet[j]:
                encode_list[i][1] = codewords[j]
    print("Index\tCodeword")
    print("------------------------------")
    for i in range(len(encode_list)):
        for j in range(2):
            print("  ", encode_list[i][j], end = "\t")
        print()
    return [encode_list, dictionary, index_dir]


def LZ78_decode(master_directory):
    encode_list = master_directory[0]
    dictionary = master_directory[1]
    index_dir = master_directory[2]
    alphabet = list(dictionary.keys())
    codewords = list(dictionary.values())
    for i in range(len(encode_list)):
        for j in range(len(codewords)):
            if encode_list[i][1] == codewords[j]:
                encode_list[i][1] = alphabet[j]
    decoded_sequence = ''
    for i in range(len(encode_list)):
        if encode_list[i][0] == '0':
            decoded_sequence = decoded_sequence + encode_list[i][1]
        else:
            decoded_sequence = decoded_sequence + str(index_dir[encode_list[i][0]])
            decoded_sequence = decoded_sequence + encode_list[i][1]
    print("The decoded sequence is: " + decoded_sequence)


n = int(input("Enter the number of characters in sequence: "))
dictionary = dict()
for i in range(n):
    alpha = input("Enter alphabet: ")
    code = input("Enter codeword: ")
    dictionary[alpha] = code
sequence = input("Enter the sequence to be coded: ")
master_directory = LZ78_encode(dictionary, sequence)
LZ78_decode(master_directory)
