A = [1, 2, 5, 1, 5, 1 ]
freq = {}
for ele in A:
    freq[ele] = freq.get(ele, 0) + 1

print(freq)