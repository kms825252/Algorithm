from itertools import combinations

word = []
puzzle = []
flag = 1

while True:
    n = input()
    if n == '#':
        break
    if n =='-':
        flag = 0
    else:
        if flag:
            temp = []
            for i in n:
                temp.append(i)
            word.append(temp)
        else:
            puzzle.append(n)
print(word)


for i in puzzle:
    alphabet = []
    for j in i:
        alphabet.append(j)

    for idx in range(9):
        a = alphabet.pop(idx)
        print(a)


