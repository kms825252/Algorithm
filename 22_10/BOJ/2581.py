import math


def sosu(x):
    if x == 1:
        return False

    elif x == 2 or x ==3:
        return True

    elif x >3:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True


m = int(input())
n = int(input())

sosu_list = []
for j in range(m, n+1):
    if sosu(j):
        sosu_list.append(j)

if sosu_list:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)

