N= int(input())
a = 2
while N != 1:
    if N % a != 0:
        a += 1
    else :
        N = N //a
        print(a)