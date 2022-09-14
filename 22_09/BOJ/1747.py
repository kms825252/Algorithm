import math
import sys

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

num = int(sys.stdin.readline())

a= 0
for i in range(num, 1000001):
    if i == 1:
        continue
    i = str(i)
    if i == i[::-1]:
        i= int(i)
        if isPrime(i):
            a = i
            break

if a == 0:
    a = 1003001
print(a)