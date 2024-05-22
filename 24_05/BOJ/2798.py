from sys import stdin

n, m = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))
max_num = 0
num_sum = 0


for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            num_sum = num[i] + num[j] + num[k]
            if num_sum <= m and max_num < num_sum:
                max_num = num_sum

print(max_num)
