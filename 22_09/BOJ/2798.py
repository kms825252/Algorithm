N, M = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            my_sum = card[i] + card[j] + card[k]
            if my_sum <= M:
                max_sum = max(max_sum, my_sum)

print(max_sum)