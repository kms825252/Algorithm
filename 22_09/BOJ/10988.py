word = input()

flag = 1
for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        flag = 0
        break

print(flag)

