import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

answer = ['+']
stk = [1]
num = 2
order = 0
flag = True

while order< n:
    if not stk:
        stk.append(num)
        num += 1
        answer.append('+')

    elif stk[-1] == arr[order]:
        stk.pop()
        order += 1
        answer.append('-')

    elif stk[-1] < arr[order]:
        stk.append(num)
        num += 1
        answer.append('+')

    else:
        print('NO')
        flag = False
        break

if flag:
    for i in answer:
        print(i)
