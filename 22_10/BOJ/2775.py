t= int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    room = [0]
    for i in range(1, n+1):
        room.append(i)
    while k>0:
        for i in range(n):
            room[i+1] = room[i]+room[i+1]
        k -= 1
    print(room[n])

