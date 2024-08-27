from sys import stdin as ss

'''
55708KB 520ms
'''

a = ss.readline().rstrip()
b = ss.readline().rstrip()
dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[len(a)][len(b)])