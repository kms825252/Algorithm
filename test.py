def preorder(n):  # 전위순회
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):    # 중위순회
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

def postorder(n):    # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


# 간선 수
E = int(input())
arr = list(map(int, input().split()))
# 정점 수
V = E +1
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(E):
    p,c = arr[i*2] ,arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] =c

preorder(1)