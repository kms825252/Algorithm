a = list(input())

height = 10
for i in range(1, len(a)):
    if a[i-1] == '(' and a[i] == ')':
        height += 10
    elif a[i-1] == ')' and a[i] == '(':
        height += 10

    elif a[i] == '(':
        height += 5

    elif a[i] == ')':
        height += 5

print(height)
