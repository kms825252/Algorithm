T = int(input())
cnt = 0
for tc in range(1, T+1):
    word = list(input())
    word = ['0'] + word
    a = []
    for i in range(1, len(word)):
        if word[i] in a and word[i-1] != word[i]:
            break
        else:
            a.append(word[i])
    else:
        cnt += 1

print(cnt)