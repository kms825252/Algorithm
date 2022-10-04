# arr = [1 ,2 ,3 ]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<< j):
#             print(arr[j], end = ' ')
#     print()
#

def perm(n,k):
    if n == k:
        print(p)
    else:
        for i in range(n,k):
            p[n], p[i] = p[i], p[n]
            perm(n+1,k)
            p[n], p[i] = p[i], p[n]

p=[1,2,3]
perm(0,3)