import math
a,b,v = map(int, input().split())

v = v - a
day = math.ceil(v/(a-b))+ 1
print(day)