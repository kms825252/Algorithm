from sys import stdin as ss

n = int(ss.readline())
array = set(map(int, ss.readline().split()))
m = int(ss.readline())
x = list(map(int, ss.readline().split()))
for i in x:
    if i in array:
        print('1')
    else:
        print('0')
