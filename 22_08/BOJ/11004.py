def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i, j, k = 0, 0, 0
    while len(left) > i and len(right) > j :
        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
        else :
            arr[k] = left[i]
            i += 1
        k += 1
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    return arr

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr = merge_sort(arr)
print(arr[K-1])
