from sys import stdin as ss

'''계수정렬 메모리초과 
입력 받은 숫자를 리스트를 만들어서 다시 카운팅했기 때문에 메모리 초과
'''
# def counting_sort(ary):
#     array = [0] * 10001
#
#     for i in ary:
#         array[i] += 1
#
#     for i in range(10001):
#         if array[i] != 0:
#             for _ in range(array[i]):
#                 print(i)
#
#     return 0
#
#
# n = int(ss.readline())
# arr = []
#
# for _ in range(n):
#     num = int(ss.readline())
#     arr.append(num)
#
# counting_sort(arr)

'''나동빈 31120KB 10012ms'''

# n = int(ss.readline())
# count_arr = [0] * 10001
#
# for _ in range(n):
#     num = int(ss.readline())
#     count_arr[num] += 1
#
# for i in range(10001):
#     if count_arr[i] != 0:
#         for _ in range(count_arr[i]):
#             print(i)
#

'''함수로 만들어서 31120KB 8140ms'''

def counting_sort(n):
    count_arr = [0] * 10001

    for _ in range(n):
        num = int(ss.readline())
        count_arr[num] += 1

    for i in range(10001):
        if count_arr[i] != 0:
            for _ in range(count_arr[i]):
                print(i)

    return 0

n = int(ss.readline())
counting_sort(n)