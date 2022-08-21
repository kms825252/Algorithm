T = int(input())

for i in range(1, T+1):
    box_num=int(input())
    box_list = list(map(int, input().split()))
    max_height = 0
    
    for j in range(box_num):
        cnt = 0
        for k in range(j+1, box_num):
            if box_list[j] > box_list[k]:
                cnt += 1
            
        if max_height < cnt :
            max_height = cnt

    print(f'#{i} {max_height}')
