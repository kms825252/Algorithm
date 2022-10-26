n, m = map(int, input().split())
case1 = []
case2 = []
for i in range(n):
    case1.append(list(map(int, input().split())))

for j in range(n):
    case2.append(list(map(int, input().split())))

for k in range(n):
    for l in range(n):
        print(case1[k][l] + case2[k][l], end=' ')
    print()

print(case1)
print(case2)

# A, B = [], []
#
# N, M = map(int, input().split())
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)
#
# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()

