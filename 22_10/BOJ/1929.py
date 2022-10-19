import math

def sosu(x):
    if x == 1:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
                break
        return True

m, n = map(int, input().split())
for j in range(m, n + 1):
    if sosu(j):
        print(j)

