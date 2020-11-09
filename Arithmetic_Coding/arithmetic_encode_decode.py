import math

def float_bin(number, k):
    b = ""
    for x in range(k):
        number = number * 2
        if number > 1:
          b = b + str(1)
          x = int(number)
          number = number - x
        elif number < 1:
            b = b + str(0)
        elif number == 1:
            b = b + str(1)
            break
    return b


def tag_encode(alpha, prob, N, s):
    unity = []
    prob_range = 0.0
    for i in range(N):
        l = prob_range
        prob_range = prob_range + prob[i]
        u = prob_range
        unity.append([alpha[i], l, u])
    for i in range(len(s) - 1):
        for j in range(len(unity)):
            if s[i] == unity[j][0]:
                prob_low = unity[j][1]
                prob_high = unity[j][2]
                diff = prob_high - prob_low
                for k in range(len(unity)):
                    unity[k][1] = prob_low
                    unity[k][2] = prob[k] * diff + prob_low
                    prob_low = unity[k][2]
                break
    low = 0
    high = 0
    for i in range(len(unity)):
        if unity[i][0] == s[-1]:
            low = unity[i][1]
            high = unity[i][2]
    tag = (low + high) / 2
    print("Tag value for sequence is: ", tag)
    k = math.ceil(math.log((1/(high - low)),2) + 1)
    bin_code = float_bin(tag, k)
    print("Binary code for the sequence " + s + " is " + bin_code)
    return [tag, N, alpha, prob]


def tag_decode(master):
    tag = master[0]
    N = master[1]
    alpha = master[2]
    prob = master[3]
    unity = []
    prob_range = 0.0
    seq = ""
    for i in range(N):
        l = prob_range
        prob_range = prob_range + prob[i]
        u = prob_range
        unity.append([alpha[i], l, u])
    for i in range(N + 1):
        for j in range(len(unity)):
            if tag > unity[j][1] and tag < unity[j][2]:
                prob_low = unity[j][1]
                prob_high = unity[j][2]
                diff = prob_high - prob_low
                seq = seq + unity[j][0]
                for k in range(len(unity)):
                    unity[k][1] = prob_low
                    unity[k][2] = prob[k] * diff + prob_low
                    prob_low = unity[k][2]
                break
    print("The sequence for tag " + str(tag) + " is " + seq)
    
    
alphabet = []
probability = []
N = int(input("Enter number of letters in file: "))
for i in range(N):
    a = input("Enter the letter: ")
    p = float(input("Enter probability for " + a + ": "))
    alphabet.append(a)
    probability.append(p)
sequence = input("Enter the sequence to be encoded: ")
master = tag_encode(alphabet,probability, N, sequence)
tag_decode(master)
