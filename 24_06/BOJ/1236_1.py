from sys import stdin as ss


'''31120KB 32ms
arr를 전체 순회할 때 행 기준, 열 기준 경비원 파악
1236.py에 비해 전체순회를 1번만 하기 때문에 8ms 더 빠르다
'''
N, M = map(int, ss.readline().split())

arr = [ss.readline().rstrip() for _ in range(N)]

row_check = [0] * N
colum_check = [0] * M

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            row_check[i] = 1
            colum_check[j] = 1

row_cnt = 0
for i in range(N):
    if row_check[i] == 0:
        row_cnt += 1

colum_cnt = 0
for i in range(M):
    if colum_check[i] == 0:
        colum_cnt += 1

print(max(row_cnt, colum_cnt))