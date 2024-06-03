from sys import stdin as ss

n = int(ss.readline())
array=[]
for i in range(n):
    array.append(int(ss.readline()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for k in array:
    print(k)