from sys import stdin as ss

'''
31120KB 56ms
책의 개수가 1000보다 작거나 같은 자연수 
10000개 이하를 탐색할 때 리스트와 딕셔너리의 속도 차이는 크게 없다

'''

N = int(ss.readline())
idx = 0
book_dict = {}
book_cnt = [0] * 1000


# { '책 제목' : 인덱스 } 형태
for _ in range(N):
    title = ss.readline().rstrip()
    if title not in book_dict.keys():
        book_dict[title] = idx
        book_cnt[idx] += 1
        idx += 1

    else:
        book_cnt[book_dict[title]] += 1

# result에 가장 많이 팔린 책을 넣기
result = []
for i in range(len(book_cnt)):
    if book_cnt[i] == max(book_cnt):
        for k, v in book_dict.items():
            if v == i:
                result.append(k)

print(min(result))