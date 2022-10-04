# def f(i, k):
#     if i == k:      # 인덱스 i == 원소의 개수
#         print(p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j] , p[i]
#
# N = int(input())
# p = list(map(int,range(1,N+1)))
# f(0,N)

def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)
                used[j] = 0

N = int(input())
a = [i for i in range(1,N+1)]
used = [0]* N
p = [0] * N
f(0,N)