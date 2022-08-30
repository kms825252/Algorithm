T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    case = [list(map(int, input().split())) for _ in range(N)]

    max_r_cnt = 0
    for i in range(N):
        r_cnt = 1
        for j in range(M-1):
            if case[i][j] == 1 and case[i][j+1] == 1:
                r_cnt += 1
        max_r_cnt = max(max_r_cnt, r_cnt)



    max_c_cnt = 0
    for j in range(M):
        c_cnt = 1
        for i in range(N-1):
            if case[i][j] == 1 and case[i+1][j] == 1:
                c_cnt +=1
        max_c_cnt = max(max_c_cnt, c_cnt)

    print(max_r_cnt)
    print(max_c_cnt)
    print(f'#{tc} {max(max_r_cnt, max_c_cnt)}')


