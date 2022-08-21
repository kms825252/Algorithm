T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())

    for i in range(max(A,B), (A*B)+1):
        if i % A ==0 and i % B == 0:
            print(i)
            break

#===================

# 유클리드 호제법

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x, y):
    result = (x*y) //gcd(x,y)
    return result

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(lcm(A, B))
