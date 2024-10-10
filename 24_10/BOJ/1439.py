from sys import stdin as ss

'''
31120KB 32ms
숫자 뒤집기
0과 1로 된 문자열을 최소 횟수로 같은 숫자로 만들기

연속된 하나 이상의 숫자를 다 뒤집을 수 있음
'''

S = ss.readline().rstrip()
splitted_S_1 = S.split('1')
splitted_S_0 = S.split('0')

cnt_0 = 0
cnt_1 = 0

for i in splitted_S_1:
    if '0' in i:
        cnt_0 += 1

for i in splitted_S_0:
    if '1' in i:
        cnt_1 += 1

print(min(cnt_1, cnt_0))
