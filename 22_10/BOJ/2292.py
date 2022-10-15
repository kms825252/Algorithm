n = int(input())
i = 1
num = 1
if n == 1:
    print(1)
else:
    while True:
        num = num + 6*i
        if num >= n:
            break
        i += 1
    print(i+1)