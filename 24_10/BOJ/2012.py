from sys import stdin as ss

'''
52504KB 504ms

N명의 예상등수를 이용해서 동석차 없이 등수를 매길 때
실제등수와 예상등수의 차인 불만도를 최소로 할 때 그 불만도 출력


예상등수를 리스트로 받아서 오름차순으로 정렬 후 1등 부터 넣을 후 불만도 구함
'''

N = int(ss.readline())
score_list = []
result = 0

for _ in range(N):
    score_list.append(int(ss.readline()))

score_list.sort()

for i in range(1, N+1):
    result += abs(score_list[i-1] - i)

print(result)