T = int(input())
for tc in range(1, T+1):
    cnt = [0] * 1001
    N = int(input())
    for _ in range(N):
        bus_type, A, B = map(int, input().split())
        cnt[A] += 1
        cnt[B] += 1

        if bus_type == 1:
            for i in range(A+1, B):
                cnt[i] += 1

        if bus_type == 2:
            if A % 2 == 0:
                for i in range(A+1, B):
                    if i % 2 == 0:
                        cnt[i] +=1
            else:
                for i in range(A+1, B):
                    if i%2 == 1 :
                        cnt[i] +=1

        if bus_type == 3:
            if A % 2 == 0:
                for i in range(A+1, B):
                    if (i % 4) == 0:
                        cnt[i] +=1
            else:
                for i in range(A+1, B):
                    if i%3 == 0 and i%10 !=0:
                        cnt[i] +=1

    print(f'#{tc} {max(cnt)}')
