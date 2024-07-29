data = [[1,2,3,],[4,5,],[6,7,8,9]]
print(data[0])
print(data[2][1])
for sub in data:
    for item in sub:
        print(item, end='')
    print()