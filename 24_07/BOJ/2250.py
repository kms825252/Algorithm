from sys import stdin as ss

'''
33748KB 1100ms

pre라는 중위순회를 하며
width라는 리스트에 x좌표에 해당하는 인덱스에 노드를 넣는다.
(중위순회를 하며 왼쪽으로 계속 들어갔을 때 처음으로 하위 노드에 -1이 나오면 그 노드가 x좌표에서 1번을 차지한다.)

그리고 level이라는 2중 배열을 만들어 level에 따른 노드들의 값을 모아준다.

tree의 키값 중에서 하위노드들로 나온 값들을 제외하여 root를 찾아낸다.

그리고 가장 넓은 너비의 level과 width를 찾아낸다.


반례
1. 루트가 1이 아닐 때
2. 노드가 1개일때 
3. tree가 정렬되어 있지 않을 때
4. 1번에서 루트가 가장 작은 수라 생각해서 정렬을 했는데 다른 수가 루트가
    될 수 있어서 dict의 key값들에서 하위 노드가 나왔던 것들을 제외하며 root를 찾아냄

'''
def pre(arr, node):
    global coord_x
    global coord_y
    global level
    global width

    if node == -1:
        return

    coord_y += 1
    try:
        level[coord_y].append(node)
    except:
        level.append([node])

    #왼쪽
    pre(arr, arr[node][0])

    width[coord_x] = node
    coord_x += 1

    #오른쪽
    pre(arr, arr[node][1])

    coord_y -= 1


N = int(ss.readline())
tree = {}
root = []

coord_x = 1
coord_y = 0
level = [[]]
width = [0] * (N+1)

for _ in range(N):
    node, left, right = map(int, ss.readline().rstrip().split())
    tree[node] = (left, right)

root = list(tree.keys())

for i in tree.values():
    if i[0] in root:
        root.remove(i[0])
    if i[1] in root:
        root.remove(i[1])

pre(tree, root[0])

result_level = 0
result_width = 0

for i in range(1, len(level)):
    a = width.index(level[i][-1]) - width.index(level[i][0]) + 1
    if result_width < a:
        result_width = a
        result_level = i

print(result_level, result_width)