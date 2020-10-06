import heapq
from collections import defaultdict

def huffman(freq):
    heap = [[w, [sym, '']] for sym, w in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for val in left[1:]:
            val[1] = '0' + val[1]
        for val in right[1:]:
            val[1] = '1' + val[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))



stri = input("Enter the string to be encoded:")
freq = defaultdict(int)
for i in stri:
    freq[i] = freq[i] + 1
    
huff = huffman(freq)
print("Character\tWeight\tHuffman Code")

for i in huff:
    print(i[0] + "\t" + str(freq[i[0]]) + ("\t") + i[1])


