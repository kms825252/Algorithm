import sys

num_list = [0]*91

def f(x):
    if num_list[x]:
        return num_list[x]

    else:
        if x <= 1:
            num_list[x] = x
            return num_list[x]
        else:
            num_list[x] = num_list[x-1] + num_list[x-2]
            return f(x-1) + f(x-2)

n = int(sys.stdin.readline())
print(f(n))