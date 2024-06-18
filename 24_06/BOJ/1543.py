from sys import stdin as ss

''' 31120KB 40ms'''
doc = ss.readline().rstrip()
word = ss.readline().rstrip()

idx = 0
cnt = 0

while idx <= len(doc) - len(word):
    if doc[idx:idx+len(word)] == word:
        cnt += 1
        idx += len(word)

    else:
        idx += 1

print(cnt)
