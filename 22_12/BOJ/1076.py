import sys

color = {
    'black': (0, 1),
    'brown': (1, 10),
    'red': (2, 100),
    'orange': (3, 1000),
    'yellow': (4, 10000),
    'green': (5, 100000),
    'blue': (6, 1000000),
    'violet': (7, 10000000),
    'grey': (8, 100000000),
    'white': (9, 1000000000),
}
num = []
for i in range(3):
    a = sys.stdin.readline().rstrip()
    if i == 2:
        num.append(color[str(a)][1])
    else:
        num.append(color[str(a)][0])
print((num[0]*10 + num[1]) * num[2])
