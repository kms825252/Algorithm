T = int(input())
for i in range(1, T+1):
    odd_sum = 0
    num = list(map(int,(input().split())))
    for j in range(10):
        if num[j] % 2 == 1:
            odd_sum += num[j]
    print(f'#{i} {odd_sum}')