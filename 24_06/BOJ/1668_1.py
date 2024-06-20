from sys import stdin as ss

'''31120KB 32ms'''
def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result


n = int(ss.readline())
array = []

for _ in range(n):
    array.append(int(ss.readline()))

print(ascending(array))
array.reverse()
print(ascending(array))
