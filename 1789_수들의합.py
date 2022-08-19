S = int(input())
N = 1
while True:
    if S - N >= 0:
        S = S - N
        N += 1
    else:
        N = N + S
        break

print(N)