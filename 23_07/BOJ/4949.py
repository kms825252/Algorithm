while True:
    cnt = 0
    stk = []
    word = list(input())
    if word[0] == '.':
        break

    try:
        for i in range(len(word)):
            if '(' in word[i]:
                stk.append('(')
            elif ')' in word[i]:
                if stk[-1] != '(':
                    print('no')
                    break
                else:
                    stk.pop()

            elif '[' in word[i]:
                stk.append('[')
            elif ']' in word[i]:
                if stk[-1] != '[':
                    print('no')
                    break
                else:
                    stk.pop()

        else:
            if stk:
                print('no')
            else:
                print('yes')

    except:
        print('no')