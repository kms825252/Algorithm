from sys import stdin as ss

'''
31252KB 40ms
'''

S = ss.readline().rstrip()

cnt_0 = 0
cnt_1 = 0

if S[0] == '1':
    cnt_1 += 1
else:
    cnt_0 += 1


for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            cnt_1 += 1
        else:
            cnt_0 += 1

print(min(cnt_0,cnt_1))