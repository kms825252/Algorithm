import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    a = sys.stdin.readline().rstrip()
    if a == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif a == 'size':
        print(len(stack))

    elif a == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif a == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        b, c = a.split()
        stack.append(int(c))