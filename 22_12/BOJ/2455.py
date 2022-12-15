count = 0
max_cnt = 0
for _ in range(4):
    out_num, in_num = map(int, input().split())
    count = count + in_num - out_num
    print(count)
    if max_cnt < count:
        max_cnt = count

print(max_cnt)