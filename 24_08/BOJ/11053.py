from sys import stdin as ss

'''
31120KB 140ms
'''

N = int(ss.readline())
num = list(map(int, ss.readline().split()))
dp = [1] * (N)

for i in range(1, N):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))