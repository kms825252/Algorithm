word = list(input())
cnt = 0
word = ['a', 'a'] + word
for i in range(2,len(word)):
    if word[i] == '-':
        if word[i-1] == 'c' or word[i-1] == 'd':
            cnt += 1

    if word[i] == '=':
        if word[i-1] == 's':
            cnt += 1
        elif word[i-1] == 'c':
            cnt += 1
        elif word[i-1] == 'z':
            if word[i-2] == 'd':
                cnt += 2
            else:
                cnt += 1
    if word[i] == 'j':
        if word[i-1] == 'l' or word[i-1] == 'n':
            cnt += 1

print(len(word) - 2 - cnt)