S = int(input())
N = 1
while True:
    if S - N >= 0:
        S = S - N
        N += 1
    else:
        N -= 1
        break

print(N)