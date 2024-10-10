from sys import stdin as ss

'''
31120KB 32ms

change = [500, 100, 50, 10, 5, 1]
거스름돈 개수 적게

1000을 냈을때 잔돈의 개수 구하기

(1000 - 물건값) 에서 큰 단위의 돈부터 빼면 됨

'''

changes = [500, 100, 50, 10, 5, 1]
price = 1000 - int(ss.readline())
result = 0

for change in changes:
    while price >= change:
        price = price - change
        result += 1

print(result)