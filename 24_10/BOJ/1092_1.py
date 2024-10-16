from sys import stdin as ss


'''
32140KB 116ms

모든 박스를 배로 옮기는데 드는 최소 시간 구하기

조건
1. 크레인은 1분에 1개의 박스만 옮길 수 있다
2. N개의 크레인은 각각 무게 제한이 있다
'''

N = int(ss.readline())
crane_weight = list(map(int, ss.readline().split()))
M = int(ss.readline())
box_weight = list(map(int, ss.readline().split()))

crane_weight.sort(reverse=True)
box_weight.sort(reverse=True)


min_time = 0
box_idx = [0]*(N+1)
cnt = 0
check = [True for _ in range(M)]

if crane_weight[0] < box_weight[0]:
    print(-1)

else:
    while M > cnt:
        for i in range(1, N+1):
            if box_idx[i] == M or crane_weight[i-1] < box_weight[M-1]:
                continue

            if min_time == 0:
                idx = box_idx[i-1]

            else:
                idx = box_idx[i]

            for j in range(idx, M):
                if check[j] and crane_weight[i-1] >= box_weight[j]:
                    check[j] = False
                    box_idx[i] = j + 1
                    cnt += 1
                    break

            if cnt == M:
                break

        min_time += 1

    print(min_time)