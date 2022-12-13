n = int(input())
score = list(map(int, input().split()))

num = 0
my_sum = 0
for i in range(len(score)):
    if score[i] == 1:
       num += 1
       my_sum += num

    else:
       num = 0

print(my_sum)