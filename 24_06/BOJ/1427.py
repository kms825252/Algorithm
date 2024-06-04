from sys import stdin as ss

n = list(map(int, ss.readline().rstrip()))
n.sort(reverse=True)

n = list(map(str, n))
print(''.join(n))
