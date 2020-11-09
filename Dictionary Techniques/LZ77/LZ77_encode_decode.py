def LZ77_encode(dictionary, sequence, len_code, search_buf_length, look_ahead_buf_length):
    str_length = len(sequence)
    search_buf_pos, look_ahead_buf_pos = 0, search_buf_length
    encode_list = []
    buffer = sequence[search_buf_pos:search_buf_pos+search_buf_length]
    for i in buffer:
        encode_list.append([0,0,dictionary[i]])
    buffer = buffer + sequence[look_ahead_buf_pos:look_ahead_buf_pos+look_ahead_buf_length]
    while 1:
        sym_offset = search_buf_length
        max_length, max_offset, next_sym = 0, 0, buffer[sym_offset]
        buffer_length = len(buffer)
        if buffer_length - sym_offset == 1:
            encode_list.append([0,0,dictionary[next_sym]])
            step = max_length + 1
            search_buf_pos =  search_buf_pos + step
            look_ahead_buf_pos = look_ahead_buf_pos + step
            buffer = sequence[search_buf_pos:search_buf_pos+search_buf_length+look_ahead_buf_length]
        else:    
            for offset in range(1,search_buf_length+1):
                pos = sym_offset - offset
                n = 0
                while buffer[pos + n] == buffer[sym_offset + n]:
                    n += 1
                    if n == buffer_length - search_buf_length - 1: break
                if max_length < n:
                    max_length = n
                    max_offset = offset
                    next_sym = buffer[sym_offset+n]
            encode_list.append([max_offset, max_length, dictionary[next_sym]])
            step = max_length + 1
            search_buf_pos =  search_buf_pos + step
            look_ahead_buf_pos = look_ahead_buf_pos + step
            buffer = sequence[search_buf_pos:search_buf_pos+search_buf_length+look_ahead_buf_length]
            if look_ahead_buf_pos >= str_length: break
    print("Offset\tLength\tCodeword")
    print("-----------------------------------")
    for i in range(len(encode_list)):
        for j in range(3):
            print("   " + str(encode_list[i][j]), end = "\t")
        print()
    return [encode_list, dictionary, len_code]


def LZ77_decode(master_directory):
    encode_list = master_directory[0]
    dictionary = master_directory[1]
    len_code = master_directory[2]
    decoded_sequence = ""
    alpha_coded = []
    for item in dictionary.items():
        alpha_coded.append([item[0], item[1]])
    for i in range(len(encode_list)):
        for j in range(len(alpha_coded)):
            if encode_list[i][2] == alpha_coded[j][1]:
                encode_list[i][2] = alpha_coded[j][0]
    for i in encode_list:
        offset, length, symbol = i
        for j in range(length):
            decoded_sequence += decoded_sequence[-offset]
        decoded_sequence += symbol
    print("The original sequence is: ", decoded_sequence)
 

n = int(input("Enter the number of characters in dictionary: "))
dictionary = dict()
for i in range(n):
    alphabet = input("Enter alphabet: ")
    codeword = input("Enter codeword: ")
    len_code = len(codeword)
    dictionary[alphabet] = codeword
sequence = input("Enter the sequence to be coded: ")
search_buffer_length = int(input("Enter the size of search_buffer: "))
look_ahead_buffer_length = int(input("Enter the size of the look ahead buffer: "))
master_directory = LZ77_encode(dictionary, sequence, len_code, search_buffer_length, look_ahead_buffer_length)
LZ77_decode(master_directory)
