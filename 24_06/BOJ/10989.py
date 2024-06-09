from sys import stdin as ss

'''선택정렬 메모리초과'''


def select_sort(ary):
    for i in range(len(ary)):
        min_idx = i
        for j in range(i, len(ary)):
            if ary[min_idx] > ary[j]:
                min_idx = j
        ary[i], ary[min_idx] = ary[min_idx], ary[i]
    return ary


'''버블정렬 메모리 초과'''


def bubble_sort(ary):
    for i in range(len(ary)-1):
        for j in range(0, len(ary)-1-i):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]

    return ary


'''병합정렬 메모리 초과'''


def merge_sort(ary):
    if len(ary) > 1:
        mid = len(ary) // 2
        left = ary[:mid]
        right = ary[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ary[k] = left[i]
                i += 1

            else:
                ary[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            ary[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ary[k] = right[j]
            j += 1
            k += 1

    return ary


n = int(ss.readline())
arr = []

for _ in range(n):
    num = int(ss.readline())
    arr.append(num)

merge_sort(arr)

for k in range(n):
    print(arr[k])

