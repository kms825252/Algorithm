from sys import stdin as ss

'''31120KB 44ms'''
N = int(ss.readline())

num = 1
cnt = 0

while N > 0:
    N -= num
    num += 1

    if N < num:
        num = 1

    cnt += 1

print(cnt)