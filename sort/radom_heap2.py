import random
random.seed('class_04')
array = [random.randrange(1000) for _ in range(10)]
#array.append(1000)
l_arr = len(array)
maxv = max(array)
print(array,maxv)
result = array[:]

div = 1
while div <= maxv:
    counts = [ 0 ] * 10
    for v in array:
        digit = v // div % 10
        counts[digit] += 1

    for i in range(len(counts) - 1):
        counts[i + 1] += counts[i]

    for i in range(l_arr - 1, -1, -1):
        v = array[i]
        digit = v // div % 10
        counts[digit] -= 1
        ri = counts[digit]
        result[ri] = v
    array = result[:]
    print(array, div)

    div*=10

exit()

counts = [0 for _ in range(maxv + 1)]
print(counts, len(counts))
for v in array:
    counts[v] += 1
print(counts, len(counts))

for i in range(len(counts) -1):
    counts[i+1] += counts[i]

print(counts, len(counts))
#result = [None for _ in range(l_arr)]
#result = [None] * l_arr
result = array[:]
for i in range(l_arr - 1, -1, -1):
    v= array[i]
    counts[v] -= 1
    ri = counts[v]
    result[ri] = v

print(result)
