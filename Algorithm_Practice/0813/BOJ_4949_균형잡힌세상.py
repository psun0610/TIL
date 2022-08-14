while 1:
    sent = input()
    if sent == '.':
        break
    
    stack = []
    
    a = 0
    b = 0
    ans = 'yes'
    for s in sent:
        if s == '(':
            a += 1
            stack.append('(')

        elif s == ')':
            if a > 0:
                tmp = stack.pop()
                if tmp == '(':
                    a -= 1
                elif tmp == '[':
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break

        elif s == '[':
            b += 1
            stack.append('[')

        elif s == ']':
            if b > 0:
                tmp = stack.pop()
                if tmp == '[':
                    b -= 1
                elif tmp == '(':
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
    else:
        if len(stack) != 0:
            ans = 'no'
    print(ans)