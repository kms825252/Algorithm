from sys import stdin as ss

'''
시간초과

'''

a = ss.readline().rstrip()
b = ss.readline().rstrip()

word_length = 0

def find_word(idx1, idx2):
    global dp
    global word_length

    for i in range(idx1+1, len(a)):
        for j in range(idx2+1, len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[idx1][idx2] + 1
                word_length = max(word_length, dp[i][j])
                find_word(i, j)

for i in range(len(a)):
    for j in range(len(b)):
        dp = [[0] * len(b) for _ in range(len(a))]
        if a[i] == b[j]:
            dp[i][j] += 1
            find_word(i, j)

print(word_length)

