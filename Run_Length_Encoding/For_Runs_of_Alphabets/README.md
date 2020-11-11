<h1>Introducción</h1>
<br>
Run-length encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.
<br>
<hr>
<h1>How the Encoder Works???</h1>
<br>

The encoding part is embedded in the function rle_encode(takes string as input).

We start the implementation by breaking the continuous string into a two-dimensional nested list storing the character and it’s count in every iterated outer list for the number of alphabets. The two-dimensional list is made such that each recognized same character has its own separate nested list and for this the nested while loop takes in account that the count doesn’t differ, while the outer while loop iterates till the length of the string. After this process is finished for a single character, the count is reset to 0.
<br>
```<br>
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
```
<br>

The next part here comes to convert the count of each alphabet to its binary equivalent which is done by the bin_fix(count, num_of_places) function. The point is to use the number of bits for each count which is required to code the maximum count, i.e. Suppose that an alphabet 'd' has a count 50, so to convet 50 to it's binary equivalent we require log2(50) = 6 bits (ceil value). So, for all the counts, we will convert it using 6 bits, even if count is 1 (code will be 000001). 
<br>
```<br>
rle_max = max(rle, key=lambda x: x[1])
places_code = math.ceil(math.log(rle_max[1], 2))
for i in range(len(rle)):
    rle[i][1] = bin_fix(rle[i][1], places_code)
```
<br>
The bin_fix() function (the zfill(k) string function adds initial zeros upto k places).

<br><br>

```<br>
def bin_fix(n, k):
    num = bin(n)
    return num[2:].zfill(k)
```
<br>

Next, we create a unique list of alphabets and assign them their respective binary codes using the bin_fix() function. Here, the idea is to count the number of alphabets in the list first and then calculate the number of required bits to convert it into binary. For example, if we have 7 alphabets in the unique list, then we need log2(7) = 3 bits (ceil value) to convert them into respective binary code.

<br>

```<br>
for i in range(0,len(rle)):
    a = rle[i][0]
    if a not in alphabets:
        alphabets.append(a)
places_alpha = math.ceil(math.log(len(alphabets),2)) 
for i in range(len(alphabets)):
    numb = bin_fix(i, places_alpha)
    alpha_codes.append([alphabets[i],numb])
```
<br>

From this we then extract the binary codes for the alphabets and place them besides their equivalent binary count which we earlier calculated and return them in tuple form to represent parenthesis.
<br>
The return function returns the final tuple of encoded alphabets and their encoded counts along with the code list of the alphabets for the decoder function (this is how the encoder passes the compressed data to the decoder).
<br>

```<br>
for i in range(len(rle)):
    for j in range(len(alpha_codes)):
        if alpha_codes[j][0] == rle[i][0]:
            final_rle.append((alpha_codes[j][1],rle[i][1]))
final_rle = tuple(final_rle)
return [final_rle,alpha_codes]
```
<br>
<hr>
<br>
<h1>How the Decoder Works???</h1>
<br>
The decompressing part of Run Length Encoding can be done by obtaining the final tuple of encoded alphabets and their encoded counts along with the code list of the alphabets.

The return function returns a list of the required parameters for our rle-decode part and we store them in form of list values so that we can traverse more easily.

<br>

```<br>
def rle_decode(master_directory):
    final_str = []
    final_strg = ''
    str1 = []
    final_rle1 = master_directory[0]
    final_rle = list(map(list,final_rle1))
    alpha_codes = master_directory[1]
```
<br>
We first match the codes of the final tuple in the parameter with the codes of the alphabets as a parameter as well and store them in another list along with the encoded counts of respective alphabets.
<br>
```<br>
for i in range(len(final_rle)):
    for j in range(len(alpha_codes)):
        if alpha_codes[j][1] == final_rle[i][0]:
            str1.append([alpha_codes[j][0],final_rle[i][1]])
```
<br>

Now we convert the respective binary counts to their equivalent decimal counts. 
<br>

```<br>
for i in range(len(str1)):
    final_str.append([str1[i][0],int(str1[i][1],2)])
```
<br>
At last we return the string by concatenating the alphabets the number of times to their respective counts.

<br>

```<br>
for i in range(len(final_str)):
    for j in range(final_str[i][1]):
        final_strg = final_strg + str(final_str[i][0])
return final_strg
```
<br>
<hr>

<br>
<h1>The Driver Code!!!</h1>

<br>
The driver code inputs a string, prints it, calls the encoder function, stores it's return, print the encoded output and then prints the decoded output.

```<br>
str1 = input("Enter the string: ")
print("String to be encoded: ", str1)
master_directory = rle_encode(str1)
print("Run Length Encoding: ", master_directory[0])
print("Decoded string: ", rle_decode(master_directory))
```
<hr>


<h3>If you like this code and the explanation, make sure to leave a star on my repository.</h3>

