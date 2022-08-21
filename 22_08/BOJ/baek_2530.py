A, B, C= map(int, input().split())
D = int(input())

if C + D >= 60:
    C = C + D - (((C + D)//60) * 60)
    B += ((C + D)//60)
else :
    C = C + D

print((C+D) // 60)
print(B)

# if B >= 60:
#     B = B - ((B//60) * 60)
#     A += B // 60

# if A >= 24:
#     A = A % 24

# print(A, B, C)