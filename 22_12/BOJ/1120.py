a, b = input().split()


my_min = 51
for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j+i]:
            cnt +=1
    if my_min > cnt:
        my_min = cnt

print(my_min)