N, M = map(int, input().split())
case = [list(input()) for _ in range(N)]
# w로 시작할때 잘못된 것: cnt1
# b로 시작할때 잘못된 것 : cnt2

min_cnt1 = 99999
min_cnt2 = 99999
for i in range(N-8 + 1):
    for j in range(M-8 + 1):
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            for l in range(8):
                if k%2 == 0:
                    if l%2 == 0 and case[i+k][j+l] != 'W':
                        cnt1 +=1

                    elif l%2 == 1 and case[i+k][j+l] != 'B':
                        cnt1 +=1

                else:
                    if l%2 == 0 and case[i+k][j+l] != 'B':
                        cnt1 +=1
                    elif l%2 == 1 and case[i+k][j+l] != 'W':
                        cnt1 +=1
        min_cnt1 = min(min_cnt1, cnt1)

        for k in range(8):
            for l in range(8):
                if k%2 == 0:
                    if l%2 == 0 and case[i+k][j+l] != 'B':
                        cnt2 +=1

                    elif l%2 == 1 and case[i+k][j+l] != 'W':
                        cnt2 +=1

                else:
                    if l%2 == 0 and case[i+k][j+l] != 'W':
                        cnt2 +=1
                    elif l%2 == 1 and case[i+k][j+l] != 'B':
                        cnt2 +=1

        min_cnt2 = min(min_cnt2, cnt2)

print(min(min_cnt1, min_cnt2))