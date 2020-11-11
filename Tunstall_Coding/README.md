<h1>Introducción</h1>
<br>
Tunstall coding is a form of entropy coding used for lossless data compression. Tunstall coding is a code which maps source symbols to a fixed number of bits. It is a variable to fixed length code.
<br>
<hr>
<br>
<h1>The Driver Code!!!</h1>
<br>
The code inputs the number of bits required to be encoding the letters and the string to be encoded. The string is further stored into the dictionary and from there we calculate the probability of each character and store the character and their respective probabilities in two different lists. The iteration count is calculated and stored in variable k. The length of letters is stored in variable N. 
<br>

```<br>
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
makefile = tunstall_encode(alphabet, probability, k, N, n, string)
print(tunstall_decode(makefile))
```
<br>
<hr>
<br>
<h1>How the Encoder Works???</h1>
<br>
The tunstall_encode() takes the lists of alphabets and their probabilities along with k, N, n and the string as parameters and returns the make-file, consisting of the encoded string (result), the 2d list of alphabets and the codewords assigned to them and the number of fixed code bits. 

This starts of with the creation of a 2d list final in which the alphabets and their probabilities are stored. Then for k iterations, we find the element with the maximum probability by sorting the list final for the final[i][1] index, and store it in the list last. The alphabet and the probability stored in the list last is concatenated (for the alphabet) and multiplied (for the probability) with all the alphabets and probabilities of the list final respectively and the alphabet and probability of the list last is removed form the original final list. 

<br>

```<br>
def tunstall_encode(alpha, prob, k, N, n, string):
    final = []
    for i in range(N):
        final.append([alpha[i], prob[i]])
    for i in range(k):
        last = max(final, key = lambda x:x[1])
        for i in range(N):
            final.append([last[0] + alpha[i], last[1] * prob[i]])
        final.pop(final.index(last))
```
<br>

Next, a function binary_fix() rounds off the binary sequence generated for the final sequence of alphabets stored in the list final to n number of bits. The zfill() string method adds preceding zero’s to the binary sequence and the bin() method converts the base 10 decimal numbers to base 2 binary numbers. 

<br>

```<br>
def binary_fix(i, n):
    binary = bin(i)
    return binary[2:].zfill(n)
```
<br>

This function is looped to fix the binary sequence to n bits of the list final and thus assign codewords. 
<br>

```<br>
for i in range(len(final)):
    final[i][1] = binary_fix(i, n)
```
<br>

Next, since we got the codewords for the combination of letters by tunstall code algorithm, we convert the string to it unique binary tunstall fixed length code. For this we convert the string into a list stri. The for loop is then used to find the pattern that matches between the list stri and the letters in the list final. If there is a match, we add the codeword to the string encode, else we merge the current element to the next element of the list stri to search for different patterns and if a merged pattern is found, we assign it the respective codeword and so on. In the end we return the make-file as a list of encode string, the list final and the value of n.

<br>

```<br>
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
```
<br>
<hr>
<br>
<h1>How the Decoder Works???</h1>
<br>

The tunstall_decode() takes the make-file as the parameter. We now open up the make-file to separate the contents in the list by storing value of number of bits in variable n, the list of alphabets and codewords in the variable final and the encoded string into a list separating by n bits, i.e. each n-bit in the string is stored at a specific index in the list decode. 
 
Again, we search the pattern for the codewords in the list decode and list final. If there is a match, we concatenate the corresponding alphabet into the variable string (which is an empty string) the at the end we print it to get the original string.

<br>

```<br>
def tunstall_decode(makefile):
    encode = makefile[0]
    final = makefile[1]
    n = makefile[2]    
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
```
<br>
<hr>
<br>


<h3>If you like the code and the explanation, make sure to leave a star on my repository.😁</h3>


