import sys

N, C = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

start = arr[1] - arr[0]
end = arr[-1] - arr[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

print(result)

