import sys

def sol(n):
    if n<1:
        return n
    x = n//3
    sol(x)
    for i in range(0,len(star), n):
        for j in range(0, len(star), n):
            for k in range(x+i, (2*x)+i):
                for m in range(x+j,(2*x)+j):
                    star[k][m] = ' '

    return star

n = int(sys.stdin.readline())
star = []
for _ in range(n):
    star.append(list('*' * n))

for i in range(n):
    print(''.join(sol(n)[i]))