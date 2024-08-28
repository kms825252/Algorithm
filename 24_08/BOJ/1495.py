from sys import stdin as  ss

'''
N: 곡 개수
S: 시작볼륨
M: 최대볼륨
0 <= 볼륨 <= M

마지막 곡의 볼륨 최대값 구하기
마지막곡 연주 못하면 -1 출력

메모리 초과
'''

N, S, M = map(int, ss.readline().split())
songs = list(map(int, ss.readline().split()))
dp = [[] for _ in range(N+1)]
dp[0].append(S)

for i in range(N):
    song = songs[i]
    for j in dp[i]:
        volum = j + song
        if volum <= M:
            dp[i+1].append(volum)

        volum = j - song
        if volum >= 0:
            dp[i+1].append(volum)

    if not dp[i+1]:
        print(-1)
        break

if dp[N]:
    print(max(dp[N]))