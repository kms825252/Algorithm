from sys import stdin as ss

N = int(ss.readline())
block = []

for i in range(1, N+1):
    area, height, weight = map(int, ss.readline().split())
    block.append((i, area, height, weight))

dp_cnt = [1]*N
dp_idx = []
dp_height = []

block_area = sorted(block, key=lambda x: x[1], reverse=True)
dp_idx.append([block_area[0][0]])
dp_height.append(block_area[0][2])
max_dp_cnt = 0
print(block_area)

for i in range(1, N):
    idx = 0
    print('asdfasdf', i)
    temp = [0] * i
    for j in range(i):
        if block_area[i][3] < block_area[j][3]:
            dp_cnt[i] = max(dp_cnt[i], dp_cnt[j]+1)
            temp[j] = 1

    if dp_cnt[i] > max_dp_cnt:
        dp_idx[idx].append(block_area[i][0])
        max_dp_cnt = dp_cnt[i]

    else:
        dp_idx.append([])
        idx += 1
        for k in range(len(temp)):
            if temp[k] == 1:
                dp_idx[idx].append(block_area[k][0])
        dp_idx[idx].append(block_area[i][0])

print(dp_cnt)
print(dp_idx)










#         else:
#             for
#         dp_cnt[i] = max(dp_cnt[i], dp_cnt[j]+1)
#         #
#         # else:
#         #     dp_idx.append()
#     if dp_cnt[i] <= dp_cnt[i-1]:
#         dp_idx.append([block_area[i][0]])
#         dp_height.append(block_area[i][2])
#
# print('asdfasdf', block_area)
# print(dp_cnt)
#
# print(dp_height)
# print(dp_idx)
#
# max_height = 0
# answer_idx = 0
# for i in range(len(dp_height)):
#     if max_height < dp_height[i]:
#         max_height = dp_height[i]
#         answer_idx = i
#
# print(len(dp_idx[answer_idx]))
# for i in dp_idx[answer_idx][::-1]:
#     print(i)