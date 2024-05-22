n = input().split()
num = []
check = []

for i in n:
    num.append(int(i))

for i in range(7):
    if num[i] < num[i+1]:
        check.append(0)

    else:
        check.append(1)

if sum(check) == 0:
    print('ascending')

elif sum(check) == 7:
    print('descending')

else:
    print('mixed')