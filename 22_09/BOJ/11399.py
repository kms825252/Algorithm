N = int(input())
case = list(map(int, input().split()))
case.sort()

my_sum = 0
time_sum = 0
for i in case:
    my_sum += i
    time_sum += my_sum

print(time_sum)
