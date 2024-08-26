from sys import stdin as ss

'''
229084KB 4392ms 
참고
https://gsmesie692.tistory.com/113
'''

N, K = map(int, ss.readline().split())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, ss.readline().split())
    for j in range(1, K+1):
        if j < W:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)

print(dp[N][K])