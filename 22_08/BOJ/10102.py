T = int(input())
a = list(input())
a_cnt = 0
b_cnt = 0
for i in a:
    if i == 'A':
        a_cnt +=1
    else:
        b_cnt +=1

if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
else:
    print('Tie')
