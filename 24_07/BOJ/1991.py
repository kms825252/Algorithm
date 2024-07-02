from sys import stdin as ss

'''
31120KB 36ms
전위 순회, 중위 순회, 후위 순회를 만드는 문제
일단 특정 알파벳의 자식 값을 쉽게 가져오기 위해 딕셔너리를 이용해서 tree를 구현

전위 순회는 
먼저 출력하고 왼쪽부터 들어감 그 후 오른쪽

중위 순회는
먼저 왼쪽부터 쭉 들어가고 출력 그 후 오른쪽

후위 순회는
왼쪽 들어가고 오른쪽 들어가고 출력
'''


def pre_order(word):
    if word == '.':
        return
    print(word, end='')
    pre_order(arr[word][0])
    pre_order(arr[word][1])


def in_order(word):
    if word == '.':
        return
    in_order(arr[word][0])
    print(word, end='')
    in_order(arr[word][1])


def post_order(word):
    if word == '.':
        return
    post_order(arr[word][0])
    post_order(arr[word][1])
    print(word, end='')


N = int(ss.readline())
arr = {}

for _ in range(N):
    root, left, right = ss.readline().split()
    arr[root] = (left, right)

pre_order('A')
print()
in_order('A')
print()
post_order('A')