from sys import stdin as ss

'''657520KB 3708ms'''
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    l, r, a = 0, 0, 0
    while len(left_arr) != l and len(right_arr) != r:
        if left_arr[l] < right_arr[r]:
            arr[a] = left_arr[l]
            l += 1

        else:
            arr[a] = right_arr[r]
            r += 1

        a += 1

    if len(left_arr) == l:
        arr[a:] = right_arr[r:]

    else:
        arr[a:] = left_arr[l:]

    return arr


N, K = map(int, ss.readline().split())
num_list = list(map(int, ss.readline().split()))

merge_sort(num_list)
print(num_list[K-1])
