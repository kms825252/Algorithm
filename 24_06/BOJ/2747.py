from sys import stdin as ss

'''시간초과'''
# def solve(n):
#     num = 0
#     if n >= 2:
#         num = solve(n-2) + solve(n-1)
#
#     elif n == 1:
#         num = 1
#
#     return num
#
#
# n = int(ss.readline())
# print(solve(n))


'''31120KB 40ms'''
n = int(ss.readline())
a, b = 0, 1
while n > 0:
    a, b = b, a+b
    n -= 1

print(a)


