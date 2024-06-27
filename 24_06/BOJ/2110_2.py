import sys

'''
이분탐색으로 풀어야함
탐색 목표를 설치거리로 설정

첫번째 좌표 + 설치거리보다 같거나 큰 값의 집 좌표가 있으면 cnt++을 한다
(첫번째 집에는 공유기 설치하니까 cnt=1로 초기화)

집 좌표 배열을 순회 후 cnt를 기준으로 설치할 공유기 개수 보다 많거나 같으면
일단 결과 값으로  mid저장, min_DST를 mid+1로 설정 후 반복
아니면 max_DST를 mid-1로 해서 다시 반복 돌림
반복 실행 후 min_DST가 max_DST 같거나 커질때
result값이 조건을 만족하는 최대 설치거리가 된다.
'''
N, C = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

min_DST = 1
max_DST = arr[-1] - arr[0]
result = 0

while(min_DST <= max_DST):
    mid = (min_DST + max_DST) // 2
    coord = arr[0]
    cnt = 1

    for i in range(1, N):
        if arr[i] >= coord + mid:
            coord = arr[i]
            cnt += 1

    if cnt >= C:
        min_DST = mid + 1
        result = mid

    else:
        max_DST = mid - 1

print(result)
