from sys import stdin as ss

'''31120KB 40ms'''
N = int(ss.readline())
idx = 0
book_dict = {}

for _ in range(N):
    title = ss.readline().rstrip()
    if title not in book_dict.keys():
        book_dict[title] = 1

    else:
        book_dict[title] += 1

sorted_book_dict = sorted(book_dict.items(), key=lambda x: (-x[1], x[0]))
'''
-x[1] : value값을 기준으로 내림차순(큰 값부터 정렬)
x[0] : 1조건인 -x[1]정렬을 시행한 이후에 key값을 기준으로 오름차순(작은 값부터 or ABC순)
'''

print(sorted_book_dict[0][0])