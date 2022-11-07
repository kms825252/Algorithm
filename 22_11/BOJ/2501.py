a, b= map(int, input().split())
case = []
for i in range(1,a+1):
    if a % i == 0:
        case.append(i)
if len(case) >= b:
    print(case[b-1])
else:
    print(0)

