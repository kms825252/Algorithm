N = int(input())

case =[list(map(int, input().split())) for _ in range(N)]

for i in range(len(case)):
    k = 1
    for j in range(len(case)):
        if case[i][0] < case[j][0] and case[i][1] < case[j][1]:
            k += 1
    print(k, end=' ')

