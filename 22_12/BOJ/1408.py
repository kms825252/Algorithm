a_h, a_m, a_s = map(int, input().split(':'))
b_h, b_m, b_s = map(int, input().split(':'))

ans_s = b_s - a_s
if ans_s < 0:
    ans_s = 60 + ans_s
    b_m = b_m - 1
if ans_s < 10 :
    ans_s = '0' + str(ans_s)

ans_m = b_m - a_m
if ans_m < 0:
    ans_m = 60 + ans_m
    b_h = b_h - 1
if ans_m < 10 :
    ans_m = '0' + str(ans_m)

ans_h = b_h - a_h
if ans_h < 10 :
    ans_h = '0' + str(ans_h)

print(f'{ans_h}:{ans_m}:{ans_s}')