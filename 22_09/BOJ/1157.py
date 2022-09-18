word = list(input())
case = []
count_word = [0, 0]
cnt = 0

for i in word:
    code = ord(i)
    if code > 96:
        code = code - 32
    case.append(chr(code))

for i in set(case):
    a = case.count(i)
    if a > count_word[1]:
        count_word[0] = i
        count_word[1] = a
        cnt = 0
    elif a == count_word[1]:
        cnt += 1

if cnt >= 1:
    print('?')
else:
    print(count_word[0])