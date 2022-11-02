case = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        case.append(num)
if case:
    print(sum(case))
    print(min(case))
else:
    print(-1)

