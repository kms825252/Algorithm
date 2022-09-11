N=int(input())
cnt0 = 0
cnt1 = 0
for tc in range(1, N+1):
    a= int(input())
    if a== 0:
        cnt0 +=1

    else:
        cnt1 +=1
if cnt0 > cnt1 :
    print('Junhee is not cute!')

else:
    print("Junhee is cute!")
