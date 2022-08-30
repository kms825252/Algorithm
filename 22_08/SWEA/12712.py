T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    case =[]
    for _ in range(N):
        case.append(list(map(int, input().split())))
    max_kill_fly = 0

    for i in range(N):
        for j in range(N):
            kill_fly = 0
            kill_fly += case[i][j]
            a = 1
            while a < M :
                di = [0, a, 0, -a]
                dj = [a, 0, -a, 0]
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < N and 0<= nj < N:
                        kill_fly += case[ni][nj]
                a += 1
            max_kill_fly = max(max_kill_fly, kill_fly)

    for i in range(N):
        for j in range(N):
            kill_fly = 0
            kill_fly += case[i][j]
            a = 1
            while a < M:
                di = [a, a, -a, -a]
                dj = [a, -a, a, -a]
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        kill_fly += case[ni][nj]
                a += 1
            max_kill_fly = max(max_kill_fly, kill_fly)

    print(f'#{tc} {max_kill_fly}')
