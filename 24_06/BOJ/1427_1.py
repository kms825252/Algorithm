from sys import stdin as ss

n = list(map(int, ss.readline().rstrip()))

for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[j] > n[i]:
            n[j] , n[i] = n[i], n[j]


n = list(map(str, n))
print(''.join(n))
