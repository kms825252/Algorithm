from sys import stdin as ss

n = int(ss.readline())
arr = []

for _ in range(n):
    x, y = map(int, ss.readline().split())
    arr.append((x, y))

'''51900KB 336ms '''
# arr.sort(key=lambda x: (x[0], x[1]))

'''52684KB 356ms'''
# arr = sorted(arr, key=lambda x: (x[0], x[1]))

'''44580KB 336ms'''
# arr.sort()

'''45364KB 320ms'''
arr = sorted(arr)

for i in arr:
    print(i[0], i[1])
