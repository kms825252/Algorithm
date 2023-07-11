n = int(input())

def f(x):
    if x>=2:
        return f(x-1) + f(x-2)
    elif x==1:
        return 1
    else:
        return 0

print(f(n))