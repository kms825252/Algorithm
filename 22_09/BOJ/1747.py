import math
import sys

def isPrime(n):
    if n ==1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

num = int(sys.stdin.readline())
flag = 1

while True:
    if isPrime(num):
        num = str(num)
        for i in range(len(num)//2):
            if num[i] != num[-i-1]:
                flag = 0
                break



print(num)

# n = 1000000
# arr = [1] * n
#
# for i in range(2, int(math.sqrt(n))+1):
#     if arr[i] == 1:
#         j = 2
#         while i*j <=n:
