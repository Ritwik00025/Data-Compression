<h1>Introducción</h1>
<br>

Arithmetic coding maps a string of data (source) symbols to a code string in such a way that the original data can be recovered from the code string. The encoding and decoding algorithms perform arithmetic operations on the code string. 
<hr>
<br>

<h1>The Driver code!!!</h1>

The code first inputs the alphabets and their probabilities and the sequence to be encoded. This is then passed to the encoder function with the list of alphabets, their probability, the length of alphabet list (N) and the sequence to be encoded (this is the driver code).
<br>
```<br>

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

```
<br>

<hr>

<br>
<h1>How the Encoder Works???</h1>

The encoder function first creates a list which contains the alphabets along with the lower value and upper value of the particular letter (referred as unity list) forming in a range of 0 to 1.<br>

```<br>

def tag_encode(alpha, prob, N, s):
    unity = []
    prob_range = 0.0
    for i in range(N):
        l = prob_range
        prob_range = prob_range + prob[i]
        u = prob_range
        unity.append([alpha[i], l, u])

```
<br>
 

Now, for length of sequence – 1 time, a for loop first matches an alphabet from the sequence and the unity list. If a match is found, the region is expanded and the lower value of the letter becomes the lower value of the whole range and the upper value of the letter becomes the upper value of the whole range and an inner for loop then assigns the new lower and upper values to all the characters and the changes these values in the unity list. 
<br>
 ```<br>
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

 
 ```
 <br>

We, then calculate the tag for the last letter for the sequence by taking the lower and higher values and tag is given by their arithmetic mean. Now the value of number of bits is calculated by taking the ceil of log on base 2 for (1 / upper – lower) + 1. 

```<br>
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
```

<br>

The float_bin function changes the corresponding floating number to its equivalent binary code will k bits.


```<br>
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
```

<br>
The encoder returns the list of alphabets, their probabilities, the value of N and the tag value.
<br>


<hr>

<br>
<h1>How the Decoder Works???</h1>
 
<br>

Moving on to the decoder function. It first creates a list which contains the alphabets along with the lower value and upper value of the particular letter (referred as unity list) forming in a range of 0 to 1.

<br>

```<br>
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
```
<br>

Now, for N + 1 time, a for loop first matches the tag value and checks for which alphabet range it lies from the unity list. If a match is found, the region is expanded and the lower value of the letter becomes the lower value of the whole range and the upper value of the letter becomes the upper value of the whole range and an inner for loop then assigns the new lower and upper values to all the characters and the changes these values in the unity list. We also concatenate the corresponding alphabet to the sequence which is the original sequence.

<br>

```<br>
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
```
<br>
<hr>

<h3>If you like this code and the explanation, make sure to leave a star on my repository.😁</h3>
