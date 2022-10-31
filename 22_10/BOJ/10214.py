t= int(input())
for _ in range(t):
    yon = 0
    kor = 0
    for i in range(9):
        a, b = map(int, input().split())
        yon += a
        kor += b

    if yon > kor :
        print('Yonsei')
    elif yon < kor:
        print('Korea')
    else:
        print('Draw')
