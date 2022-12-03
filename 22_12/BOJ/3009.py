x_lst = []
y_lst = []
for _ in range(3):
    x, y = input().split()
    x_lst.append(x)
    y_lst.append(y)

for i in range(3):
    if x_lst.count(x_lst[i]) == 1 :
        x_ans = x_lst[i]
    if y_lst.count(y_lst[i]) == 1 :
        y_ans = y_lst[i]

print(x_ans, y_ans)