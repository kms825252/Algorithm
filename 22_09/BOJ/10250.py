T = int(input())
for tc in range(1, T+1):
    H, W ,N = map(int, input().split())
    room = []
    for i in range(1,W+1):
        for j in range(1, H+1):
            room.append(j*100 + i)
    print(room[N-1])