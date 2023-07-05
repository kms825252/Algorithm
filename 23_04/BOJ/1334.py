import sys

n = int(sys.stdin.readline())

def isPal(x):
    num = str(x)
    if num == num[::-1]:
        return True
    else:
        return False

while True:
    n = n + 1
    if isPal(n):
        break

print(n)
