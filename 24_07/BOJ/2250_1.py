from sys import stdin as ss

'''
33748KB 1100ms

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

tree = dict(sorted(tree.items(), key=lambda x: x[0]))

pre(tree, root[0])

result_level = 0
result_width = 0

for i in range(1, len(level)):
    a = width.index(level[i][-1]) - width.index(level[i][0]) + 1
    if result_width < a:
        result_width = a
        result_level = i

print(result_level, result_width)