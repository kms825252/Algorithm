from sys import stdin as ss


'''31120KB 40ms
조건.모든 행과 모든 열에 한 명 이상의 경비원이 있어야 한다

경비원 1명을 추가 시 행과 열 모두 만족하는 곳에 경비원을 둘 수 있다.
그러면 행과 열 기준으로 필요 경비원을 각각 구하고 둘 중 더 큰 값을 구하면
최소 필요 경비원을 알 수 있다
'''
N, M = map(int, ss.readline().split())
arr = []

for i in range(N):
    arr.append(list(ss.readline().rstrip()))

# 행 기준 필요 경비원 구하기
row_cnt = 0
for i in range(N):
    flag = False
    for j in range(M):
       if arr[i][j] == 'X':
           flag = True
           break

    if not flag:
        row_cnt += 1

#열 기준 필요 경비원 구하기
colum_cnt = 0
for i in range(M):
    flag = False
    for j in range(N):
        if arr[j][i] == 'X':
            flag = True
            break

    if not flag:
        colum_cnt += 1

# 최소 경비원 구하기
print(max(row_cnt, colum_cnt))
