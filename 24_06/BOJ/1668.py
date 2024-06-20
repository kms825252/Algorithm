from sys import stdin as ss

'''31120KB 32ms'''
N = int(ss.readline())
arr = []
left_cnt = 0
right_cnt = 0
big = 0

for i in range(N):
    arr.append(int(ss.readline()))
    if big < arr[i]:
        left_cnt += 1
        big = arr[i]

big = 0
for j in range(N-1, -1, -1):
    if big < arr[j]:
        right_cnt += 1
        big = arr[j]

print(left_cnt)
print(right_cnt)
