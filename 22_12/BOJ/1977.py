a = int(input())
b = int(input())

a1 = a**(1/2)
b1 = b**(1/2)

if int(a1) == a1:
    a1 = int(a1)
else:
    a1 = int(a1) + 1

b1 = int(b1)

my_sum = 0
my_list = list(range(a1,b1+1))

if my_list:
    for i in my_list:
        my_sum += i ** 2
    print(my_sum)
    print(my_list[0]**2)

else:
    print(-1)