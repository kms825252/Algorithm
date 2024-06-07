from sys import stdin as ss

"""리스트 버블 정렬 - 시간초과"""
# n = int(ss.readline())
# member = []
#
# for i in range(n):
#     age, name = ss.readline().rstrip().split()
#     age = int(age)
#     member.append([i, age, name])
#
# for i in range(n-1):
#     for j in range(n-i-1):
#         if member[j][1] > member[j+1][1]:
#             member[j], member[j+1] = member[j+1], member[j]
#
# for i in member:
#     print(i[1], i[2])


"""리스트 선택 정렬 - 시간 초과"""
# n = int(ss.readline())
# member = []
#
# for i in range(n):
#     age, name = ss.readline().rstrip().split()
#     age = int(age)
#     member.append([i, age, name])
#
# for i in range(n):
#     min_idx = i
#     for j in range(i, n):
#         if member[j][1] < member[i][1]:
#             min_idx =j
#
#     member[i], member[min_idx] = member[min_idx], member[i]
#
# for i in member:
#     print(i[1], i[2])


"""딕셔너리 sorted - 61104KB 320ms"""
# n = int(ss.readline())
# member = {}
#
# for i in range(n):
#     age, name = ss.readline().rstrip().split()
#     age = int(age)
#     member[i] = age, name
#
# member = sorted(member.items(), key=lambda x: x[1][0])
#
# for i in member:
#     print(i[1][0], i[1][1])


"""리스트 sorted - 53068KB 328ms"""
# n = int(ss.readline())
# member = []
#
# for i in range(n):
#     age, name = ss.readline().rstrip().split()
#     age = int(age)
#     member.append([i, age, name])
#
# member = sorted(member, key=lambda x: x[1])
#
# for i in member:
#     print(i[1], i[2])


"""리스트 sort - 52284KB 304ms"""
# n = int(ss.readline())
# member = []
#
# for i in range(n):
#     age, name = ss.readline().rstrip().split()
#     age = int(age)
#     member.append([i, age, name])
#
# member.sort(key=lambda x: x[1])
#
# for i in member:
#     print(i[1], i[2])


"""나동빈 - 46140KB 252ms"""
n = int(ss.readline())
member = []

for _ in range(n):
    a = ss.readline().rstrip().split()
    member.append((int(a[0]), a[1]))

member.sort(key=lambda x: x[0])

for i in member:
    print(i[0], i[1])

"""
tuple은 list와 달리 여유공간 메모리를 할당하지 않기 때문에
정적인 데이터를 쓸때 튜플로 하는게 효과적이다.
"""