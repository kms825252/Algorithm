import sys

sum_num = 0.0
sum_score = 0.0
for _ in range(20):
    sub, score, grade = sys.stdin.readline().split()
    if grade == 'A+':
        grade = 4.5
    elif grade == 'A0':
        grade = 4.0
    elif grade == 'B+':
        grade = 3.5
    elif grade == 'B0':
        grade = 3.0
    elif grade == 'C+':
        grade = 2.5
    elif grade == 'C0':
        grade = 2.0
    elif grade == 'D+':
        grade = 1.5
    elif grade == 'D0':
        grade = 1.0
    elif grade == 'F':
        grade = 0.0
    else:
        continue

    score = float(score)
    sum_num += score * grade
    sum_score += score

print(sum_num/sum_score)