from itertools import permutations

n, m = map(int, input().split())
num = list(range(1,n+1))
perm = permutations(num, m)
for i in perm:
    for j in i:
        print(j, end=" ")
    print()