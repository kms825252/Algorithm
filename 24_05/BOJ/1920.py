from sys import stdin as ss

n = int(ss.readline())
n_num = list(map(int, ss.readline().split()))
check_list = {}
for i in n_num:
    check_list[i] = 1

m = int(ss.readline())
m_num = list(map(int, ss.readline().split()))

# for i in m_num:
#     try:
#         print(check_list[i])
#     except KeyError:
#         print(0)

for i in m_num:
    if check_list.get(i):
        print(check_list[i])

    else:
        print(0)
