import sys

N = int(sys.stdin.readline())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
case.sort(key=lambda x: x[0])
case.sort(key=lambda x: x[1])

for i in range(len(case)):
    if case[i] == [0, 0]:
        continue
    for j in range(i+1,len(case)):
        if case[i][1] > case[j][0]:
            case[j] = [0,0]

cnt = 0
for i in range(len(case)):
    if case[i] != [0, 0]:
        cnt += 1
print(cnt)