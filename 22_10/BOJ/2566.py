case = [list(map(int, input().split())) for _ in range(9)]
my_max = case[0][0]
my_i = 0
my_j = 0
for i in range(9):
    for j in range(9):
        if case[i][j] > my_max:
            my_max = case[i][j]
            my_i = i
            my_j = j

print(my_max)
print(my_i+1, my_j+1)

