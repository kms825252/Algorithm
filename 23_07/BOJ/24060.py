import sys
input = sys.stdin.readline

def merge_sort(arr):
    global cnt, K
    if len(arr) < 2:
        return arr

    mid = (len(arr) + 1) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    l = h = 0
    merge_arr = []
    while l < len(low_arr) and h < len(high_arr):
        cnt += 1
        if low_arr[l] < high_arr[h]:
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[h])
            h += 1
        if cnt == K:
            print(merge_arr[-1])


    for i in range(len(low_arr)-l):
        merge_arr.append(low_arr[l])
        l += 1
        cnt +=1
        if cnt == K:
            print(merge_arr[-1])
    for i in range(len(high_arr) - h):
        merge_arr.append(high_arr[h])
        h += 1
        cnt += 1
        if cnt == K:
            print(merge_arr[-1])
    return merge_arr

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
merge_sort(arr)
if cnt < K:
    print(-1)
