x, y, w,h = map(int, input().split())

my_list = [w-x, x, h-y, y]
print(min(my_list))