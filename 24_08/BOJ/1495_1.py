from sys import stdin as ss

'''
N: 곡 개수
S: 시작볼륨
M: 최대볼륨
0 <= 볼륨 <= M

마지막 곡의 볼륨 최대값 구하기
마지막곡 연주 못하면 -1 출력

------------
평범한 배낭처럼 0 ~ M의 볼륨만큼의 캐시를 만들어서
각 노래마다 가능한 볼륨에 1(True)값을 준다.
만약 노래가 끝났는데 캐시에 1값이 없으면 -1 출력

순회가 끝나면 dp[N] 안에 있는 값을 거꾸로 순회하며 1일때 값을 출력하여
최대 볼륨을 구한다
'''

N, S, M = map(int, ss.readline().split())
songs = list(map(int, ss.readline().split()))
dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][S] = 1


for i in range(N):
    song = songs[i]
    for j in range(M+1):
        if dp[i][j] == 1:
            if j-song >= 0:
                dp[i+1][j-song] = 1
            if j+song <= M:
                dp[i+1][j+song] = 1

    if max(dp[i+1]) == 0:
        print(-1)
        break

for k in range(M, -1, -1):
    if dp[N][k] == 1:
        print(k)
        break