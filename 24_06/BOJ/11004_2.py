from sys import stdin as ss

'''나동빈 657572KB 3868ms'''
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


n, k = map(int, ss.readline().split())
array = list(map(int, ss.readline().split()))
array = merge_sort(array)
print(array[k-1])

132