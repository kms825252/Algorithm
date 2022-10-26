n = int(input())
case = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in case:
    if i == v :
        cnt +=1
print(cnt)