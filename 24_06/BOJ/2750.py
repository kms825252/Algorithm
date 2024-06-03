from sys import stdin as ss

n = int(ss.readline())
num_list = [int(ss.readline())]

for _ in range(n-1):
    idx = 0
    new_num = int(ss.readline())
    for i in num_list:
        if i > new_num:
            num_list.insert(idx, new_num)
            break

        idx += 1

    else:
        num_list.append(new_num)

for i in num_list:
    print(i)
