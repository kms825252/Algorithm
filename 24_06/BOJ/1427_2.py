from sys import stdin as ss

n = ss.readline().rstrip()

for i in range(9, -1,-1):
    for j in n:
        if int(j) == i:
            print(j, end='')
