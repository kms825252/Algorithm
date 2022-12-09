remain = 0
t = int(input())
for _ in range(t):
    student, apple = map(int, input().split())
    remain += apple - (apple // student) * student

print(remain)