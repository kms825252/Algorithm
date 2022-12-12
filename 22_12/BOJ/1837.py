a, b = map(int,input().split())

for i in range(2,b):
    if a%i == 0:
        num1 = i
        print(f'BAD {num1}')
        break

else:
    print('GOOD')