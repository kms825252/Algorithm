# def fibo_dp(n):
#     table[0] = 0
#     table[1] = 1
#     for i in range(2, n+1):
#         table[i] = table[i-1] + table[i-2]
#     return
#
# table = [0]*101
# fibo_dp(100)
# print(table[20])


a = 0
b = 1
n = 20
for _ in range(n-1):
    a, b = b, a+b

print(b)