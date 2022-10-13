n= int(input())
cnt = n//5
while cnt>=0:
    n1 = n - cnt * 5
    if n1 % 3 == 0 :
        cnt = cnt + n1//3
        break
    cnt -= 1

print(cnt)