import math
from collections import Counter
import time
import sys

def binary_fix(i, num_bits):
    binary = bin(i)
    return binary[2:].zfill(num_bits)

def tunstall_encode(alpha, prob, k, N, num_bits, string):
    
    t1 = time.time()

    table = []
    for i in range(N):
        table.append([alpha[i], prob[i]])
    for i in range(k):
        last = max(table, key = lambda x:x[1])
        table.remove(last)
        for i in range(N):
            table.append([last[0] + alpha[i], last[1] * prob[i]])
    for i in range(len(table)):
        table[i][1] = binary_fix(i, num_bits)
    unused = binary_fix(i+1,num_bits)
        
    chars = list(string)
    encoded = ""
    for i in range(len(chars)):
        done = False
        for j in range(len(table)):
            if chars[i] == table[j][0]:
                encoded = encoded + str(table[j][1])
                done = True
                break
        if not done:
            if i+1>=len(chars):
                encoded += unused
                table.append((chars[i],unused))
                continue
            chars[i+1] = str( chars[i] + chars[i+1] )

    t2 = time.time()

    print("The set of alphabets and codes are: ")
    print("Alphabet\tCode")
    print("-------------------------")
    for i in range(len(table)-1):
        print(table[i][0],'\t',table[i][1])

    print("Generated tunstall code for string " + string + " is: " + encoded)
    return [encoded, table, num_bits], (t2-t1)

def tunstall_decode(result):
    
    t1 = time.time()

    encoded = result[0]
    table = result[1]
    num_bits = result[2]    
    chunks = [encoded[num_bits*k:num_bits*(k+1)] for k in range(int(len(encoded)/num_bits))]
    
    string = ""
    for i in range(len(chunks)):
        for j in range(len(table)):
            if chunks[i] == str(table[j][1]):
                string = string + table[j][0]
                break

    t2 = time.time()

    print("---------------------------------------------------------------")
    print("Decoded string is:", string)
    return (t2-t1)

def main():

    if not (2 <= len(sys.argv) <= 3):
        print("[ Usage : ] python tun_enc_doc.py {num_bits}")
        print("or")
        print("[ Usage : ] python tun_enc_doc.py {num_bits} {filepath}")
        return

    num_bits = int(sys.argv[1])
    filepath = None
    string = ''
    if len(sys.argv)==3:
        filepath = sys.argv[2]
        with open(filepath, 'r') as f:
            string = f.read()
    else:
        string = input("Enter the string to be encoded: ")
    len_str = len(string)

    dictionary = dict()
    for i in string:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1
    
    N = len(dictionary)
    if 2**num_bits < N :
        raise Exception("not enough bits")

    alphabet = []
    probability = []
    for i in dictionary.items():
        alphabet.append(i[0])
        probability.append(i[1])
    for i in range(N):
        probability[i] = probability[i] / len_str
        
    k = math.floor(((2 ** num_bits) - N)/ (N - 1))
    result, exec_time = tunstall_encode(alphabet, probability, k, N, num_bits, string)

    table = result[1]
    bits_table = num_bits*len(result[1])
    for x,_ in table:
        bits_table+=(8*len(x))
    
    size_compressed = num_bits + int((len(result[0])-1)/8)+1 + bits_table
    size_original = len(string)*8
    ratio = size_compressed/size_original*100

    print("[+] Compression finished in %.5f seconds"% exec_time )
    print("[+] Compression ratio  %.1f"% ratio )

    exec_time = tunstall_decode(result)
    print("[+] Decompression finished in %.5f seconds"% exec_time )
    
if __name__ == '__main__':
	main()